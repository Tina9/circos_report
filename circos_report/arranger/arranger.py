#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import json
import os
from jbiot import log
from jbiot import jbiotWorker

def file_arrange(param):

    tgtdir = param['dir']
    files = param['pngs']

    if not os.path.exists(tgtdir):
        cmd = "mkdir -p %s" % tgtdir
        log.run("create directory", cmd)

    for fi in files:
        cmd = "cp %s %s" % (fi, tgtdir)
        log.run("arrange files", cmd)

def projson(param):
    '''
    param = {"pngs": ["data/circos.cnv.png","data/circos.cnv.png"]}
    '''

    files = param["pngs"]

    result = {}
    result["plot_of_circos"] = files

    ### add text to the needer reporter json file
    if "snv_annos" in param and "cnv_annos" in param and "sv_annos" in param:
        result["plot_of_text"] = "circos图由里到外依次为sv,cnv,snp和indel的结果"
    elif "snv_annos" in param and "cnv_annos" in param:
        result["plot_of_text"] = "circos图由里到外依次为cnv,snp和indel的结果"
    elif "snv_annos" in param and "sv_annos" in param:
        result["plot_of_text"] = "circos图由里到外依次为sv,snp和indel的结果"
    elif "cnv_annos" in param and "sv_annos" in param:
        result["plot_of_text"] = "circos图由里到外依次为sv和cnv的结果"
    elif "snv_annos" in param:
        result["plot_of_text"] = "circos图由里到外为snp和indel的结果"
    elif "cnv_annos" in param:
        result["plot_of_text"] = "circos图为cnv的结果"
    elif "sv_annos" in param:
        result["plot_of_text"] = "circos图为sv的结果"

    jsonfile = "report.json"

    paramstr = json.dumps(result)
    cmd = "echo '%s' > %s" % (paramstr, jsonfile)
    log.run("produce the needer reporter json file", cmd)

    param['render_json'] = jsonfile

    return param

def arr_main(params):
    '''params = {
        "pngs": ["data/circos.cnv.png","data/circos.cnv.png"],
        }
    '''
    ### move the file to profit location
    params["dir"] = "report"
    file_arrange(params)
    ### write the information to the json file
    json_param = projson(params)

    return json_param

#==================for omics platfoorm===================
class cirArr_Worker(jbiotWorker):
    def handle_task(self, key, paramsotWorker):
        self.execMyfunc(arr_main, params)
