import os
import config

def cnv_filing(cnvinp, prefix):

    out_file = prefix + ".cnv_circos.txt"
    lines = []
    with open(cnvinp, "r") as cnv:
        for line in cnv:
            if line.split("\t")[0] != "Chr":
                hs = line.split("\t")[0].replace("chr", "hs")
                start = line.split("\t")[1] 
                end = line.split("\t")[2]
                cp = line.split("\t")[6]
                lines = [hs, start, end, cp]
                with open(out_file, "a") as fw:
                    cnv_line = "\t".join(lines) + "\n"
                    fw.write(cnv_line)

    return out_file


if __name__ == "__main__":

    cnv_filing("/lustre/users/zhangxu/DevWork/cnv_report/tests/data/22.tumor.ready.cnv.info.anno.txt", "22.tumor.ready")

