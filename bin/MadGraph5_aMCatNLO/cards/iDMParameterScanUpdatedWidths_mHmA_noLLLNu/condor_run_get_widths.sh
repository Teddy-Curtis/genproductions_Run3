#!/bin/bash


mH=$1
mA=$2
process=$3
direc=$4
echo "process = "
echo $process
eval "$(micromamba shell hook --shell bash)"
micromamba activate higgs-dna-all
cd /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu

python getWidths.py $mH $mA $process $direc 