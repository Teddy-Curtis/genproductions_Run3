#!/bin/bash


mH=$1
mA=$2
mHch=$3
process=$4
direc=$5
echo "process = "
echo $process
eval "$(micromamba shell hook --shell bash)"
micromamba activate higgs-dna-all
cd /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_varyMHch

python getWidths.py $mH $mA $mHch $process $direc 