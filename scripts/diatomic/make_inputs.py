import json
import os
import subprocess
from qcelemental import constants as qcel

def _getParamsFrom(name):
    M = 1
    if name[0].isdigit():
        M = int(name[0])
        name = name[1:]
    Q = 0
    if name[-1] in ["+", "-"]:
        Q = 1 if name[-1] == "+" else -1
        name = name[:-1]
    if len(name) == 4:
        Z1 = name[:2]
        Z2 = name[2:]
    elif len(name) == 3:
        if name[-1] == "2":
            Z1 = name[:2]
            Z2 = name[:2]
        elif name[-1].islower():
            Z1 = name[0]
            Z2 = name[1:]
        elif name[-2].islower():
            Z1 = name[:2]
            Z2 = name[2]
    elif len(name) == 2:
        if name[-1] == "2":
            Z1 = name[0]
            Z2 = name[0]
        else:
            Z1 = name[0]
            Z2 = name[1]
    return Z1, Z2, Q, M
            
with open(os.path.join("inputs", "cbs_data.json"), "r") as infile:
    jsdata = json.load(infile)
    cbsdata = jsdata["Lehtola"]
    cbsdata.update(jsdata["Kraus"])
    

with open(os.path.join("inputs", "helfem_inputs.json"), "r") as infile:
    helfemdata = json.load(infile)

outputdict = {}
for diatomic in helfemdata.keys():
    if diatomic in cbsdata:
        print(diatomic)
        Z1, Z2, Q, M = _getParamsFrom(diatomic)
        R = cbsdata[diatomic]["R"]
        u = qcel.bohr2angstroms if cbsdata[diatomic].get("u", "B0") == "A" else 1.0
        item = {
                "molecule": {
                    "symbols": [Z1, Z2],
                    "geometry": [0.0, 0.0, 0.0, 0.0, 0.0, R/u],
                    "molecular_charge": int(Q),
                    "molecular_multiplicity": int(M)
                }, 
                "driver": "energy", 
                "model": {},
                "keywords": {
                    "reference": "UKS",
                    "scf_type":  "PK",
                    "e_convergence": 1e-10,
                    "dft_spherical_points": 974,
                    "dft_radial_points": 150,
                    "guess": "SAP"
                }
               }
        outputdict[diatomic] = item
        
with open(os.path.join("inputs", "psi4_inputs.json"), "w") as outfile:
    json.dump(outputdict, outfile, indent=1)
