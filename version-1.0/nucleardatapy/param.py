import os
import numpy as np  # 1.15.0

#
# nucleardatapy_tk = os.getenv('NUCLEARDATAPY_TK')
nucleardatapy_tk = os.path.dirname(os.path.abspath(__file__))
# print('nseospy_path:',nseospy_path)
#
# where data/ are stored
#
path_data = os.path.join(nucleardatapy_tk, "data/")
#
# where AME/ is stored
#
path_ame = os.path.join(path_data, "AME/")
#
col = [
    "blue",
    "orange",
    "green",
    "red",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "cyan",
    "black",
    "magenta",
    "yellow",
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]
# colors = [ "r", "b", "g", "k", "purple", "m", "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf", "orange", "y" ]
#
elements = np.array(
    [
        "H",
        "He",
        "Li",
        "Be",
        "B",
        "C",
        "N",
        "O",
        "F",
        "Ne",
        "Na",
        "Mg",
        "Al",
        "Si",
        "P",
        "S",
        "Cl",
        "Ar",
        "K",
        "Ca",
        "Sc",
        "Ti",
        "V",
        "Cr",
        "Mn",
        "Fe",
        "Co",
        "Ni",
        "Cu",
        "Zn",
        "Ga",
        "Ge",
        "As",
        "Se",
        "Br",
        "Kr",
        "Rb",
        "Sr",
        "Y",
        "Zr",
        "Nb",
        "Mo",
        "Tc",
        "Ru",
        "Rh",
        "Pd",
        "Ag",
        "Cd",
        "In",
        "Sn",
        "Sb",
        "Te",
        "I",
        "Xe",
        "Cs",
        "Ba",
        "La",
        "Ce",
        "Pr",
        "Nd",
        "Pm",
        "Sm",
        "Eu",
        "Gd",
        "Tb",
        "Dy",
        "Ho",
        "Er",
        "Tm",
        "Yb",
        "Lu",
        "Hf",
        "Ta",
        "W",
        "Re",
        "Os",
        "Ir",
        "Pt",
        "Au",
        "Hg",
        "Tl",
        "Pb",
        "Bi",
        "Po",
        "At",
        "Rn",
        "Fr",
        "Ra",
        "Ac",
        "Th",
        "Pa",
        "U",
        "Np",
        "Pu",
        "Am",
        "Cm",
        "Bk",
        "Cf",
        "Es",
        "Fm",
        "Md",
        "No",
        "Lr",
        "Rf",
        "Db",
        "Sg",
        "Bh",
        "Hs",
        "Mt",
        "Ds",
        "Rg",
        "Cn",
        "Nh",
        "Fl",
        "Mc",
        "Lv",
        "Ts",
        "Og",
    ]
)


#
def tex2str(ele):
    """
	Transform an element in variable `ele` written in one of the following latex forms: 
	$5.6$, ${5.6}$, \
	$8.76\\pm1.82$, ${8.76}\\pm{1.82}$, \
	${21.35}^{+0.37}_{-0.26}$, $21.35^{+0.37}_{-0.26}$, \
	${21.35}_{-0.26}^{+0.37}$, $21.35_{-0.26}^{+0.37}$.

	into `str` or `None` if not in these formats.

    :return: cent, errp, errm.
    :rtype: str.
	"""
    ele = ele.strip()
    if "$" in ele:
        # print('ele:',ele)
        # print('ele [2:-2]:',ele[2:-2])
        # ele1 = ele.strip('$')[1]
        # ele1 = ele[2:-2]
        ele1 = ele.strip("$")
        # print('ele1:',ele1)
        if "\\pm" in ele1:
            ele2 = ele1.split("\\pm")
            cent = ele2[0]
            errp = ele2[1]
            errm = errp
        elif "^" in ele1:
            ele2 = ele1.split("^")
            if "_" in ele2[0]:
                ele3 = ele2[0].split("_")
                errp = ele2[1]
                cent = ele3[0]
                errm = ele3[1]
            elif "_" in ele2[1]:
                ele3 = ele2[1].split("_")
                cent = ele2[0]
                errp = ele3[0]
                errm = ele3[1]
            else:
                print("The variable ele in not in the expected format (1)")
                print("ele:", ele)
                print("Exit()")
                exit()
        elif "-" in ele1:
            cent = None
            errp = None
            errm = None
        else:
            cent = ele1
            errp = str(0.0)
            errm = errp
            # if isinstance(ele1, float):
            # print('The variable ele in not in the expected format (2)')
            # print('ele:',ele)
            # print('ele1:',ele1)
            # print('Exit()')
            # exit()
        if cent is not None and "{" in cent:
            cent = cent.split("{")[1]
        if cent is not None and "}" in cent:
            cent = cent.split("}")[0]
        if errp is not None and "{" in errp:
            errp = errp.split("{")[1]
        if errp is not None and "}" in errp:
            errp = errp.split("}")[0]
        if errm is not None and "{" in errm:
            errm = errm.split("{")[1]
        if errm is not None and "}" in errm:
            errm = errm.split("}")[0]
        if errp is not None:
            errp = str(abs(float(errp)))
        if errm is not None:
            errm = str(abs(float(errm)))
    else:
        cent = None
        errp = None
        errm = None
    #
    return cent, errp, errm
