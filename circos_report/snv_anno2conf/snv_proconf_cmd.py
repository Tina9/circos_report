#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

import os
import sys
import json
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

def filingCMD(jsonfile):

    cmd = "python %s %s" % (snv_filing, jsonfile)
    tag = "use the snv_filing script to get the separated file"
    log.run(tag, cmd)

def countCMD(jsonfile):
    
    cmd = "python %s %s" % (snv_count, jsonfile)
    tag = "use the snv_count script to get the counted file"
    log.run(tag, cmd)

def confCMD(jsonfile):

    cmd = "python %s %s" % (snv_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

def main_snv(params):
    '''params are an input dict which has the following keys

        Args:
            params(dict): which has the following keys::
        
                {
                    "snvinp": "data/test.mutect2_snv.anno.txt",
                    "circos_report_template": "data/circos_report_template.md",
                    "circos_snv_tmp": "data/circos_snv_template.md",
                    "prefix": "patient1",
                    "plotinfo":
                        {
                            "chrom_unit": 1000000,
                            "species": "data/hs_circos.txt",
                            "karytotype": "data/karyotype.human.hg19.txt"
                        }
                }

    Returns:
        dict: which has the following keys::

            {
            "plotinfo": 
                {
                "snp_min": 0, 
                "indel_out": "patient1.indel_circos.txt", 
                "karytotype": "data/karyotype.human.hg19.txt", 
                "indel_min": 0, 
                "snp_max": 7, 
                "outfile": "patient1_circos.snv.png", 
                "indel_max": 1, 
                "snp_out": "patient1.snp_circos.txt", 
                "chrom_unit": 1000000, 
                "species": "data/hs_circos.txt"
                }, 
            "snvinp": "data/test.mutect2_snv.anno.txt", 
            "circos_report_template": "data/circos_report_template.md", 
            "outconf": "patient1_circos.snv.conf", 
            "prefix": "patient1", 
            "indel": "patient1.indel_snp.txt", 
            "snp": "patient1.snp_snp.txt", 
            "circos_snv_tmp": "data/circos_snv_template.md"
            } 
    '''

    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.snv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a snv json file",cmd)

    filingCMD(jsonfile)
    countCMD(jsonfile)
    confCMD(jsonfile)

    return params

#==========for omics platform============#
class confSNV_Worker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(main_snv,params)
    
