import sys,os
sys.path.append("../")
import json
from circos_report.filing.sv_filing import sv_filing

svinp = "data/22.tumor.ready.mergeavi.anno.txt"
prefix = "22.tumor.ready"

def test_sv_filing():

    sv_filing(svinp, prefix)


if __name__ == "__main__":

    test_sv_filing()
