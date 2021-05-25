import psi4
import json
import argparse
import os
import sys
import hashlib

parser = argparse.ArgumentParser(
    description="Run a geometry optimization starting with an xyz file and a method")
parser.add_argument("xyzfile", help = "path to input XYZ file")
parser.add_argument("--functional", help = "method to use",
                    default="b3lyp-d3bj", type = str.lower)
parser.add_argument('--basis', help="basis set to use",
                    default="def2-svpd", type = str.lower)
parser.add_argument('--nthreads', help="number of threads", default=4, type = int)
parser.add_argument('--memory', help="amount of memory (GB)", default=4, type = float)
parser.add_argument('--outpath', help="path to putput folder", default="results")
parser.add_argument('--cluster', default="local", type = str.lower)
parser.add_argument('--hess', default=-1, type = int)
parser.add_argument('--dyn', default=0, type = int)

args = parser.parse_args()

assert os.path.exists(args.xyzfile)
infolder, xyzfile = os.path.split(args.xyzfile)
method = f"{args.functional}/{args.basis}"
outmoltag = f"{method}:{xyzfile}"
outmolhash = hashlib.sha256(outmoltag.encode("utf-8")).hexdigest()[:10]
outmolfn = f"{outmolhash}.xyz"

if os.path.exists(os.path.join(args.outpath, outmolfn)):
    print(f"Job {outmoltag} already performed. Skipping.")
    sys.exit()

print(f"Calculating job {outmoltag} now.")
with open(os.path.join(infolder, xyzfile), "r") as infile:
    inmolstr = infile.read().strip()
inmol = psi4.geometry(inmolstr)

psi4.set_memory(f"{args.memory:4f}GB")
psi4.set_num_threads(args.nthreads)
psi4.set_options({
    "dft_spherical_points": 974,
    "dft_radial_points": 150,
    "g_convergence": "interfrag_tight",
    "full_hess_every": args.hess,
    "dynamic_level": args.dyn
})


E, wfn = psi4.optimize(method, molecule = inmol, return_wfn = True)
outmolarr = wfn.molecule().save_string_xyz_file().split("\n")
outmolarr[1] = outmoltag
os.makedirs(args.outpath, exist_ok = True)
with open(os.path.join(args.outpath, f"{outmolhash}.xyz"), "w") as outfile:
    outfile.write("\n".join(outmolarr))
