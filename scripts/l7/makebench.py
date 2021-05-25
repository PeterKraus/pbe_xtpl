import os
import json
import argparse
import hashlib
import math
import subprocess
from qcelemental import constants as qcelc

parser = argparse.ArgumentParser(description="Prepare single point energies of all xyz files in specified folder")

parser.add_argument('--jsonpath', help="folder containing JSON files")
parser.add_argument('--functional', help="method to use", required = True, type = str.lower)
parser.add_argument('--basis', help="basis set to use", required = True, type = str.lower)
parser.add_argument('--nthreads', help="number of threads", default=4, type = int)
parser.add_argument('--memory', help="amount of memory", default=4, type = float)
parser.add_argument('--cluster', default="zeus", type = str.lower)

args = parser.parse_args()
outpath = "outputs"
jobpath = args.jsonpath

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
    if os.path.exists(casehash + ".sl") or args.cluster == "bignimbus":
        pass
    else:
        slurmlines = []
        slurmlines.append("#!/bin/bash --login")
        if args.cluster == "zeus":
           slurmlines.append("#SBATCH --partition=workq")
        elif args.cluster == "bigzeus":
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
        if args.cluster == "zeus" or args.cluster == "bigzeus":
            shellines.append("export PATH=/group/f97/kraus/miniconda3/bin:$PATH")
            shellines.append("export PSI_SCRATCH=/scratch/f97/kraus/scratch/")
        elif args.cluster == "bignimbus":
            shellines.append("export PATH=/home/ubuntu/pk/Applications/miniconda3/bin:$PATH")
            shellines.append("source /home/ubuntu/pk/Applications/.bin/conda.source")
            shellines.append("export PSI_SCRATCH=/home/ubuntu/pk/scratch/")
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
