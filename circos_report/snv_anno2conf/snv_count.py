#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json

bedtools = "bedtools"

#####################################################################
############## Using snv_count to get the count CMD #################
#####################################################################

def snp_indel_count(params):
    '''params include keys as follows:
        {"snp": "data/22.tumor.ready.snp_snp.txt",
        "indel": "data/22.tumor.ready.indel_snp.txt",
        "prefix": "22.tumor.ready"
        "plotinfo": {
            "species": "data/hs_circos.txt",
            }
        }
    '''

    species = params["plotinfo"]["species"]
    prefix = params["prefix"]
    fileA = params["snp"]
    fileB = params["indel"]

    ################ Using bedtools to calculate the MM value ########################
    snp_out = prefix + ".snp_circos.txt"
    os.system("%s intersect -a %s -b %s -wa -c > %s" % (bedtools, species, fileA, snp_out))

    indel_out = prefix + ".indel_circos.txt"
    os.system("%s intersect -a %s -b %s -wa -c > %s" % (bedtools, species, fileB, indel_out))

    params['plotinfo']["snp_out"] = prefix + ".snp_circos.txt"
    params['plotinfo']["indel_out"] = prefix + ".indel_circos.txt"

    return params

if __name__ == "__main__":

    jsonfile = sys.argv[1]
    
    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    snp_indel_count_param = snp_indel_count(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(snp_indel_count_param, f_w_obj)
