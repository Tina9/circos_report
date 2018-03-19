import sys
sys.path.append("../circos_report/cnv_sv_anno2conf")
from cnv_sv_proconf_cmd import main_cnv_sv

params = {"plotinfo":
            {"karytotype": "data/karyotype.human.hg19.txt",
            "chrom_unit": 1000000,
            "species": "data/hs_circos.txt",
            },
        "circos_cnv_sv_tmp": "data/circos_cnv_sv_template.md",
        "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
        "prefix": "patient1",
        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
        "circos_report_template": "data/circos_report_template.md"
         }

def test_main_cnv_sv():

    main_cnv_sv(params)

if __name__ == "__main__":
    
    test_main_cnv_sv()
