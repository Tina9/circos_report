#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
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

def filingCMD(jsonfile):

    cmd = "python %s %s" % (sv_filing, jsonfile)
    tag = "use the sv_filing script to get the input file of circos"
    log.run(tag, cmd)

def confCMD(jsonfile):

    cmd = "python %s %s" % (sv_proconf, jsonfile)
    tag = "get the conf file of circos sv"
    log.run(tag, cmd)

def main_sv(params):
    """params are an input dict which has the following keys 

    Args:
        params(dict): which has the following keys::

            {
                "plotinfo": 
                    {
                        "chrom_unit": 1000000, 
                        "species": "data/hs_circos.txt", 
                        "karytotype": "data/karyotype.human.hg19.txt"
                    }, 
                "svinp": "data/22.tumor.ready.mergeavi.anno.txt", 
                "circos_sv_tmp": "data/circos_sv_template.md", 
                "prefix": "patient1", 
                "circos_report_template": "data/circos_report_template.md", 
                "circos_snv_tmp": "data/circos_snv_template.md"
            }

    Returns:
        dict : which has the following keys::

            {
                "outconf": "patient1_circos.sv.conf", 
                "circos_report_template": "data/circos_report_template.md", 
                "plotinfo": 
                {
                    "sv_out": "patient1.sv_circos.txt", 
                    "outfile": "patient1_circos.sv.png", 
                    "chrom_unit": 1000000, 
                    "species": "data/hs_circos.txt", 
                    "karytotype": "data/karyotype.human.hg19.txt"
                }, 
                "prefix": "patient1", 
            "svinp": "data/22.tumor.ready.mergeavi.anno.txt", 
            "circos_snv_tmp": "data/circos_snv_template.md", 
            "circos_sv_tmp": "data/circos_sv_template.md"
            }
    """

    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.sv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a sv json file",cmd)

    filingCMD(jsonfile)
    confCMD(jsonfile)

    return params

class confSV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execfunc(main_sv, params)

