import sys
sys.path.append("../circos_report/cnv_anno2conf")
from cnv_proconf_cmd import main_cnv


params = {"plotinfo": {"karytotype": "data/karyotype.human.hg19.txt", "chrom_unit": 1000000, "species": "data/hs_circos.txt"}, "circos_report_template": "data/circos_report_template.md", "prefix": "patient1", "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt", "circos_cnv_tmp": "data/circos_cnv_template.md"}

def test_main_cnv():
    main_cnv(params)

if __name__ == "__main__":
    test_main_cnv()

