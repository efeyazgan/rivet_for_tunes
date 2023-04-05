# Rivet Instructions for running on basic tunes
```
cmsrel CMSSW_11_2_4
cd CMSSW_11_2_4/src
cmsenv

git cms-merge-topic mseidel42:RivetPaths_11_2

git-cms-init
git-cms-addpkg GeneratorInterface/RivetInterface
git-cms-addpkg Configuration/Generator

git clone https://:@gitlab.cern.ch:8443/cms-gen/Rivet.git
cd Rivet
git remote add cms-gen ssh://git@gitlab.cern.ch:7999/cms-gen/Rivet.git
git pull cms-gen master

source rivetSetup.sh
#scram b -j8

cd ..
git clone https://github.com/efeyazgan/rivet_for_tunes.git

curl -s https://raw.githubusercontent.com/cms-sw/genproductions/master/genfragments/ThirteenTeV/MinBias_TuneCP5_13TeV_pythia8_cff.py -o Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5_13TeV_pythia8_cff.py --create-dirs
curl -s https://raw.githubusercontent.com/cms-sw/genproductions/UL2019/python/rivet_customize.py -o Configuration/GenProduction/python/rivet_customize.py
curl -s https://raw.githubusercontent.com/cms-sw/cmssw/master/Configuration/Generator/python/MinBias_13TeV_pythia8_TuneCUETP8M1_cfi.py -o Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py --create-dirs
curl -s https://raw.githubusercontent.com/cms-sw/genproductions/master/genfragments/SevenTeV/MinBias_TuneZ2star_7TeV_pythia6_cff.py -o Configuration/GenProduction/python/SevenTeV/MinBias_TuneZ2star_7TeV_pythia6_cff.py --create-dirs
curl -s https://raw.githubusercontent.com/cms-sw/genproductions/master/genfragments/SevenTeV/MinBias_Tune4C_7TeV_pythia8_cff.py -o Configuration/GenProduction/python/SevenTeV/MinBias_Tune4C_7TeV_pythia8_cff.py --create-dirs
curl -s https://raw.githubusercontent.com/cms-sw/cmssw/master/Configuration/Generator/python/PythiaUEP11Settings_cfi.py -o Configuration/GenProduction/python/SevenTeV/PythiaUEP11Settings_cfi.py --create-dirs 
curl -s https://raw.githubusercontent.com/cms-sw/cmssw/master/Configuration/Generator/python/PythiaUEP11mpiHiSettings_cfi.py -o Configuration/GenProduction/python/SevenTeV/PythiaUEP11mpiHiSettings_cfi.py --create-dirs
```
For CP5:
```
cp Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5_13TeV_pythia8_cff.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneUp_13TeV_pythia8_cff.py
cp Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5_13TeV_pythia8_cff.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneDown_13TeV_pythia8_cff.py
sed -i 's/CP5/CP5TuneUp/g' Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneUp_13TeV_pythia8_cff.py
sed -i 's/CP5/CP5TuneDown/g' Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneDown_13TeV_pythia8_cff.py
```
For CUETP8M2T4:
```
sed -i 's/CUEP8M1/CUEP8M2T4/g' Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py
sed -i 's/Pythia8ConcurrentGeneratorFilter/Pythia8GeneratorFilter/g' Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py
cp Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneUp_13TeV_pythia8_cff.py
cp Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneDown_13TeV_pythia8_cff.py
python rivet_for_tunes/append_cuetp8m2t4updown.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneUp_13TeV_pythia8_cff.py
python rivet_for_tunes/append_cuetp8m2t4updown.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneDown_13TeV_pythia8_cff.py
```

P11 requires the minbias parameters from Z2* to be added. i.e. 
```
cat rivet_for_tunes/p11_add_minbias_cfg.txt >> Configuration/GenProduction/python/SevenTeV/PythiaUEP11Settings_cfi.py
cat rivet_for_tunes/p11_add_minbias_cfg.txt >> Configuration/GenProduction/python/SevenTeV/PythiaUEP11mpiHiSettings_cfi.py
```

Compile:
```
scram b -j8
```

```
#CP5
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CP5_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#CP5TuneUp
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneUp_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CP5TuneUp_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#CP5TuneDown
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCP5TuneDown_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CP5TuneDown_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#CUETP8M2T4:
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CUETP8M2T4_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#CUETP8M2T4 Tune Down:
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneDown_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CUETP8M2T4_TuneDown_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#CUETP8M2T4 Tune Up:
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/MinBias_TuneCUEP8M2T4_TuneDown_13TeV_pythia8_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_CUETP8M2T4_TuneUp_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#Z2*:
cmsDriver.py Configuration/GenProduction/python/SevenTeV/MinBias_TuneZ2star_7TeV_pythia6_cff.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_TuneZ2star_7TeV_pythia6_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#p11:
mv Configuration/GenProduction/python/SevenTeV/PythiaUEP11Settings_cfi.py Configuration/GenProduction/python/SevenTeV/MinBias_P11_7TeV_pythia6_cfi.py
cmsDriver.py Configuration/GenProduction/python/SevenTeV/MinBias_P11_7TeV_pythia6_cfi.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_TuneP11_7TeV_pythia6_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
#p11mpiHi:  
mv Configuration/GenProduction/python/SevenTeV/PythiaUEP11mpiHiSettings_cfi.py Configuration/GenProduction/python/SevenTeV/MinBias_P11mpiHi_7TeV_pythia6_cfi.py
cmsDriver.py Configuration/GenProduction/python/SevenTeV/MinBias_P11_7TeV_pythia6_cfi.py -s GEN --datatier=GEN-SIM-RAW --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=rivet_TuneP11mpiHi_7TeV_pythia6_cfg.py --customise=Configuration/GenProduction/rivet_customize.py
```
Change the comenergy to 13 TeV, add the random number stuff, rivet routine and output filename:
```
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CP5_cfg.py CMS_2015_I1384119 CP5_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CP5TuneUp_cfg.py CMS_2015_I1384119 CP5TuneUp_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CP5TuneDown_cfg.py CMS_2015_I1384119 CP5TuneDown_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CUETP8M2T4_cfg.py CMS_2015_I1384119 CUETP8M2T4_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CUETP8M2T4_TuneDown_cfg.py CMS_2015_I1384119 CUETP8M2T4_TuneDown_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_CUETP8M2T4_TuneUp_cfg.py CMS_2015_I1384119 CUETP8M2T4_TuneUp_13TeV_pythia8.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_TuneZ2star_7TeV_pythia6_cfg.py CMS_2015_I1384119 TuneZ2star_13TeV_pythia6.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_TuneP11_7TeV_pythia6_cfg.py CMS_2015_I1384119 TuneP11_13TeV_pythia6.yoda
python rivet_for_tunes/append_rivet_routine_and_output_yoda.py rivet_TuneP11mpiHi_7TeV_pythia6_cfg.py CMS_2015_I1384119 TuneP11mpiHi_13TeV_pythia6.yoda
```

Run the rivet routines:
```
cmsRun rivet_CP5_cfg.py
cmsRun rivet_CP5TuneUp_cfg.py
cmsRun rivet_CP5TuneDown_cfg.py
cmsRun rivet_CUETP8M2T4_cfg.py
cmsRun rivet_CUETP8M2T4_TuneDown_cfg.py
cmsRun rivet_CUETP8M2T4_TuneUp_cfg.py
cmsRun rivet_TuneZ2star_7TeV_pythia6_cfg.py
cmsRun rivet_TuneP11_7TeV_pythia6_cfg.py
cmsRun rivet_TuneP11mpiHi_7TeV_pythia6_cfg.py
```

Make an envelope from the tune variations
```
python2 Rivet/scripts/yodacombine -o CP5_13TeV_pythia8_unc.yoda eigentunes CP5_13TeV_pythia8.yoda CP5TuneUp_13TeV_pythia8.yoda CP5TuneDown_13TeV_pythia8.yoda
python2 Rivet/scripts/yodacombine -o CUETP8M2T4_13TeV_pythia8_unc.yoda eigentunes CUETP8M2T4_13TeV_pythia8.yoda 
python2 Rivet/scripts/yodacombine -o TuneP11_13TeV_pythia6_unc.yoda eigentunes TuneP11_13TeV_pythia6.yoda TuneP11mpiHi_13TeV_pythia6.yoda
```

Make the plots and dump in a webpage:
```
rivet-mkhtml -c rivet_for_tunes/plots.plot --mc-errs CP5_13TeV_pythia8_unc.yoda:Title="13 TeV CP5 pythia8":PolyMarker="triangle":DotScale=1.5  CUETP8M2T4_13TeV_pythia8_unc.yoda:Title="13 TeV CUETP8M2T4":PolyMarker="diamond":DotScale=1.5  TuneZ2star_13TeV_pythia6.yoda:Title="13 TeV Z2* pythia6":PolyMarker="o":DotScale=1.5 TuneP11_13TeV_pythia6_unc.yoda:Title="13 TeV P11 pythia6":PolyMarker="*":DotScale=1.5 -o /eos/user/e/efe/www/CMS_2015_I1384119
```
where
plots.plot is
```
# BEGIN PLOT /CMS_2016_I1491950/*
#XMin=1.0
#XMax=2.0
XTwosidedTicks=1
YTwosidedTicks=1
LogY=0
LegendXPos=0.25
RatioPlotErrorBandColor=grey!40!yellow!60
ConnectBins=0
RatioPlot=1
Legend=1
#LegendYPos=0.75
# END PLOT
```

See https://gitlab.com/hepcedar/rivet/-/blob/master/doc/tutorials/makeplots.md for plotting options. 


https://efe.web.cern.ch/efe/CP5_vs_Z2star/CMS_2015_I1384119/index.html 

Rivet routines to be used (incomplete list):
----
CMS\_2015\_PAS\_FSQ\_15_007
CMS\_2015\_I1384119
https://gitlab.cern.ch/cms-gen/Rivet/-/merge_requests/89
/eos/user/e/efe/DPSUncertainty/yodafiles/TTTo1L\_pythia8\_test.txt.yoda
