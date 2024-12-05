#!/bin/bash

mH=80
mA=150
tag=idm_dilepton
outputname=idm_dilepton_13p6_parameterscan_updatedWidths_CMSSW_12_4_8

scram_version=el8_amd64_gcc10
CMSSW_version=CMSSW_12_4_8
run_name=${tag}_mH${mH}_mA${mA}
run_folder=cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu/cards/13p6/mH${mH}/${tag}_mH${mH}_mA${mA}


./gridpack_generation.sh ${run_name} ${run_folder} local ALL # ${scram_version} ${CMSSW_version} ${outputname}