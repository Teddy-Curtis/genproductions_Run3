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

def replaceInFile(file, run_name, mH, mA, mHch):
    file = file.replace("<RUN_NAME>", run_name)
    file = file.replace("<MH2>", str(mH))
    file = file.replace("<MH3>", str(mA))
    file = file.replace("<MHPM>", str(mHch))
    file = file.replace("<LAM2>", str(0.0))
    file = file.replace("<LAML>", str(0.0000000000001))
    return file

def readFile(filename):
    with open(filename, 'r') as f:
        file = f.read()
    return file

def saveFile(file, filename):
    with open(filename, 'w') as f:
        f.write(file)


def makeFiles(mH, mA, mHch, run_prefix, base_dir, files):
    run_name = f'{run_prefix}_mH{mH}_mA{mA}_mHch{mHch}'
    run_directory = f"{base_dir}/mH{mH}/{run_name}"



    os.makedirs(run_directory, exist_ok=True)



    for template_filename in files:
        file = readFile(template_filename)

        file = replaceInFile(file, run_name, mH, mA, mHch)

        filename = f'{run_name}{template_filename}'
        file_dir = f'{run_directory}/{filename}'
        saveFile(file, file_dir)
    
    
    with open(f"{base_dir}/input_arguments.txt", "a") as f:
        f.write(f"{mH}, {mA}, {mHch}\n")



def getMaxMHch(mH, mA):
    diff = mA - mH
    if (diff)<20:
        return mA+60
    elif (diff)<50:
        return mA+50
    elif (diff)<80:
        return mA+40
    elif (diff)<120:
        return mA+30
    else:
        raise ValueError("Invalid mass difference")


# define the mass splittings
masses = [
    [70, 98],
    [80, 114],
    [90, 130],
    [100, 146],
    [110, 166]
]

masses_to_run_over = []

for mH, mA in masses:
    for mHch in [mA + 1, getMaxMHch(mH, mA)]:
        masses_to_run_over.append([mH, mA, mHch])
        

print(masses_to_run_over)

# Now add in the specific points
for mH, mA, mHch in masses_to_run_over:
    makeFiles(mH, mA, mHch, run_prefix, base_dir, files)