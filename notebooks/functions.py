zetacolors = {
    "cc-pvdz":      "#238b45", "cc-pvtz":      "#74c476", "cc-pvqz":      "#bae4b3", "cc-pv5z":      "#edf8e9",
    "aug-cc-pvdz":  "#238443", "aug-cc-pvtz":  "#78c679", "aug-cc-pvqz":  "#c2e699", "aug-cc-pv5z":  "#ffffcc",
    "def2-svp":     "#6a51a3", "def2-tzvp":    "#9e9ac8", "def2-qzvp":    "#cbc9e2",
    "def2-svpd":    "#88419d", "def2-tzvpd":   "#8c96c6", "def2-qzvpd":   "#b3cde3",
    "cc-pwcvdz":    "#d94701", "cc-pwcvtz":    "#fd8d3c", "cc-pwcvqz":    "#fdbe85", "cc-pwcv5z":    "#feedde",
    "aug-cc-pwcvdz":"#e31a1c", "aug-cc-pwcvtz":"#fd8d3c", "aug-cc-pwcvqz":"#fecc5c", "aug-cc-pwcv5z":"#ffffb2",
    "pcseg-1":      "#2171b5", "pcseg-2":      "#6baed6", "pcseg-3":      "#bdd7e7",
    "aug-pcseg-1":  "#225ea8", "aug-pcseg-2":  "#41b6c4", "aug-pcseg-3":  "#a1dab4" 
}
zetacolors["cc-pvdz-pp"] = zetacolors["cc-pvdz"]
zetacolors["cc-pvtz-pp"] = zetacolors["cc-pvtz"]
zetacolors["cc-pvqz-pp"] = zetacolors["cc-pvqz"]
zetacolors["cc-pv5z-pp"] = zetacolors["cc-pv5z"]


extrapolations = {
    "cc-pv[dt]z": {"comps": ["cc-pvdz", "cc-pvtz"], "zetas": [2,3], "α0": 3.622, "αx": 1.511, "αc": 0.005, "αdh": 2.2},
    "cc-pv[tq]z": {"comps": ["cc-pvtz", "cc-pvqz"], "zetas": [3,4], "α0": 3.622, "αx": 1.511, "αc": 0.005, "αdh": 3.0},
    "cc-pv[dt]z-pp": {"comps": ["cc-pvdz-pp", "cc-pvtz-pp"], "zetas": [2,3], "α0": 3.622, "αx": 1.511, "αc": 0.005, "αdh": 2.2},
    "cc-pv[tq]z-pp": {"comps": ["cc-pvtz-pp", "cc-pvqz-pp"], "zetas": [3,4], "α0": 3.622, "αx": 1.511, "αc": 0.005, "αdh": 3.0},
    "aug-cc-pv[dt]z": {"comps": ["aug-cc-pvdz", "aug-cc-pvtz"], "zetas": [2,3], "α0": 3.676, "αx": 1.887, "αc": 0.139, "αdh": 2.2},
    "aug-cc-pv[tq]z": {"comps": ["aug-cc-pvtz", "aug-cc-pvqz"], "zetas": [3,4], "α0": 3.676, "αx": 1.887, "αc": 0.139, "αdh": 3.0},
    "def2-[st]zvp": {"comps": ["def2-svp", "def2-tzvp"], "zetas": [2,3], "α0": 7.406, "αx": 1.266, "αc": -0.046, "αdh": 2.2},
    "def2-[st]zvpp": {"comps": ["def2-svp", "def2-tzvpp"], "zetas": [2,3], "α0": 7.408, "αx": 1.267, "αc": -0.046, "αdh": 2.2},
    "def2-[st]zvpd": {"comps": ["def2-svpd", "def2-tzvpd"], "zetas": [2,3], "α0": 7.925, "αx": 1.370, "αc": 0.101, "αdh": 2.2},
    "def2-[st]zvppd": {"comps": ["def2-svpd", "def2-tzvppd"], "zetas": [2,3], "α0": 7.927, "αx": 1.371, "αc": 0.101, "αdh": 2.2},
    "def2-[tq]zvp": {"comps": ["def2-tzvp", "def2-qzvp"], "zetas": [3,4], "α0": 7.406, "αx": 1.266, "αc": -0.046, "αdh": 3.0},
    "def2-[tq]zvpp": {"comps": ["def2-tzvp", "def2-qzvpp"], "zetas": [3,4], "α0": 7.408, "αx": 1.267, "αc": -0.046, "αdh": 3.0},
    "def2-[tq]zvpd": {"comps": ["def2-tzvpd", "def2-qzvpd"], "zetas": [3,4], "α0": 7.925, "αx": 1.370, "αc": 0.101, "αdh": 3.0},
    "def2-[tq]zvppd": {"comps": ["def2-tzvppd", "def2-qzvppd"], "zetas": [3,4], "α0": 7.927, "αx": 1.371, "αc": 0.101, "αdh": 3.0},
    "cc-pwcv[dt]z": {"comps": ["cc-pwcvdz", "cc-pwcvtz"], "zetas": [2,3], "α0": 4.157, "αx": 1.192, "αc": -0.048, "αdh": 2.2},
    "cc-pwcv[tq]z": {"comps": ["cc-pwcvtz", "cc-pwcvqz"], "zetas": [3,4], "α0": 4.157, "αx": 1.192, "αc": -0.048, "αdh": 3.0},
    "aug-cc-pwcv[dt]z": {"comps": ["aug-cc-pwcvdz", "aug-cc-pwcvtz"], "zetas": [2,3], "α0": 4.485, "αx": 1.445, "αc": 0.085, "αdh": 2.2},
    "aug-cc-pwcv[tq]z": {"comps": ["aug-cc-pwcvtz", "aug-cc-pwcvqz"], "zetas": [3,4], "α0": 4.485, "αx": 1.445, "αc": 0.085, "αdh": 3.0},
    "pcseg-[12]": {"comps": ["pcseg-1", "pcseg-2"], "zetas": [2,3], "α0": 5.883, "αx": -1.825, "αc": 0.227, "αdh": 2.2},
    "pcseg-[23]": {"comps": ["pcseg-2", "pcseg-3"], "zetas": [3,4], "α0": 5.883, "αx": -1.825, "αc": 0.227, "αdh": 3.0},
    "aug-pcseg-[12]": {"comps": ["aug-pcseg-1", "aug-pcseg-2"], "zetas": [2,3], "α0": 6.166, "αx": -2.137, "αc": 0.296, "αdh": 2.2},
    "aug-pcseg-[23]": {"comps": ["aug-pcseg-2", "aug-pcseg-3"], "zetas": [3,4], "α0": 6.166, "αx": -2.137, "αc": 0.296, "αdh": 3.0},
# OLD DATA
    "cc-pv[dt]z-v1":    {"comps": ["cc-pvdz", "cc-pvtz"], "zetas": [2,3], "α0": 3.974, "αx": 0.0, "αc": 0.0, "αdh": 2.257},
    "cc-pv[dt]z-pp-v1": {"comps": ["cc-pvdz-pp", "cc-pvtz-pp"], "zetas": [2,3], "α0": 3.974, "αx": 0.0, "αc": 0.0, "αdh": 2.257},
    "def2-[st]zvp-v1":  {"comps": ["def2-svp", "def2-tzvp"], "zetas": [2,3], "α0": 9.042, "αx": 0.0, "αc": 0.0, "αdh": 2.096},
    "def2-[st]zvpd-v1": {"comps": ["def2-svpd", "def2-tzvpd"], "zetas": [2,3], "α0": 9.065, "αx": 0.0, "αc": 0.0, "αdh": 2.267},
    "pcseg-[12]-v1":    {"comps": ["pcseg-1", "pcseg-2"], "zetas": [2,3], "α0": 6.366, "αx": 0.0, "αc": 0.0, "αdh": 1.935},
}

def getFuncPars(functional):
    if functional in ["blyp-d3bj", "pbe-d3bj", "revpbe-d3bj", "b97-d3bj", "scan-d3bj", "m06l-d3", "b97m-v", "b97m-d3bj"]:
        return (0.0, 0.0)
    elif functional == "b3lyp-d3bj":
        return (0.2, 0.0)
    elif functional == "wb97x-v":
        return (0.167, 0.0)
    elif functional == "m052x-d3":
        return (0.56, 0.0)
    elif functional == "m062x-d3":
        return (0.54, 0.0)
    elif functional == "dldf+d10":
        return (0.56, 0.0)
    elif functional == "dsd-blyp-d3bj":
        return (0.71, 0.46)
    elif functional == "dsd-pbep86-nl":
        return (0.69, 0.56)
    elif functional == "b2plyp-d3bj":
        return (0.53, 0.27)
    elif functional == "pwpb95-nl":
        return (0.50, 0.269)
    elif functional in ["pbe0-dh-d3bj", "pbe0dh-d3bj"]:
        return (0.5, 0.125)
    else:
        raise ValueError
        
def prettifyBasis(bname, replace = True):
    if "cc" in bname:
        bname = bname.replace("v", "V").replace("z", "Z")
        bname = bname.replace("wc", "wC")
    if "def2" in bname:
        bname = bname.replace("z", "Z").replace("v", "V")
        bname = bname.replace("pd", "PD").replace("p", "P")
    if "zapa" in bname:
        bname = bname.replace("zapa", "ZaPa")
        bname = bname.replace("cv", "CV")
    if "jorge" in bname:
        bname = bname.replace("zp", "ZP")
        bname = bname.replace("a", "A")
    if "X" in bname and "$X$" not in bname:
        bname = bname.replace("X", "$X$")
    if "N" in bname and "$N$" not in bname:
        bname = bname.replace("N", "$N$")
    if replace:
        return bname.replace("q","$X$").replace("3","$N$").replace("5", "$X$")
    else:
        return bname.replace("-s", "-S").replace("st","ST").replace("-t", "-T").replace("-q","-Q")

def prettifyFunc(fname):
    fname = fname.upper()
    if fname.startswith("W"):
        fname = "ω" + fname[1:]
    if fname.startswith("REV"):
        fname = "rev" + fname[3:]
    fname = fname.replace("D3BJ", "D3(BJ)")
    if "D3" in fname and "D3(BJ)" not in fname:
        fname = fname.replace("D3", "D3(0)")
    fname = fname.replace("M062", "M06-2").replace("M052", "M05-2")
    return fname