#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

try:
    from config import bedtools
except:
    bedtools = "bedtools"
  
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

def filing_snv_CMD(jsonfile):

    cmd = "python %s %s" % (snv_filing, jsonfile)
    tag = "use the snv_filing script to get the separated file"
    log.run(tag, cmd)

def count_snv_CMD(jsonfile):
    
    cmd = "python %s %s" % (snv_count, jsonfile)
    tag = "use the snv_count script to get the counted file"
    log.run(tag, cmd)

###########################################################
###########################################################
###########################################################

def filing_cnv_CMD(jsonfile):

    cmd = "python %s %s" % (cnv_filing, jsonfile)
    tag = "use the cnv_filing script to calculate the MM value"
    log.run(tag, cmd)

###########################################################
###########################################################
###########################################################

def confCMD(jsonfile):

    cmd = "python %s %s" % (snv_cnv_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

###########################################################
######## main function to get the cmd of snv_cnv_conf file#
###########################################################

def main_snv_cnv(params):
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
            "circos_snv_cnv_tmp": "data/circos_snv_cnv_template.md", 
            "snvinp": "data/test.mutect2_snv.anno.txt", 
            "prefix": "patient1", 
            "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
            "circos_report_template": "data/circos_report_template.md"
            }

    Returns:
        dict : which has the following keys::

            {
            "outconf": "patient1_circos.snv.cnv.conf", 
            "circos_snv_cnv_tmp": "data/circos_snv_cnv_template.md", 
            "snvinp": "data/test.mutect2_snv.anno.txt", 
            "circos_report_template": "data/circos_report_template.md", 
            "plotinfo": 
                {
                    "snp_min": 0.0, 
                    "indel_out": "patient1.indel_circos.txt", 
                    "cnv_out": "patient1.cnv_circos.txt", 
                    "karytotype": "data/karyotype.human.hg19.txt", 
                    "indel_min": 0.0, 
                    "snp_max": 7.0, 
                    "outfile": "patient1_circos.snv.cnv.png", 
                    "indel_max": 1.0, 
                    "snp_out": "patient1.snp_circos.txt", 
                    "chrom_unit": 1000000, 
                    "species": "data/hs_circos.txt", 
                    "cnv_max": 1.0, 
                    "cnv_min": 0.0  
                }, 
            "prefix": "patient1", 
            "indel": "patient1.indel_snp.txt", 
            "snp": "patient1.snp_snp.txt", 
            "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt"
            }   
    """
    
    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.snv.cnv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a snv_cnv json file",cmd)

    filing_snv_CMD(jsonfile)
    count_snv_CMD(jsonfile)
    filing_cnv_CMD(jsonfile)
    confCMD(jsonfile)

    return params

class conf_SNV_CNV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_snv_cnv, params)

