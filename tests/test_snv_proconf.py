import sys
sys.path.append("../circos_report/snv_anno2conf")
from snv_proconf_cmd import main_snv

params = {"snvinp": "data/test.mutect2_snv.anno.txt", "prefix": "patient1", "plotinfo": {"chrom_unit": 1000000, "species": "data/hs_circos.txt", "karytotype": "data/karyotype.human.hg19.txt"}, "circos_report_template": "data/circos_report_template.md", "circos_snv_tmp": "data/circos_snv_template.md"}


def test_main_snp():

    main_snv(params)

if __name__ == "__main__":

    test_main_snp()
