import os
import config

def snv_filing(snvinp, prefix):

	with open(snvinp, "r") as fp:
		for info in fp:
			snp_line = []
			del_line = []
			snp_name = prefix + ".snp_snp.txt"
			del_name = prefix + ".del_snp.txt"
			if info.split("\t")[18] == "snp":
				snp_chro = info.split("\t")[0].replace("chr", "hs")
				snp_start = info.split("\t")[1]
				snp_kind = info.split("\t")[18]
				snp_line = [snp_chro,snp_start,snp_start,snp_kind]
				with open(snp_name, "a") as snp:
					snp_lines = '\t'.join(snp_line) + "\n"
					snp.write(snp_lines)

			elif info.split("\t")[18] == "del":
				del_chro = info.split("\t")[0].replace("chr", "hs")
				del_start = info.split("\t")[1]
				del_kind = info.split("\t")[18]
				del_line = [del_chro,del_start,del_start,del_kind]
				with open(del_name, "a") as dele:
					del_lines = '\t'.join(del_line) + "\n"
					dele.write(del_lines)

	return snp_name, del_name

