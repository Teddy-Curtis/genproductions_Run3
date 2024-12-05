# This file creates all of the gridpacks, then sends them over the the myFiles
# directory on EOS
# Name of the process:
tag = idm_dilepton
outputname = idm_dilepton_vary_mHch_13p6

# These define the arguments for input
scram_version=el8_amd64_gcc10
CMSSW_version=CMSSW_12_4_8
run_name=$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)
run_folder=cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_varyMHch/cards/mH$(mH)/$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)


Executable = gridpack_generation.sh

# have to do logging on afs
home=/afs/cern.ch/user/e/ecurtis/idmStudyImperial
output = $(home)/logging/13p6_genprod_vary_mHch_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch).out
error = $(home)/logging/13p6_genprod_vary_mHch_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch).err
log = $(home)/logging/13p6_genprod_vary_mHch_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch).log


arguments = $(run_name) $(run_folder) local ALL $(scram_version) $(CMSSW_version) $(outputname)

Transfer_Input_Files = /afs/cern.ch/user/e/ecurtis/idmStudyImperial/MCproduction/newGenproductions
#Transfer_Input_Files = /afs/cern.ch/user/e/ecurtis/idmStudyImperial/MCproduction/genproductions_compressed.tar.gz
should_transfer_files = YES
when_to_transfer_output = ON_EXIT
Transfer_Output_Files = ""
Universe = vanilla
Initialdir = .
getenv = False
#+MaxRuntime=14400
+JobFlavour = "nextweek"
#+JobFlavour = "testmatch"
RequestCpus = 8

JobBatchName = create_gridpacks_$(output_name)

queue mH, mA, mHch from cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_varyMHch/cards/input_arguments.txt

