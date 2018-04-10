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
### My own script to deal with the sv file
sv_filing = os.path.join(sdir, "sv_filing.py")
if not os.path.exists(sv_filing):
    sv_filing = "/opt/sv_filing.py"

### My own script to get the sv conf file
sv_proconf = os.path.join(sdir, "sv_proconf.py")
if not os.path.exists(sv_proconf):
    sv_proconf = "/opt/sv_proconf.py"

######################################################
######################################################
######################################################

def get_cmd(tpl,jsonfile):

    cmd2 = "%s %s" % (sv_filing, jsonfile)
    tag2 = "use the sv_filing script to calculate the MM value"
    log.run(tag2, cmd2, i=[jsonfile], o=[jsonfile])

    cmd3 = "%s %s" % (sv_proconf, jsonfile)
    tag3 = "get the conf file of circos"
    log.run(tag3, cmd3, i=[tpl,jsonfile], o=[jsonfile])

def parse_param(info):
    param = {}
    plotinfo = {}
    plotinfo['species'] = info["circos_species"]
    plotinfo['chrom_unit'] = info["circos_chrom_unit"]
    plotinfo['karytotype'] = info["circos_karytotype"]
    param['plotinfo'] = plotinfo
    param['report_template'] = info['circos_report_template']
    param['sv_annos'] = info['sv_annos']
    param['circos_sv_tmp'] = info['circos_sv_tmp']

    return param

def data_cycle(params):

    anno2conf = params.copy()
    del anno2conf["sv_annos"]
    sv_param = params["sv_annos"]

    circos_res = {}
    for key,value in sv_param.items():
        anno2conf["svinp"] = value
        anno2conf["prefix"] = str(key)

        ### filing the params to the input of transfer json file
        jsonfile = anno2conf['prefix'] + "_transfer.json"
        conf = anno2conf['prefix'] + '_circos.sv.conf'
        png = anno2conf['prefix'] + "_circos.sv.png"
        tpl = anno2conf['circos_sv_tmp']
        paramstr = json.dumps(anno2conf)
        cmd1 = "echo '%s' > %s " % (paramstr,jsonfile)
        log.run("produce a sv json file", cmd1, i=None, o=[jsonfile])

        circos_res[key] = {}
        circos_res[key]["conf"] = conf
        circos_res[key]["png"] = png 
        ### wirte the command to the log file
        get_cmd(tpl, jsonfile)

    ### return a list
    return circos_res

def main_sv(params):
    '''params is an input dict including the following keys

    Args:
        params (dict) : key is `yaml`, value is a yaml file::

            svinp : the output of calling sv
            circos_report_template : the report template
            circos_sv_tmp : the template of sv's conf
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
                    outfile :  the output name of circos file
                    sv_out : the file are used for the snp input of circos png 
                }
            svinp : the output of calling sv
            circos_report_template : the report template
            outconf : name of the circos conf file
            circos_sv_tmp : the template of sv's conf
    '''
    # handle input ...
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())

    cycle_param = parse_param(indict)
    circos_res = data_cycle(cycle_param)

    # handle output ...
    outdict = {}
    outdict["circos_res"] = circos_res
    outdict["circos_text"] = "circos图为sv的结果"
    outdict["yaml"] = yamlin
    yamlout = yamladd(yamlin, outdict)
    return yamlout

class confSV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_sv, params)


