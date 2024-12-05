import os
import numpy as np
import sys

run_prefix = 'idm_dilepton'

base_dir = "cards"


# Check if directory already exists as we don't want to overwrite them 
# if the decays have already been found! 
if os.path.exists(f"{base_dir}"):
    print(f"Directory already exists, exiting so that it doesn't overwrite the decays that have been found!")
    sys.exit(0)
else:    
    os.makedirs(base_dir, exist_ok = True)






files = ['_proc_card.dat', '_run_card.dat', '_customizecards.dat', '_extramodels.dat']

def replaceInFile(file, run_name, mH, mA, mHch, lam345):
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(mHch))
    file = file.replace("<LAM2>", str(0.0))
    file = file.replace("<LAML>", str(lam345))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)


def makeFiles(mH, mA, mHch, lam345, run_prefix, base_dir, files):
    run_name = f'{run_prefix}_mH{mH}_mA{mA}_mHch{mHch}_lam{lam345}'
    run_directory = f"{base_dir}/mH{mH}/{run_name}"



    os.makedirs(run_directory, exist_ok=True)



    for template_filename in files:
        file = readFile(template_filename)

        file = replaceInFile(file, run_name, mH, mA, mHch, lam345)

        filename = f'{run_name}{template_filename}'
        file_dir = f'{run_directory}/{filename}'
        saveFile(file, file_dir)
    
    
    with open(f"{base_dir}/input_arguments.txt", "a") as f:
        f.write(f"{mH}, {mA}, {mHch}, {lam345}\n")


def getLam(mH):
    lam = (0.05 / 28) * (mH - 72)

    return np.round(lam, 4)


mHch = 300
masses = [
    [70, 98],
    [80, 114],
    [90, 130],
    [100, 146],
    [110, 166]
]

param_points = []

for mH, mA in masses:
    param_points.append([mH, mA, mHch, getLam(mH)])
    param_points.append([mH, mA, mHch, 8])

for mH, mA, mHch, lam345 in param_points:
    makeFiles(mH, mA, mHch, lam345, run_prefix, base_dir, files)
