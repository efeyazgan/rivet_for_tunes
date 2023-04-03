import sys
inFile = sys.argv[1]
with open(inFile, 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "comEnergy" in line:
            line = line.replace("7000","13000")
        if line.startswith('process.source'):
            lines[i] = lines[i].strip() + '\n\n' + \
                  "from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper" + '\n' + \
                  "randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)" + '\n' + \
                  "randSvc.populate()" + '\n'
    f.seek(0)
    for line in lines:
        f.write(line)
