#!/usr/bin/env python
#coding=utf-8

__authon__ = "zhangxu"

import sys
import os
dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"../circos_report")
sys.path.insert(0,dirpath)
from snv_anno2conf.snv_anno2conf import main_snv
from cnv_anno2conf.cnv_anno2conf import main_cnv
from sv_anno2conf.sv_anno2conf import main_sv
from snv_cnv_anno2conf.snv_cnv_anno2conf import main_snv_cnv
from snv_sv_anno2conf.snv_sv_anno2conf import main_snv_sv
from cnv_sv_anno2conf.cnv_sv_anno2conf import main_cnv_sv
from multi_anno2conf.multi_anno2conf import main_multi
from circmd.circmd import circmd
from arranger.arrange import arrange
from reporter.report import report 
import yaml
from jbiot import jbiotWorker

# choose anno2conf
def choose_anno2conf(indict):

    yml = indict["yaml"]
    params = yaml.load(open(yml).read())

    if "snv_annos" in params and "cnv_annos" in params and "sv_annos" in params:

        main_multi(params)

    elif "snv_annos" in params and "cnv_annos" in params:

        main_snv_cnv(params)

    elif "snv_annos" in params and "sv_annos" in params:

        main_snv_sv(params)

    elif "cnv_annos" in params and "sv_annos" in params:

        main_cnv_sv(params)

    elif "snv_annos" in params:

        main_snv(params)

    elif "cnv_annos" in params:

        main_cnv(params)

    elif "sv_annos" in params:

        main_sv(params)

# entrypoint function
def circos_report(params):

    # call apps
    choose_anno2conf(params)
    circmd(params)
    arrange(params)
    report(params)
    
    return params

# mulit-omics platform
class circos_reportWorker(jbiotWorker):
    def handle_task(self,key,params):
        self.execute(circos_report,params)


# main function
def main(yml):
    #1. read yaml 
    params = {}
    params["yaml"] = yml
    circos_report(params)

if __name__ == "__main__":
    from docopt import docopt
    usage = """
    Usage:
       circos_report.py -c <params> 

    Options:
        -c,--conf <params>    params in yaml format.

    """
    args = docopt(usage)
    yml = args["--conf"]
    main(yml)
