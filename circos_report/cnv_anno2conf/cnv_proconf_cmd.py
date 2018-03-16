#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
from jbiot import log
from jbiot import jbiotWorker

sdir = os.path.dirname(os.path.abspath(__file__))
### My own script to seprate the cnv file
cnv_filing = os.path.join(sdir, "cnv_filing.py")
if not os.path.exists(cnv_filing):
    cnv_filing = "/opt/cnv_filing.py"

### My own script to get the conf file
cnv_proconf = os.path.join(sdir, "cnv_proconf.py")
if not os.path.exists(cnv_proconf):
    cnv_proconf = "/opt/cnv_proconf.py"

######################################################
######################################################
######################################################

def filingCMD(jsonfile):

    cmd = "python %s %s" % (cnv_filing, jsonfile)
    tag = "use the cnv_filing script to calculate the MM value"
    log.run(tag, cmd)

def confCMD(jsonfile):

    cmd = "python %s %s" % (cnv_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

def main_cnv(params):
    """params are an input dict which has the following keys 

    Args:
        params(dict): which has the following keys::
            {
            "plotinfo": 
                {
                    "karytotype": "data/karyotype.human.hg19.txt", 
                    "chrom_unit": 1000000, 
                    "species": "data/hs_circos.txt"
                }, 
            "circos_report_template": "data/circos_report_template.md", 
            "prefix": "patient1", 
            "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt", 
            "circos_cnv_tmp": "data/circos_cnv_template.md"}
            }

    Returns:
        dict : which has the following keys::
        {
        "outconf": "patient1_circos.cnv.conf", 
        "circos_cnv_tmp": "data/circos_cnv_template.md", 
        "circos_report_template": "data/circos_report_template.md", 
        "plotinfo": 
            {
                "cnv_min": 0, 
                "karytotype": "data/karyotype.human.hg19.txt", 
                "outfile": "patient1_circos.cnv.png", 
                "cnv_max": 1, 
                "chrom_unit": 1000000, 
                "species": "data/hs_circos.txt", 
                "cnv_out": "patient1.cnv_circos.txt"
            }, 
        "prefix": "patient1", 
        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt"
        }

    """

    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.cnv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a cnv json file",cmd)

    filingCMD(jsonfile)
    confCMD(jsonfile)

    return params    

class confCNV_Worker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(main_cnv, params)
