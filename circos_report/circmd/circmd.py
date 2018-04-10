#!/usr/bin/env python
#coding=utf-8

__authon__ = "zhangxu"


import yaml
from config import circostool
from jbiot import log
from jbiot import yamladd
from jbiot import jbiotWorker

def data_cycle(params):
    
    circos_res = params['circos_res']    
    for patient,value in circos_res.items():
        conf = value['conf']
        png = value['png']
        cmd = "perl %s -conf %s" % (circostool,conf)
        tag = "Get the cmd of circos:"
        log.run(tag, cmd, i=[conf], o=[png])

def circmd(params):
    '''params is an input dict which includes the following keys

    Args:
        params (dict) : key is `yaml`, value is a yaml file::

            'outconf:': the name of the circos conf file

    Returns:
        str : out yaml file
    '''

    # handle input ...
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())
    data_cycle(indict)

    # handle output ...
    outdict = {}
    yamlout = yamladd(yamlin, outdict)
    return yamlout


#==================for omics platfoorm===================
class circmd_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(circmd,params)


