#!/usr/bin/env python
#coding=utf-8
import sys
import os
import yaml

dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../circos_report")
sys.path.insert(0,dirpath)

from docopt import docopt
from snv_anno2conf.snv_proconf_cmd import main_snv
from cnv_anno2conf.cnv_proconf_cmd import main_cnv
from sv_anno2conf.sv_proconf_cmd import main_sv
from snv_cnv_anno2conf.snv_cnv_proconf_cmd import main_snv_cnv
from snv_sv_anno2conf.snv_sv_proconf_cmd import main_snv_sv
from cnv_sv_anno2conf.cnv_sv_proconf_cmd import main_cnv_sv
from multi_anno2conf.multi_proconf_cmd import main_multi
from circos_cmd.circmd import circosCMD
from arranger.arranger import arr_main
from reporter.report import report
from jbiot import jbiotWorker

### Common function to get the parameter of yaml
def parse_yml_parameter(info):
    ### make a dict to save the data about plot information
    param = {}
    plotinfo = {}
    plotinfo['species'] = info["circos_species"]
    plotinfo['chrom_unit'] = info["circos_chrom_unit"]
    plotinfo['karytotype'] = info["circos_karytotype"]
    param['plotinfo'] = plotinfo
    param['report_template'] = info['circos_report_template']

    if "snv_annos" in info and "cnv_annos" in info and "sv_annos" in info:
        param['snv_annos'] = info['snv_annos']
        param['cnv_annos'] = info['cnv_annos']
        param['sv_annos'] = info['sv_annos']
        param['circos_multi_tmp'] = info['circos_multi_tmp']        

    elif "snv_annos" in info and "cnv_annos" in info:
        param['snv_annos'] = info['snv_annos']
        param['cnv_annos'] = info['cnv_annos']
        param['circos_snv_cnv_tmp'] = info['circos_snv_cnv_tmp']
    
    elif "snv_annos" in info and "sv_annos" in info:
        param['snv_annos'] = info['snv_annos']
        param['sv_annos'] = info['sv_annos']
        param['circos_snv_sv_tmp'] = info['circos_snv_sv_tmp']
    
    elif "cnv_annos" in info and "sv_annos" in info:
        param['cnv_annos'] = info['cnv_annos']
        param['sv_annos'] = info['sv_annos']
        param['circos_cnv_sv_tmp'] = info['circos_cnv_sv_tmp']

    elif "snv_annos" in info:
        param['snv_annos'] = info['snv_annos']
        param['circos_snv_tmp'] = info['circos_snv_tmp']

    elif "cnv_annos" in info:
        param['cnv_annos'] = info['cnv_annos']
        param['circos_cnv_tmp'] = info['circos_cnv_tmp']

    elif "sv_annos" in info:
        param['sv_annos'] = info['sv_annos']
        param['circos_sv_tmp'] = info['circos_sv_tmp'] 

    return param

def choose_snv(params):

    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    snv_param = params["snv_annos"]

    pngs = []
    for key,value in snv_param.items():
        anno2conf['snvinp'] = value
        anno2conf['prefix'] = str(key)
        
        ### convert tsv into conf
        circmd_param = main_snv(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.snv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_cnv(params):

    anno2conf = params.copy()
    del anno2conf["cnv_annos"]
    cnv_param = params["cnv_annos"]

    pngs = []
    for key,value in cnv_param.items():
        anno2conf['cnvinp'] = value
        anno2conf['prefix'] = str(key)

        ### convert tsv into conf
        circmd_param = main_cnv(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.cnv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_sv(params):

    anno2conf = params.copy()
    del anno2conf["sv_annos"]
    sv_param = params["sv_annos"]

    pngs = []
    for key, value in sv_param.items():
        anno2conf['svinp'] = value
        anno2conf['prefix'] = str(key)

        ### convert tsv into conf
        circmd_param = main_sv(anno2conf) 

        ### exec the conf file 
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.sv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs
    
    return params

def choose_snv_cnv(params):

    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    del anno2conf["cnv_annos"]
    snv_param = params["snv_annos"]
    cnv_param = params["cnv_annos"]

    pngs = []
    for key,value in snv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['snvinp'] = value
        anno2conf['cnvinp'] = cnv_param[key]

        ### convert tsv info conf
        circmd_param = main_snv_cnv(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.snv.cnv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_snv_sv(params):

    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    del anno2conf["sv_annos"]
    snv_param = params["snv_annos"]
    sv_param = params["sv_annos"]

    pngs = []
    for key, value in snv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['snvinp'] = value
        anno2conf['svinp'] = sv_param[key]

        ### convert tsv info conf
        circmd_param = main_snv_sv(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.snv.sv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_cnv_sv(params):

    anno2conf = params.copy()
    del anno2conf["cnv_annos"]
    del anno2conf["sv_annos"]
    cnv_param = params["cnv_annos"]
    sv_param = params["sv_annos"]

    pngs = []
    for key, value in cnv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['cnvinp'] = value
        anno2conf['svinp'] = sv_param[key]
    
        ### convert tsv info conf
        circmd_param = main_cnv_sv(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.cnv.sv.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_multi(params):

    anno2conf = params.copy()
    del anno2conf["snv_annos"]
    del anno2conf["cnv_annos"]
    del anno2conf["sv_annos"]
    snv_param = params["snv_annos"]
    cnv_param = params["cnv_annos"]
    sv_param = params["sv_annos"]

    pngs = []
    for key,value in snv_param.items():
        anno2conf['prefix'] = str(key)
        anno2conf['snvinp'] = value
        anno2conf['cnvinp'] = cnv_param[key]
        anno2conf['svinp'] = sv_param[key]

        ### convert tsv info conf
        circmd_param = main_multi(anno2conf)

        ### exec the conf file
        circosCMD(circmd_param)

        ### return pngs to arrange
        anno2conf['plotinfo']['outfile'] = anno2conf['prefix'] + "_circos.multi.png"
        pngs.append(anno2conf['plotinfo']['outfile'])

    params['pngs'] = pngs

    return params

def choose_proConf_CMD(params):

    if "snv_annos" in params and "cnv_annos" in params and "sv_annos" in params:

        choose_param = choose_multi(params)

    elif "snv_annos" in params and "cnv_annos" in params:

        choose_param = choose_snv_cnv(params)

    elif "snv_annos" in params and "sv_annos" in params:

        choose_param = choose_snv_sv(params)

    elif "cnv_annos" in params and "sv_annos" in params:

        choose_param = choose_cnv_sv(params)

    elif "snv_annos" in params:

        choose_param = choose_snv(params)

    elif "cnv_annos" in params:

        choose_param = choose_cnv(params)

    elif "sv_annos" in params:

        choose_param = choose_sv(params)

    return choose_param

################################################################################
###################### the main function to get circos conf ####################
################################################################################

def main_circos(params):

    to_be_chosen_params = parse_yml_parameter(params)

    choose_param = choose_proConf_CMD(to_be_chosen_params)
    print choose_param

    ### arrange the file
    jsonfile_param = arr_main(choose_param) 
   
    ### get the result report
    to_report_param = {}
    to_report_param["render_json"] = jsonfile_param["render_json"] 
    to_report_param["report_template"] = choose_param["report_template"] 

    ### get the report of the circos result
    report(to_report_param)

    return {}


class circosWorker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(main_circos)

def parse_yml(yml):

    info = yaml.load(open(yml, 'r').read())

    main_circos(info)

if __name__ == "__main__":
    usage= """
    Usage:
        cnv_report.py -c <parameter>
    
    Options:
        -c, --conf <params>    params file for soft in yaml format

    """

    args = docopt(usage)
    yml = args["--conf"]    

    parse_yml(yml)
