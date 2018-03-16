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

### My own script to seprate the sv file
sv_filing = os.path.join(sdir, "sv_filing.py")
if not os.path.exists(sv_filing):
    sv_filing = "/opt/sv_filing.py"

### My own script to get the conf file
multi_proconf = os.path.join(sdir, "multi_proconf.py")
if not os.path.exists(multi_proconf):
    multi_proconf = "/opt/multi_proconf.py"

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

def filing_sv_CMD(jsonfile):
    
    cmd = "python %s %s" % (sv_filing, jsonfile)
    tag = "use the sv_filing script to calculate the MM value"
    log.run(tag, cmd)

###########################################################
###########################################################
###########################################################

def confCMD(jsonfile):

    cmd = "python %s %s" % (multi_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

###########################################################
######## main function to get the cmd of snv_cnv_conf file#
###########################################################

def main_multi(params):
    """params are an input dict which has the following keys

        Args:
            params(dict): which has the fillowing keys::

                {
                "snvinp": "data/test.mutect2_snv.anno.txt",
                "plotinfo":
                     {
                        "chrom_unit": 1000000,
                        "species": "data/hs_circos.txt",
                        "karytotype": "data/karyotype.human.hg19.txt",
                     },
                "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
                "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
                "circos_report_template": "data/circos_report_template.md",
                "circos_multi_tmp": "data/circos_multi_template.md",
                "prefix": "patient1"
                }
    
        Returns:
            dict : which has the following keys::

                {
                "plotinfo": 
                    {
                        "snp_min": 0.0, 
                        "indel_out": "patient1.indel_circos.txt", 
                        "cnv_out": "patient1.cnv_circos.txt", 
                        "karytotype": "data/karyotype.human.hg19.txt", 
                        "sv_out": "patient1.sv_circos.txt", 
                        "indel_min": 0.0, 
                        "snp_max": 14.0, 
                        "outfile": "patient1_circos.multi.png", 
                        "indel_max": 2.0, 
                        "snp_out": "patient1.snp_circos.txt", 
                        "chrom_unit": 1000000, 
                        "species": "data/hs_circos.txt", 
                        "cnv_max": 1.0, 
                        "cnv_min": 0.0
                    }, 
                "circos_multi_tmp": "data/circos_multi_template.md", 
                "snvinp": "data/test.mutect2_snv.anno.txt", 
                "circos_report_template": "data/circos_report_template.md", 
                "outconf": "patient1_circos.multi.conf", 
                "prefix": "patient1",
                "svinp": "data/22.tumor.ready.mergeavi.anno.txt", 
                "indel": "patient1.indel_snp.txt", 
                "snp": "patient1.snp_snp.txt", 
                "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt"
                }
    """
    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.multi.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a multi json file",cmd)

    filing_snv_CMD(jsonfile)
    count_snv_CMD(jsonfile)
    filing_cnv_CMD(jsonfile)
    filing_sv_CMD(jsonfile)
    confCMD(jsonfile)

    return params

class confMULTI_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_multi, params)

