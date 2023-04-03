import sys
inFile = sys.argv[1]
with open(inFile, 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if 'SoftQCD:double' in line:
            lines[i] = lines[i].replace("),",",")
            if "down" in inFile.lower():
                lines[i] = lines[i].strip() + '\n' + \
                "            'Tune:pp 14',\n" + \
                "            'Tune:ee 7',\n" + \
                "            'MultipartonInteractions:ecmPow=0.25208',\n" + \
                "            'SpaceShower:alphaSvalue=0.1108',\n" + \
                "            'PDF:pSet=LHAPDF6:NNPDF30_lo_as_0130',\n" + \
                "            'MultipartonInteractions:pT0Ref=2.268694e+00',\n" + \
                "            'MultipartonInteractions:expPow=1.561995e+00',\n" + \
                "            'ColourReconnection:range=8.714042e+00'),\n\n"
            if "up" in inFile.lower():
                lines[i] = lines[i].strip() + '\n' + \
                "            'Tune:pp 14',\n" + \
                "            'Tune:ee 7',\n" + \
                "            'MultipartonInteractions:ecmPow=0.25208',\n" + \
                "            'SpaceShower:alphaSvalue=0.1108',\n" + \
                "            'PDF:pSet=LHAPDF6:NNPDF30_lo_as_0130',\n" + \
                "            'MultipartonInteractions:pT0Ref=2.127913e+00',\n" + \
                "            'MultipartonInteractions:expPow=1.710694e+00',\n" + \
                "            'ColourReconnection:range=6.500048e+00'),\n\n"
    f.seek(0)
    for line in lines:
        f.write(line)
