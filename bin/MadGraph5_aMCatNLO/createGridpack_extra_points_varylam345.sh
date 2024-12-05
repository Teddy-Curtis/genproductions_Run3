# This file creates all of the gridpacks, then sends them over the the myFiles
# directory on EOS
# Name of the process:
tag = idm_dilepton
outputname = idm_dilepton_vary_lam345_13p6

# These define the arguments for input
scram_version=el8_amd64_gcc10
CMSSW_version=CMSSW_12_4_8
run_name=$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)_lam$(lam345)
run_folder=cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_biggerLam345/cards/mH$(mH)/$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)_lam$(lam345)


Executable = gridpack_generation.sh

# have to do logging on afs
home=/afs/cern.ch/user/e/ecurtis/idmStudyImperial
output = $(home)/logging/13p6_genprod_vary_lam345_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)_lam$(lam345).out
error = $(home)/logging/13p6_genprod_vary_lam345_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)_lam$(lam345).err
log = $(home)/logging/13p6_genprod_vary_lam345_$(tag)_mH$(mH)_mA$(mA)_mHch$(mHch)_lam$(lam345).log


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

queue mH, mA, mHch, lam345 from cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_biggerLam345/cards/test_arguments.txt

