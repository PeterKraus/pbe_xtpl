import os
import json
import argparse
import hashlib
import math
import subprocess
from qcelemental import constants as qcelc

parser = argparse.ArgumentParser(description="Prepare single point energies of all xyz files in specified folder")

parser.add_argument('--xyzpath', help="folder containing XYZ files")
parser.add_argument('--functional', help="method to use", required = True, type = str.lower)
parser.add_argument('--basis', help="basis set to use", required = True, type = str.lower)
parser.add_argument('--nthreads', help="number of threads", default=4, type = int)
parser.add_argument('--memory', help="amount of memory", default=4, type = float)
parser.add_argument('--cluster', default="zeus", type = str.lower)

args = parser.parse_args()

# check that all job jsons are created
assert os.path.exists(args.xyzpath) and os.path.isdir(args.xyzpath)
inputs, bench = os.path.split(args.xyzpath)
jobpath = os.path.join("jobs", bench)
outpath = os.path.join("outputs", bench)

molecules = [mol for mol in os.listdir(args.xyzpath) if mol.endswith("xyz")]
os.makedirs(jobpath, exist_ok = True)
jsonfiles = [jsf for jsf in os.listdir(jobpath) if jsf.endswith("json")]
for mol in molecules:
    if mol[:-4] + ".json" in jsonfiles:
        continue
    else:
        try:
            with open(os.path.join(args.xyzpath, mol), "r") as infile:
                xyzlines = infile.readlines()
            n = int(xyzlines.pop(0).strip())
            chg, mul = [int(each.replace(",", "")) for each in xyzlines.pop(0).strip().split()]
            symbols = []
            geometry = []
            while len(xyzlines) > 0:
                line = xyzlines.pop(0).strip()
                if line != "":
                    el, x, y, z = line.split()
                    symbols.append(el)
                    geometry.append(float(x)/qcelc.bohr2angstroms)
                    geometry.append(float(y)/qcelc.bohr2angstroms)
                    geometry.append(float(z)/qcelc.bohr2angstroms)
        except ValueError:
            print(mol)
            raise
        molschema = {
            "molecule": {
                "symbols": symbols,
                "geometry": geometry,
                "molecular_charge": chg,
                "molecular_multiplicity": mul
            },
            "driver": "energy",
            "model": {},
            "keywords": {
                "reference": "RKS" if mul == 1 else "UKS",
                "dft_spherical_points": 974,
                "dft_radial_points": 150,
                "guess": "SAP"
            }
        }
        with open(os.path.join(jobpath, mol[:-4] + ".json"), "w") as outfile:
            json.dump(molschema, outfile, indent=1)

# list all jobs and create jobfiles
jsonfiles = [jsf for jsf in os.listdir(jobpath) if jsf.endswith("json")]
os.makedirs(outpath, exist_ok = True)
outfiles = [jsf for jsf in os.listdir(outpath) if jsf.endswith("json")]
skipped = 0
for jsmol in jsonfiles:
    casename = f"{args.functional} {args.basis} {jsmol[:-5]}"
    casehash = hashlib.sha256(casename.encode("utf-8")).hexdigest()[:10]
    if casehash + ".json" in outfiles:
        try:
            with open(os.path.join(outpath, casehash + ".json"), "r") as qmfile:
                qmdata = json.load(qmfile)
                if qmdata["success"]:
                    skipped += 1
                    continue
                else:
                    raise RuntimeError
        except:
            pass
    if os.path.exists(casehash + ".sl") or args.cluster != "zeus":
        pass
    else:
        slurmlines = []
        slurmlines.append("#!/bin/bash --login")
        #slurmlines.append("#SBATCH --partition=workq")
        slurmlines.append("#SBATCH --partition=highmemq")
        slurmlines.append("#SBATCH --nodes=1")
        slurmlines.append(f"#SBATCH --ntasks={args.nthreads:d}")
        slurmlines.append(f"#SBATCH --mem={math.ceil(args.memory):d}GB")
        slurmlines.append("#SBATCH --account=f97")
        slurmlines.append("#SBATCH --time=24:00:00")
        slurmlines.append("#SBATCH --export=NONE")
        slurmlines.append(f"#SBATCH --job-name={casehash}")
        slurmlines.append(f"#SBATCH --output={casehash}.out")
        slurmlines.append(f"srun --export=all -n 1 -c {args.nthreads} {casehash}.sh")
        with open(casehash + ".sl", "w") as slfile:
            slfile.write("\n".join(slurmlines) + "\n")
    if os.path.exists(casehash + ".sh"):
        pass
    else:
        shellines = []
        shellines.append("#!/bin/bash")
        if args.cluster == "zeus":
            shellines.append("export PATH=/group/f97/kraus/miniconda3/bin:$PATH")
            shellines.append("export PSI_SCRATCH=/scratch/f97/kraus/scratch/")
        elif args.cluster == "bignimbus":
            shellines.append("export PATH=/home/ubuntu/pk/Applications/miniconda3/bin:$PATH")
            shellines.append("source /home/ubuntu/pk/Applications/.bin/conda.source")
        shellines.append("source activate psi4-1.4a2.dev923")
        shellines.append(f"python runner.py --input={os.path.join(jobpath, jsmol)} " + \
                         f"--output={os.path.join(outpath, casehash + '.json')} " + \
                         f"--functional={args.functional} --basis={args.basis} " + \
                         f'--clean={casehash} --tag="{casename}" ' + \
                         f"--memory={args.memory} --nthreads={args.nthreads}")
        with open(casehash + ".sh", "w") as shfile:
            shfile.write("\n".join(shellines) + "\n")
        subprocess.run(["chmod", "+x", f"{casehash}.sh"])
        #subprocess.run(["sbatch", f"{casehash}.sl"])
print(skipped, len(outfiles))
