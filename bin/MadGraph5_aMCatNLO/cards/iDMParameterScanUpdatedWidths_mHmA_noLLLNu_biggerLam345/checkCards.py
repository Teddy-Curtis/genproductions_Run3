import glob
mH = 80
process = "idm_all_procs"


files = glob.glob(f"cards/13p6/*/*/*cards.dat")

print(files)

for file in files:
    mass_point = file.split("/")[-2]
    with open(file, "r") as f:
        info = f.read()
        
    #print(info)
    if "1.00" in info:

        print(f"Cards failed for: {mass_point}")