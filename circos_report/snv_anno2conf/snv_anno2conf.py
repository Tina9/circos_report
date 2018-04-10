#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

try:
    import config
except:
    pass

import os 
import sys
import json
import yaml
from jbiot import yamladd
from jbiot import log
from jbiot import jbiotWorker


sdir = os.path.dirname(os.path.abspath(__file__))
### My own script to seprate the snv file
snv_filing = os.path.join(sdir, "snv_filing.py")
if not os.path.exists(snv_filing):
    snv_filing = "/opt/snv_filing.py"

### My own script to count the snv file
snv_count = os.path.join(sdir, "snv_count.py")
if not os.path.exists(snv_count):
    snv_count = "/opt/snv_count.py"

### My own script to get the conf file
snv_proconf = os.path.join(sdir,"snv_proconf.py")
if not os.path.exists(snv_proconf):
    snv_proconf = "/opt/snv_proconf.py"

######################################################
######################################################
######################################################
def get_cmd(tpl, jsonfile):

    cmd2 = "%s %s" % (snv_filing, jsonfile) 
    tag2 = "use the snv_filing script to get the separated file" 
    log.run(tag2, cmd2, i=[jsonfile], o=[jsonfile])

    cmd3 = "%s %s" % (snv_count, jsonfile)
    tag3 = "use the snv_count script to get the counted file"
    log.run(tag3, cmd3, i=[jsonfile], o=[jsonfile])

    cmd4 = "%s %s" % (snv_proconf, jsonfile)
    tag4 = "get the conf file of circos"
    log.run(tag4, cmd4, i=[tpl,jsonfile], o=[jsonfile])

def parse_param(info):
    ### make a dict to save the data about plot information
    param = {}
    plotinfo = {}
    plotinfo['species'] = info["circos_species"]
    plotinfo['chrom_unit'] = info["circos_chrom_unit"]
    plotinfo['karytotype'] = info["circos_karytotype"]
    param['plotinfo'] = plotinfo
    param['snv_annos'] = info['snv_annos']
    param['circos_snv_tmp'] = info['circos_snv_tmp']
    param['report_template'] = info['circos_report_template']
    return param

def data_cycle(params):
    
    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    snv_param = params["snv_annos"]

    circos_res = {}
    for key,value in snv_param.items():
        anno2conf['snvinp'] = value
        anno2conf['prefix'] = str(key)

        ### filing the params to the input of transfer json file
        jsonfile = anno2conf['prefix'] + "_transfer.json"
        conf = anno2conf['prefix'] + '_circos.snv.conf'
        png = anno2conf['prefix'] + "_circos.snv.png"
        tpl = anno2conf['circos_snv_tmp']
        paramstr = json.dumps(anno2conf)
        cmd1 = "echo '%s' > %s " % (paramstr,jsonfile)
        log.run("produce a snv json file", cmd1, i=None, o=[jsonfile])

        circos_res[key] = {}
        circos_res[key]["conf"] = conf
        circos_res[key]["png"] = png
        ### wirte the command to the log file
        get_cmd(tpl, jsonfile)

    ### return a list
    return circos_res

def main_snv(params):
    '''params is an input dict including the following keys

    Args:
        params (dict) : key is `yaml`, value is a yaml file::

            snvinp : the output of calling snv
            circos_report_template : the report template
            circos_snv_tmp : the template of snv's conf
            plotinfo :
                {
                    chrom_unit : the basic number of unit(numeric)
                    species : data file including unit of all chromosomes used for bedtools
                    karytotype : karytotype file of circos    
                }

    Returns:
        params (dict) : key is `yaml`, value is a yaml file::

            plotinfo : 
                {
                    chrom_unit : the basic number of unit(numeric)
                    species : data file including unit of all chromosomes used for bedtools
                    karytotype : karytotype file of circos
                    snp_min :  the min value of snp file
                    snp_max : the max value of snp file
                    indel_min : the min value of indel file
                    indel_max : the max value of indel file
                    outfile :  the output name of circos file
                    snp_out : the file are used for the snp input of circos png 
                    indel_out : the file are used for the indel input of circos png
                }
            snvinp : the output of calling snv
            circos_report_template : the report template
            outconf : name of the circos conf file
            indel : the indel file after separated from annotated file
            snp :  the snp file after separated from annotated file
            circos_snv_tmp : the template of snv's conf
    '''
    # handle input ...
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())
    
    cycle_param = parse_param(indict)
    circos_res = data_cycle(cycle_param)

    # handle output ...
    outdict = {}
    outdict["circos_res"] = circos_res
    outdict["circos_text"] = "circos图由里到外为snp和indel的结果"
    outdict["yaml"] = yamlin
    yamlout = yamladd(yamlin, outdict)
    return yamlout


#==========for omics platform============#
class confSNV_Worker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(main_snv,params)



