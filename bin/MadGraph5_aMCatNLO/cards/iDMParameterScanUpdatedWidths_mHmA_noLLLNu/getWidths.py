####  !/afs/cern.ch/user/e/ecurtis/miniconda3/envs/idm/bin/python
import subprocess
import sys
import os

mH, mA, process, base_dir = sys.argv[1], sys.argv[2], str(sys.argv[3]), str(sys.argv[4])
print(f"mH = {mH}, mA = {mA}")
print(f"Process = {process}")
print(f"Base directory = {base_dir}")


os.makedirs(f"tmp/base_{process}_mH{mH}_mA{mA}", exist_ok=True)
os.chdir(f"tmp/base_{process}_mH{mH}_mA{mA}")

# MadGraph dirdctory
MG_dir = "/vols/cms/emc21/idmStudy/BPs/MG5_aMC_v2_9_19"


def getXS(particle):
    with open(f'cross_section_{particle}.txt', 'r') as f:
        xs_file = f.readlines()
    for line in xs_file:
        if line.startswith("run_01"):
            decay = float(line.split(" ")[2])
    return decay

custom_card_loc = f"{base_dir}/{process}_mH{mH}_mA{mA}/{process}_mH{mH}_mA{mA}_customizecards.dat"

# First I need to read in the set commands
with open(custom_card_loc, 'r') as f:
    set_commands = f.read()
print(set_commands)

################################### h3 Width ########################################
# The first thing I want to do is code to create the MG txt script 
with open(f'find_h3_decay_{process}_mH{mH}_mA{mH}.txt', 'w') as f:
    f.write('import model InertDoublet_UFO\n')
    f.write('generate h3 > h2 all all\n')
    f.write(f'output {process}_mH{mH}_mA{mH}_h3Width\n')
    f.write(f'launch {process}_mH{mH}_mA{mH}_h3Width\n')
    # for line in set_commands:
    #     f.write(line)
    f.write(set_commands)
    f.write(f'launch {process}_mH{mH}_mA{mH}_h3Width -i\n')
    f.write('print_results --path=./cross_section_h3.txt --format=short\n')

# Now run this
cmd = f"python {MG_dir}/bin/mg5_aMC find_h3_decay_{process}_mH{mH}_mA{mH}.txt"
status, out = subprocess.getstatusoutput(cmd)
print(out)

# Now that I have the h3 decay, I can update the set commands
# First read what the xs is
h3_decay = getXS("h3")
print(f"h3 h3_decay = {h3_decay}")



################################### h+ Width ########################################
# Now repeat but for h+
# The first thing I want to do is code to create the MG txt script 
with open(f'find_hch_decay_{process}_mH{mH}_mA{mH}.txt', 'w') as f:
    f.write('import model InertDoublet_UFO\n')
    f.write('generate h+ > h2 all all\n')
    f.write(f'output {process}_mH{mH}_mA{mA}_hchWidth\n')
    f.write(f'launch {process}_mH{mH}_mA{mA}_hchWidth\n')
    # for line in set_commands:
    #     f.write(line)
    f.write(set_commands)
    f.write(f'launch {process}_mH{mH}_mA{mA}_hchWidth -i\n')
    f.write('print_results --path=./cross_section_hch.txt --format=short\n')

# Now run this
cmd = f"python {MG_dir}/bin/mg5_aMC find_hch_decay_{process}_mH{mH}_mA{mH}.txt"
status, out = subprocess.getstatusoutput(cmd)
print(out)


hch_decay = getXS("hch")
print(f"hch hch_decay = {hch_decay}")






################################### Update Widths ########################################
# Now replace and update the set commands
set_commands = set_commands.replace("set param_card DECAY 36 1.0000", f"set param_card DECAY 36 {h3_decay}")
set_commands = set_commands.replace("set param_card DECAY 37 1.0000", f"set param_card DECAY 37 {hch_decay}")


# Now overwrite the set commands
with open(f'{base_dir}/{process}_mH{mH}_mA{mA}/{process}_mH{mH}_mA{mA}_customizecards.dat', 'w') as f:
    f.write(set_commands)


# Now I copy it back to afs 
# cmd = f"cp -f {process}_mH{mH}_mA{mA}_customizecards.dat {base_dir}/{process}_mH{mH}_mA{mA}/{process}_mH{mH}_mA{mA}_customizecards.dat"
# status, out = subprocess.getstatusoutput(cmd)