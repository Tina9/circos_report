import os
import config

def sv_filing(svinp, prefix):

	outfile = prefix + ".sv_circos.txt"
	lines = []
	with open(svinp, "r") as fr:
		for line in fr:
			if line.split("\t")[0] != "Chr":
				hs1 = line.split("\t")[0].replace("chr", "hs")
				break1  = line.split("\t")[1]
				hs2 = line.split("\t")[4].replace("chr", "hs")
				break2 = line.split("\t")[5]
				lines = [hs1, break1, break1, hs2, break2, break2]

				with open(outfile, "a") as fw:
					sv_line = "\t".join(lines) + "\n"
					fw.write(sv_line)

	return outfile

if __name__ == "__main__":

	sv_filing("/lustre/users/zhangxu/DevWork/sv_report/tests/data/22.tumor.ready.mergeavi.anno.txt", "22.tumor.ready")
