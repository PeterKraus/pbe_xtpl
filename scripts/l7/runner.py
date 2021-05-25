import psi4
import os
import json
import qcengine as qcng
import argparse

parser = argparse.ArgumentParser(description="Run single point energies of an json schema files")

parser.add_argument('--input', help="path to JSON schema file")
parser.add_argument('--output', help="requested output path")
parser.add_argument('--functional', help="method to use", required = True, type = str.lower)
parser.add_argument('--basis', help="basis set to use", required = True, type = str.lower)
parser.add_argument('--nthreads', help="number of threads", default=4, type = int)
parser.add_argument('--memory', help="amount of memory", default=4, type = float)
parser.add_argument('--clean', help="file prefix to clean", default = False)
parser.add_argument('--tag', default="")

args = parser.parse_args()

assert os.path.exists(args.input)
with open(args.input, "r") as infile:
    molschema = json.load(infile)

molschema["driver"] = "energy"
molschema["model"] = {
    "method": args.functional,
    "basis": args.basis
}

molschema["keywords"] = {
    "guess": "SAP",
    "freeze_core": "true",
    "dft_vv10_postscf": "true"
}

ret = qcng.compute(molschema, "psi4",
                    return_dict=True,
                    local_options={"memory": args.memory, "ncores": args.nthreads})
if ret["success"]:
    ret["tag"] = args.tag
    with open(args.output, "w") as outfile:
        json.dump(ret, outfile, indent=1)
    if args.clean:
        cleanlist = [fn for fn in os.listdir(os.getcwd()) if fn.startswith(args.clean)]
        for fn in cleanlist:
            os.remove(fn)
else:
    print(ret)
    raise RuntimeError
            
