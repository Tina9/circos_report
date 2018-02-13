import os
from config import bedtools
from jbiot import log

def count_snp(species, fileA, prefix):

    snp_out = prefix + ".snp_circos.txt"
    snp_cmd = "%s intersect -a %s -b %s -wa -c > %s" % (bedtools, species, fileA, snp_out)

    snp_tag = "get the snp file of circos:"
    log.run(snp_tag, snp_cmd)

    return snp_out

def count_del(species, fileB, prefix):

    del_out = prefix + ".del_circos.txt"
    del_cmd = "%s intersect -a %s -b %s -wa -c > %s" % (bedtools, species, fileB, del_out)

    del_tag = "get the del file of circos:"
    log.run(del_tag,del_cmd)

    return del_out
