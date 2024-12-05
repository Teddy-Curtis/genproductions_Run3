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
# cd /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/FCC_newRun_all/e365
custom_card_loc="${direc}/${process}_mH${mH}_mA${mA}_mHch${mHch}/${process}_mH${mH}_mA${mA}_mHch${mHch}_customizecards.dat"


cd $_CONDOR_SCRATCH_DIR

echo "pwd:"
pwd

cp /vols/cms/emc21/idmStudy/MCproduction/gridpackProduction/genproductions/bin/MadGraph5_aMCatNLO/cards/iDMParameterScanUpdatedWidths_mHmA_noLLLNu_varyMHch/getWidths_otherWay.py . 
cp $custom_card_loc .
mv ${process}_mH${mH}_mA${mA}_mHch${mHch}_customizecards.dat customizecards.dat

BASE=`pwd`

ls
pwd

python getWidths_otherWay.py $mH $mA $mHch $process $BASE

cd $BASE
ls
cp new_customizecards.dat "${direc}/${process}_mH${mH}_mA${mA}_mHch${mHch}/${process}_mH${mH}_mA${mA}_mHch${mHch}_customizecards.dat"