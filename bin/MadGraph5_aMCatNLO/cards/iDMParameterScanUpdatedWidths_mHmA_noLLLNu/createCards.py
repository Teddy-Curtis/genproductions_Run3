import os
import numpy as np
import sys

run_prefix = 'idm_dilepton'

# define the mass splittings
mHs = list(np.arange(60, 190, 10))
mAs = list(np.arange(60, 500, 10))
mHch = 300
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
    run_name = f'{run_prefix}_mH{mH}_mA{mA}'
    run_directory = f"{base_dir}/mH{mH}/{run_name}"



    os.makedirs(run_directory, exist_ok=True)



    for template_filename in files:
        file = readFile(template_filename)

        file = replaceInFile(file, run_name, mH, mA, mHch)

        filename = f'{run_name}{template_filename}'
        file_dir = f'{run_directory}/{filename}'
        saveFile(file, file_dir)
    
    
    with open(f"{base_dir}/input_arguments.txt", "a") as f:
        f.write(f"{mH}, {mA}\n")


for mH in mHs:
    for mA in mAs:
        if not ((mH < mA) & (mA - mH >= 20) & (mA - mH <= 100)):
            continue

        print(f"{mH}, {mA}")
        continue




# Now add in the specific points

# also add the mass splitting of 92
mHs_92 = list(np.arange(60, 190, 10))
deltaAH = 92
mHch = 300

for mH in mHs_92:
    mA = mH + deltaAH
    if not ((mH < mA) & (mA - mH >= 20) & (mA - mH <= 100)):
        continue
    print(f"{mH}, {mA}")

# Also add the validation points
mHs_val = [85, 85, 115, 135, 165, 165]
mAs_val = [120, 170, 180, 190, 200, 250]
for mH, mA in zip(mHs_val, mAs_val):
    mHs.append(mH)
    mAs.append(mA)

for mH, mA in zip(mHs_val, mAs_val):
    if not ((mH < mA) & (mA - mH >= 20) & (mA - mH <= 100)):
        print(f"Didnt work for {mH}, {mA}")
        continue
    print(mH, mA)
    makeFiles(mH, mA, mHch, run_prefix, base_dir, files)

   
