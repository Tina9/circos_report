import sys
sys.path.append("../circos_report/multi_anno2conf")
from multi_proconf_cmd import main_multi

params = {"snvinp": "data/test.mutect2_snv.anno.txt", 
            "plotinfo": {
                "chrom_unit": 1000000, 
                "species": "data/hs_circos.txt", 
                "karytotype": "data/karyotype.human.hg19.txt", 
                }, 
        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
        "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
        "circos_report_template": "data/circos_report_template.md", 
        "circos_multi_tmp": "data/circos_multi_template.md",
        "prefix": "patient1"}

def test_main_multi():

    main_multi(params)

if __name__ == "__main__":

    test_main_multi()
