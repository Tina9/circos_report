import sys,os
sys.path.append("../")
import json

cnvinp = "data/22.tumor.ready.cnv.info.anno.txt"
prefix = "22.tumor.ready"

from circos_report.filing.cnv_filing import cnv_filing

def test_cnv_filing():

	cnv_filing(cnvinp, prefix)


if __name__ == "__main__":

	test_cnv_filing()
