import sys
sys.path.append("../")
from circos_report.filing.snv_filing import snv_filing 

snvinput = "data/patient1.mutect2_snv.anno.tsv"
prefix = "22.tumor.ready"

def test_snvfiling():

	snv_filing(snvinput, prefix)

if __name__ == "__main__":

	test_snvfilin()

