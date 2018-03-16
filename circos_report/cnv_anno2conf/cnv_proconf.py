#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
from jbiot import jbiotWorker
from jinja2 import Template

############################################################################################################
####################  calculate the min and max value of the circos input file  ############################
############################################################################################################

def cal_MM(finame):

    # make a list to save the value of the file
    value = []

    with open(finame, 'r') as f:
        for line in f:
            value.append(int(line.rstrip().split("\t")[3]))
    min_value = min(value)
    max_value = max(value)

    return min_value, max_value

#    '''get the max and min value of the circos input file
#    params involve keys as follows:
#
#    Args:
#        dict: including the file to get mm value
#
#    Returns:
#        dict: a dict including mm value
#
#    the input dict includes following information:
#        {"cnv_out": "patient1.cnv_circos.txt"}
#
#    '''
def cal_cnvMM(params):

    cnv_file = params['plotinfo']['cnv_out']

    cnv_min, cnv_max = cal_MM(cnv_file)

    params['plotinfo']['cnv_min'] = cnv_min
    params['plotinfo']['cnv_max'] = cnv_max

    return params


#    '''params include keys as follows:
#    {
#        "plotinfo": 
#            {"karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt", 
#            "chrom_unit": 1000000, 
#            "species": "data/hs_circos.txt",            
#            "cnv_out": "patient1.cnv_circos.txt"}, 
#        "prefix": "patient1", 
#        "cnv_out": "patient1.cnv_circos.txt",
#    }
#    '''
def params_filing(params):

    params = cal_cnvMM(params)

    params['outconf'] = params['prefix'] + '_circos.cnv.conf'
    params['plotinfo']['outfile'] = params['prefix'] + "_circos.cnv.png"

    return params

#    '''get the conf file of circos script
#
#    Args:
#        dict: including mm value
#    
#    Return:
#        dict: a dict including mm value and so on
#
#    Dict is as follows:
#        {
#        "plotinfo": 
#            {"cnv_min": 0, 
#            "karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt", 
#            "cnv_max": 1, 
#            "chrom_unit": 1000000, 
#            "species": "data/hs_circos.txt", 
#            'outfile': "data/patient1_circos.cnv.png",           
#            "cnv_out": "patient1.cnv_circos.txt"}, 
#        "prefix": "patient1", 
#        "outconf" "patient1_circos.cnv.conf",
#        "circos_cnv_tmp": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_template.md"
#        }
#    '''
def produce_config(pconf_params):

    params = params_filing(pconf_params)        
    
    out = params['outconf']
    tpl = params['circos_cnv_tmp']
    loc = params['plotinfo']

    with open(tpl, 'r') as f_obj:
        temp = f_obj.read()
    template = Template(temp)
    circos_input = template.render(loc)

    with open(out, 'w') as f_obj:
        f_obj.write(circos_input)

    return params

if __name__ == "__main__":

    jsonfile = sys.argv[1]
    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    params = produce_config(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(params, f_w_obj)


