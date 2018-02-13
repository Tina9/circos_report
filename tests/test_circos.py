import sys,os
sys.path.append("../")

from circos_report.reporter.circos import circos

kind = "data/circos.snv.conf" 

def test_circos():

    circos(kind)


if __name__ == "__main__":

    test_circos()
