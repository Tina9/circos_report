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
from jbiot import log
from jbiot import yamladd
from jbiot import jbiotWorker

sdir = os.path.dirname(os.path.abspath(__file__))
### My own script to seprate the cnv file
cnv_filing = os.path.join(sdir, "cnv_filing.py")
if not os.path.exists(cnv_filing):
    cnv_filing = "/opt/cnv_filing.py"

### My own script to seprate the sv file
sv_filing = os.path.join(sdir, "sv_filing.py")
if not os.path.exists(sv_filing):
    sv_filing = "/opt/sv_filing.py"

### My own script to get the conf file
cnv_sv_proconf = os.path.join(sdir, "cnv_sv_proconf.py")
if not os.path.exists(cnv_sv_proconf):
    cnv_sv_proconf = "/opt/cnv_sv_proconf.py"

######################################################
######################################################
######################################################
def get_cmd(tpl,jsonfile):
    
    cmd2 = "%s %s" % (cnv_filing, jsonfile)
    tag2 = "use the cnv_filing script to calculate the MM value"
    log.run(tag2, cmd2, i=[jsonfile], o=[jsonfile])

    cmd3 = "python %s %s" % (sv_filing, jsonfile)
    tag3 = "use the sv_filing script to calculate the MM value"
    log.run(tag3, cmd3, i=[jsonfile], o=[jsonfile])

    cmd4 = "python %s %s" % (cnv_sv_proconf, jsonfile)
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
    param['cnv_annos'] = info['cnv_annos']
    param['sv_annos'] = info['sv_annos']
    param['circos_cnv_sv_tmp'] = info['circos_cnv_sv_tmp']
    param['report_template'] = info['circos_report_template']
    return param

def data_cycle(params):
    
    anno2conf = params.copy()
    del anno2conf["cnv_annos"]
    del anno2conf["sv_annos"]
    cnv_param = params["cnv_annos"]
    sv_param = params["sv_annos"]

    circos_res = {}
    for key,value in cnv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['cnvinp'] = value
        anno2conf['svinp'] = sv_param[key]

        ### filing the params to the input of transfer json file
        jsonfile = anno2conf['prefix'] + "_transfer.json"
        conf = anno2conf['prefix'] + '_circos.cnv.sv.conf'
        png = anno2conf['prefix'] + '_circos.cnv.sv.png'
        tpl = anno2conf['circos_cnv_sv_tmp']
        paramstr = json.dumps(anno2conf)
        cmd1 = "echo '%s' > %s " % (paramstr,jsonfile)
        log.run("produce a cnv&sv json file", cmd1, i=None, o=[jsonfile])

        circos_res[key] = {}
        circos_res[key]["conf"] = conf
        circos_res[key]["png"] = png 
        ### wirte the command to the log file
        get_cmd(tpl, jsonfile)

    ### return a list
    return circos_res

def main_cnv_sv(params):
    '''params is an input dict including the following keys
    
    Args:
        params (dict) : key is `yaml`, value is a yaml file::

            plotinfo:
                    {
                        karytotype : karytotype file of circos
                        chrom_unit : the basic number of unit(numeric)
                        species : data file including unit of all chromosomes used for bedtools
                    },
            circos_report_template : the report template
            cnvinp : the output of calling cnv
            svinp : the output of calling sv
            circos_cnv_sv_tmp: the template of cnv&sv's conf

    Returns:
        params (dict) : key is `yaml`, value is a yaml file::

            plotinfo :
                {
                    karytotype : karytotype file of circos
                    chrom_unit : the basic number of unit(numeric)
                    species : data file including unit of all chromosomes used for bedtools
                    cnv_min : the min value of the cnv file
                    cnv_max : the max value of the cnv file
                    sv_out : the file are user as the sv input of circos' png
                    cnv_out : the file are used as the cnv input of circos' png
                    outfile : the output name of circos file
                }
            outconf : name os the circos conf file
            circos_cnv_sv_tmp : the template of cnv&sv's conf
            circos_report_template : the report template
            cnvinp : the output of calling cnv
            svinp : the output of calling sv
    '''
    # handle input ...
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())

    cycle_param = parse_param(indict)
    circos_res = data_cycle(cycle_param)

    # handle output ...
    outdict = {}
    outdict["circos_res"] = circos_res
    outdict["circos_text"] = "circos图由里到外依次为sv和cnv的结果"
    yamlout = yamladd(yamlin, outdict)
    return yamlout


class conf_CNV_SV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_cnv_sv,params)
