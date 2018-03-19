import sys
sys.path.append("../circos_report/snv_cnv_anno2conf")
from snv_cnv_proconf_cmd import main_snv_cnv


params = {"plotinfo":         
            {"karytotype": "data/karyotype.human.hg19.txt", 
            "chrom_unit": 1000000, 
            "species": "data/hs_circos.txt"}, 
        "circos_snv_cnv_tmp": "data/circos_snv_cnv_template.md", 
        "snvinp": "data/test.mutect2_snv.anno.txt", 
        "prefix": "patient1", 
        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
        "circos_report_template": "data/circos_report_template.md"
            }

def test_main_snv_cnv():

    main_snv_cnv(params)

if __name__ == "__main__":

    test_main_snv_cnv()
