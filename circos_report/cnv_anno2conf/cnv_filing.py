#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
from jbiot import jbiotWorker

############################################################################################################
################## convert the output of cnvkit into the circos input ######################################
############################################################################################################

#    '''params include keys as follows:
#        {
#        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
#        "prefix": "22.tumor.ready",
#         }    
#    '''

def cnv_filing_count(params):

    cnvinp = params["cnvinp"]
    prefix = params["prefix"]

    title_fold_change = open(cnvinp, "r").readline().split("\t").index("CopyNumber")
    title_chr = open(cnvinp, "r").readline().split("\t").index("Chr")
    title_start = open(cnvinp, "r").readline().split("\t").index("Start")
    title_end = open(cnvinp, "r").readline().split("\t").index("End")


    out_file = prefix + ".cnv_circos.txt"
    lines = []
    with open(cnvinp, "r") as cnv:
        for line in cnv:
            if line.split("\t")[title_chr] != "Chr":
                hs = line.split("\t")[title_chr].replace("chr", "hs")
                start = line.split("\t")[title_start]
                end = line.split("\t")[title_end]
                cp = line.split("\t")[title_fold_change]
                lines = [hs, start, end, cp]
                with open(out_file, "a") as fw:
                    cnv_line = "\t".join(lines) + "\n"
                    fw.write(cnv_line)

    params["plotinfo"]["cnv_out"] = out_file
    return params

def cnv_filing(jsonfile):

    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    cnv_params = cnv_filing_count(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(cnv_params, f_w_obj)


if __name__ == "__main__":

    jsonfile = sys.argv[1]
    cnv_filing(jsonfile)

