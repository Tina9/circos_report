#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import json
import sys

def snv_filing_sep(params):
    '''params include keys as follows:
    {
    "snvinp": "data/patient1.mutect2_snv.anno.tsv",
    "prefix": "patient1",
    }
    '''

    snvinp = params["snvinp"]
    prefix = params["prefix"]

    title_index = open(snvinp, "r").readline().split("\t").index("VarType")

    with open(snvinp, "r") as fp:
        for info in fp:
            snp_line = []
            indel_line = []
            snp_name = prefix + ".snp_snp.txt"
            indel_name = prefix + ".indel_snp.txt"
            if info.split("\t")[title_index] == "snp":
                snp_chro = info.split("\t")[0].replace("chr", "hs")
                snp_start = info.split("\t")[1]
                snp_kind = info.split("\t")[title_index]
                snp_line = [snp_chro,snp_start,snp_start,snp_kind]
                with open(snp_name, "a") as snp:
                    snp_lines = '\t'.join(snp_line) + "\n"
                    snp.write(snp_lines)

            elif info.split("\t")[title_index] == "del" or info.split("\t")[title_index] == "ins":
                indel_chro = info.split("\t")[0].replace("chr", "hs")
                indel_start = info.split("\t")[1]
                indel_kind = info.split("\t")[title_index]
                indel_line = [indel_chro,indel_start,indel_start,indel_kind]
                with open(indel_name, "a") as dele:
                    indel_lines = '\t'.join(indel_line) + "\n"
                    dele.write(indel_lines)

    params["snp"] = snp_name
    params["indel"] = indel_name

    return params


def snv_filing(jsonfile):
    '''read in a json file and separate it
    Args:
        json(dict): keys are as follows

        {
        "snvinp": "data/patient1.mutect2_snv.anno.tsv",
        "prefix": "patient1",
         }

    Returns:
        json(dict): keys are as follow

        {
        "snvinp": "data/patient1.mutect2_snv.anno.tsv",
        "prefix": "patient1",
        "snp": "patient1.snp_snp.txt",
        "indel": "patient1.indel_snp.txt",
        }
   '''

    with open(jsonfile, "r") as f_obj:
        params = json.load(f_obj)

    snv_params = snv_filing_sep(params)  
    
    with open(jsonfile,'w') as f_wobj:
        json.dump(snv_params, f_wobj)

if __name__ == "__main__":
    
    jsonfile = sys.argv[1]
    snv_filing(jsonfile)

