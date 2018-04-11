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
### My own script to seprate the snv file
snv_filing = os.path.join(sdir, "snv_filing.py")
if not os.path.exists(snv_filing):
    snv_filing = "/opt/snv_filing.py"

### My own script to count the snv file
snv_count = os.path.join(sdir, "snv_count.py")
if not os.path.exists(snv_count):
    snv_count = "/opt/snv_count.py"

### My own script to seprate the cnv file
cnv_filing = os.path.join(sdir, "cnv_filing.py")
if not os.path.exists(cnv_filing):
    cnv_filing = "/opt/cnv_filing.py"

### My own script to get the conf file
snv_cnv_proconf = os.path.join(sdir, "snv_cnv_proconf.py")
if not os.path.exists(snv_cnv_proconf):
    snv_cnv_proconf = "/opt/snv_cnv_proconf.py"

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

    cmd4 = "%s %s" % (cnv_filing, jsonfile)
    tag4 = "use the cnv_filing script to calculate the MM value"
    log.run(tag4, cmd4, i=[jsonfile], o=[jsonfile])

    cmd5 = "%s %s" % (snv_cnv_proconf, jsonfile)
    tag5 = "get the conf file of circos"
    log.run(tag5, cmd5, i=[tpl, jsonfile], o=[jsonfile])

def parse_param(info):
    ### make a dict to save the data about plot information
    param = {}
    plotinfo = {}
    plotinfo['species'] = info["circos_species"]
    plotinfo['chrom_unit'] = info["circos_chrom_unit"]
    plotinfo['karytotype'] = info["circos_karytotype"]
    param['plotinfo'] = plotinfo
    param['snv_annos'] = info['snv_annos']
    param['cnv_annos'] = info['cnv_annos']
    param['circos_snv_cnv_tmp'] = info['circos_snv_cnv_tmp']
    param['report_template'] = info['circos_report_template']
    return param

def data_cycle(params):

    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    del anno2conf["cnv_annos"]
    snv_param = params["snv_annos"]
    cnv_param = params["cnv_annos"]

    circos_res = {}
    for key,value in snv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['snvinp'] = value
        anno2conf['cnvinp'] = cnv_param[key]

        ### filing the params to the input of transfer json file
        jsonfile = anno2conf['prefix'] + "_transfer.json"
        conf = anno2conf['prefix'] + '_circos.snv.cnv.conf'
        png = anno2conf['prefix'] + '_circos.snv.cnv.png'
        tpl = anno2conf['circos_snv_cnv_tmp']
        paramstr = json.dumps(anno2conf)
        cmd1 = "echo '%s' > %s " % (paramstr,jsonfile)
        log.run("produce a snv&cnv json file", cmd1, i=None, o=[jsonfile])

        circos_res[key] = {}
        circos_res[key]["conf"] = conf
        circos_res[key]["png"] = png 
        ### wirte the command to the log file
        get_cmd(tpl, jsonfile)

    ### return a list
    return circos_res

def main_snv_cnv(params):
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
            snvinp : the output of calling snv
            circos_snv_cnv_tmp : the template of snv&cnv's conf

    Returns:
        params (dict) : key is `yaml`, value is a yaml file::

            plotinfo :
                {
                    karytotype : karytotype file of circos
                    chrom_unit : the basic number of unit(numeric)
                    species : data file including unit of all chromosomes used for bedtools
                    snp_min :  the min value of snp file
                    snp_max : the max value of snp file
                    indel_min : the min value of indel file
                    indel_max : the max value of indel file
                    cnv_min : the min value of the cnv file
                    cnv_max : the max value of the cnv file
                    outfile : the output name of circos file
                    snp_out : the file are used for the snp input of circos png
                    indel_out : the file are used for the indel input of circos png
                    cnv_out : the file are used as the cnv input of circos' png 
                }
            outconf : name of the circos conf file
            circos_snv_cnv_tmp : the template of snv&cnv's conf
            circos_report_template : the report template
            snp :  the snp file after separated from annotated file
            indel : the indel file after separated from annotated file
            snvinp : the output of calling snv
            cnvinp : the output of calling cnv
    '''
    # handle input ...
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())

    cycle_param = parse_param(indict)
    circos_res = data_cycle(cycle_param)

    # handle output ...
    outdict = {}
    outdict["circos_text"] = "circos图由里到外依次为cnv,snp和indel的结果"
    outdict["circos_res"] = circos_res
    yamlout = yamladd(yamlin, outdict)
    return yamlout


class conf_SNV_CNV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_snv_cnv, params)

