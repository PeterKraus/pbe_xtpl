import psi4
import os
import json
import math
from qcelemental import constants
import qcengine as qcng
import argparse

parser = argparse.ArgumentParser(description="Run single point energies of all objects in a json file in specified 'benchmark' folder")

parser.add_argument('--input', help="file with input jsons", required = True)
parser.add_argument('--functional', help="method to use", required = True, type = str.lower)
parser.add_argument('--basis', help="basis set to use", required = True, type = str.lower)
parser.add_argument('--nthreads', help="number of threads", default=4, type = int)
parser.add_argument('--memory', help="amount of memory", default=4, type = float)
parser.add_argument('--singlets', help="run singlets only", default = False, 
                                  action = 'store_const', const=True)

args = parser.parse_args()


assert os.path.exists(args.input)
with open(args.input, "r") as infile:
    suite = json.load(infile)

try:
    with open(os.path.join("outputs", f"{args.functional}_{args.basis}.json"), "r") as outfile:
        results = json.load(outfile)
except:
    results = {}
    
with open(os.path.join("outputs", f"{args.functional}_{args.basis}.json"), "w") as outfile:
    json.dump(results, outfile, indent=1)

for item in suite:
    if args.singlets and not item.startswith("1"):
        continue
    with open(os.path.join("outputs", f"{args.functional}_{args.basis}.json"), "r") as outfile:
        results = json.load(outfile)
    if item not in results:
        print(f": Running {item:6s}: {args.functional}/{args.basis}")
        injson = suite[item]
        injson["model"] = {"method": args.functional, "basis": args.basis}
        try:
            ret = qcng.compute(injson, "psi4", 
                               return_dict=True,
                               local_options={"memory": args.memory,
                                              "ncores": args.nthreads,
                                              "scratch_directory": "$PSI_SCRATCH"})
            if ret["success"]:
                print(f'::: {item} done.')
                with open(os.path.join("outputs", f"{args.functional}_{args.basis}.json"), "r") as outfile:
                    results = json.load(outfile)
                results[item] = ret
                with open(os.path.join("outputs", f"{args.functional}_{args.basis}.json"), "w") as outfile:
                    json.dump(results, outfile, indent=1)
            else:
                print(ret)
                raise RuntimeError
        except:
                print(f'::: {item} failed.')
                continue
