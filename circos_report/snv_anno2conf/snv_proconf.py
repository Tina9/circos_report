#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
import jbiot
from jinja2 import Template

def cal_MM(finame):

    # make a list to save the value of the file
    value = []

    with open(finame, 'r') as f:
        for line in f:
            value.append(float(line.rstrip().split("\t")[3]))
    min_value = min(value)
    max_value = max(value)

    return min_value, max_value

def cal_snvMM(params):
    '''get the max and min value of a file's 4th column 
    params involve keys as follows:
    
    Args:
        dict: including the file to get mm value

    Returns:
        dict: a dict including mm value

    the input dict includes following infomation:
        {'snp_out': 'data/22.tumor.ready.snp_circos.txt',
        'indel_out': 'data/22.tumor.ready.indel_circos.txt',}

    '''

    snp_file = params['plotinfo']['snp_out']
    indel_file = params['plotinfo']['indel_out']

    snp_min, snp_max = cal_MM(snp_file)
    indel_min, indel_max = cal_MM(indel_file)

    params['plotinfo']["snp_min"] = snp_min
    params['plotinfo']["snp_max"] = snp_max
    params['plotinfo']["indel_min"] = indel_min
    params['plotinfo']["indel_max"] = indel_max

    return params

def params_filing(pconf_params):
    '''params include keys as follows:
    {
        "cirSNV": "data/circos_snv_template.md",
        "prefix": "patient1.mutect2_snv.anno"
        "plot_info": {
                    "karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt",
                    "chrom_unit": 1000000,
                    "snp_out": "data/22.tumor.ready.snp_circos.txt",
                    "indel_out": "data/22.tumor.ready.indel_circos.txt",
                    "snp_min": 1
                    "snp_max": 2
                    "indel_min": 0
                    "indel_max": 2
                    }
    }
    '''

    params = cal_snvMM(pconf_params)
    
    params['outconf'] = params['prefix'] + "_circos.snv.conf"
    params['plotinfo']['outfile'] = params['prefix'] + "_circos.snv.png"

    return params

def produce_config(param):
    '''get the conf file of circos script

    Args:
        dict: including the file to get mm value

    Returns:
        dict: a dict including mm value and so on

    Dict are as follows:
        {'indel': 'data/patient1.indel_snp.txt', 
        'snvinp': 'data/patient1.mutect2_snv.anno.tsv', 
        'plotinfo': {'indel_out': 'data/patient1.indel_circos.txt', 
                    'snp_out': 'data/patient1.snp_circos.txt', 
                    'chrom_unit': 1000000, 
                    'species': 'data/hs_circos.txt',
                    'karytotype': '/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt'}, 
        'prefix': 'patient1', 
        'circos_snv_tmp': 'data/circos_snv_template.md', 
        'snp': 'data/patient1.snp_snp.txt'}
    '''

    params = params_filing(param)
    
    out = params['outconf']
    tpl = params['circos_snv_tmp']
    loc = params['plotinfo']

    with open(tpl, 'r') as f:
        temp = f.read()

    template = Template(temp)
    circos_input = template.render(loc)

    with open(out, 'w') as f_obj:
        f_obj.write(circos_input)

    return params

if __name__ == "__main__":

    jsonfile = sys.argv[1]

    with open(jsonfile, 'r') as f_obj:
        param_input = json.load(f_obj)

    params = produce_config(param_input)

    with open(jsonfile,'w') as f_w_obj:
        json.dump(params, f_w_obj)

