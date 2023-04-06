import sys
inFile = sys.argv[1]
inRivet = sys.argv[2]
outyoda = sys.argv[3]
with open(inFile, 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "comEnergy" in line:
            lines[i] = lines[i].replace("7000","13000")
        if "from Configuration.GenProduction.rivet_customize import customise" in line:
            lines[i] = lines[i].replace("from","#from")
        if "process" in line and "customise(process)" in line:
            lines[i] = lines[i].replace("process =","#process =")
        if line.startswith('process.source'):
            lines[i] = lines[i].strip() + '\n\n' + \
                  "from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper" + '\n' + \
                  "randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)" + '\n' + \
                  "randSvc.populate()" + '\n'
    f.seek(0)
    for line in lines:
        f.write(line)

with open(inFile, 'w') as f:
    for line in lines:
        if "GeneratorInterface.RivetInterface.rivetAnalyzer_cfi" not in line and "process.rivetAnalyzer.AnalysisNames" not in line and "process.rivetAnalyzer.OutputFile" not in line and "process.generation_step+=process.rivetAnalyzer" not in line and "process.schedule.remove(process.RAWSIMoutput_step" not in line:
            f.write(line)

with open(inFile, 'a+') as f:
    f.writelines([
        "process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')\n"
        "process.rivetAnalyzer.AnalysisNames = cms.vstring('"+inRivet+"')\n"
        "process.rivetAnalyzer.OutputFile = cms.string('"+outyoda+"')\n"
        "process.generation_step+=process.rivetAnalyzer\n"
        "process.schedule.remove(process.RAWSIMoutput_step)\n"
    ])
