import sys
sys.path.append("../circos_report/snv_sv_anno2conf")
from snv_sv_proconf_cmd import main_snv_sv

params = {"svinp": "data/22.tumor.ready.mergeavi.anno.txt", "snvinp": "data/test.mutect2_snv.anno.txt", "prefix": "patient1", "plotinfo": {"chrom_unit": 1000000, "species": "data/hs_circos.txt", "karytotype": "data/karyotype.human.hg19.txt"}, "circos_snv_sv_tmp": "data/circos_snv_sv_template.md","circos_report_template": "data/circos_report_template.md"}

def test_main_snv_sv():

    main_snv_sv(params)

if __name__ == "__main__":

    test_main_snv_sv()
