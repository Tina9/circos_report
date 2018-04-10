#!/usr/bin/env python
#! -*- coding:utf-8 -*-

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

def cal_cnvMM(params):

    cnv_file = params['plotinfo']['cnv_out']

    cnv_min, cnv_max = cal_MM(cnv_file)

    params['plotinfo']['cnv_min'] = cnv_min
    params['plotinfo']['cnv_max'] = cnv_max

    return params

def params_filing(params):

    params = cal_cnvMM(params)

    params['outconf'] = params['prefix'] + '_circos.cnv.sv.conf'
    params['plotinfo']['outfile'] = params['prefix'] + "_circos.cnv.sv.png"

    return params

def produce_config(pconf_params):
    
    params = params_filing(pconf_params)

    out = params['outconf']
    tpl = params['circos_cnv_sv_tmp']
    loc = params['plotinfo']

    with open(tpl, 'r') as f_obj:
        temp = f_obj.read()
    template = Template(temp)
    circos_input = template.render(loc)

    with open(out, 'w') as f_w_obj:
        f_w_obj.write(circos_input)
    
    return params

if __name__ == "__main__":

    jsonfile = sys.argv[1]
    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    params = produce_config(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(params, f_w_obj)
