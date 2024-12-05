# This file creates all of the gridpacks, then sends them over the the myFiles
# directory on EOS
# Name of the process:

base_dir=/afs/cern.ch/user/e/ecurtis/idmStudyImperial/MCproduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths/mH$(mH)
process_name=h2h2lPlMnunu

Executable = getWidths.py

# have to do logging on afs
home=/afs/cern.ch/user/e/ecurtis/idmStudyImperial
output = $(home)/logging/getWidths_mH$(mH)_mA$(mA)_mHch$(mHch).out
error = $(home)/logging/getWidths_mH$(mH)_mA$(mA)_mHch$(mHch).err
log = $(home)/logging/getWidths_mH$(mH)_mA$(mA)_mHch$(mHch).log

set_file=$(base_dir)/$(process_name)/$(process_name)_mH$(mH)_mA$(mA)_mHch$(mHch)/$(process_name)_mH$(mH)_mA$(mA)_mHch$(mHch)_customizecards.dat
MG_tar_file=/afs/cern.ch/user/e/ecurtis/idmStudyImperial/BPs/MG5_aMC_v2_6_7_forCondor.tar.gz

arguments = $(mH) $(mA) $(mHch) $(process_name) $(base_dir)

Transfer_Input_Files= $(MG_tar_file),$(set_file)
should_transfer_files=YES
when_to_transfer_output=ON_EXIT
Transfer_Output_Files=""
Universe = vanilla
Initialdir = .
getenv=False
+MaxRuntime=7200
RequestCpus = 1

#! Change this below to loop over the correct directory!!!!
queue mH, mA, mHch from mH80/input_arguments.txt
