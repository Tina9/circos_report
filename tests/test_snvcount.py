import sys
sys.path.append("../")
from circos_report.filing.snv_count import count_snp,count_del

dele = "22.tumor.ready.del_snp.txt"
snp = "22.tumor.ready.snp_snp.txt"
specie = "/lustre/users/zhangxu/DevWork/circos_report/circos_report/filing/hs_circos.txt"
prefix = "22.tumor.ready"

def test_count_snp():

	count_snp(specie, snp, prefix)

def test_count_del():

	count_del(specie, dele, prefix)


if __name__ == "__main__":

	test_count_snp()
	test_count_del()
