import sys
sys.path.append("../circos_report/sv_anno2conf")
from sv_proconf_cmd import main_sv

params = {"plotinfo": {"chrom_unit": 1000000, "species": "data/hs_circos.txt", "karytotype": "data/karyotype.human.hg19.txt"}, "svinp": "data/22.tumor.ready.mergeavi.anno.txt", "circos_sv_tmp": "data/circos_sv_template.md", "prefix": "patient1", "circos_report_template": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_report_template.md", "circos_snv_tmp": "data/circos_snv_template.md"}

def test_main_sv():
    main_sv(params)

if __name__ == "__main__":
    test_main_sv() 
