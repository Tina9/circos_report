#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "zhangxu"

try:
    from config import render
    from config import md2html
except:
    render = "render.py"
    md2html = "md2html.py"
import os
from jbiot import jbiotWorker
from jbiot import log

def get_file(remotefile):
    home = os.environ["HOME"]
    localfile = remotefile.split("/")[-1]
    cmd = "wget %s -P %s/.templates " % (home,remotefile)

    localfile = os.path.join(home,".templates",localfile)
    if os.path.exists(localfile):
        return localfile
    tag = "get circos report templates"
    log.run(tag,cmd)
    if os.path.exists(localfile):
        return localfile
    return 

def report(params):

    '''params is a input dict which has the following keys

    Args:
        params(dict): which has the following keys::

            {
                render_json  : data/circos_report_template.md
                report_template  : data/report.json
            }

    Returns:
        dict: which has the following keys:: 

            {
                "snvReport": "report.md"
            }
    '''

    # get template
    templ = params["report_template"]
    if templ.startswith("http://"):
        templ = get_file(templ)

    ijson = params["render_json"] 
    out = "circos_report.md"
    cmd = "%s -t %s -j %s -o %s" % (render,templ,ijson,out)
    log.run("render mapping circos template",cmd,docker="kongdeju/alpine-dev:stable")

    cmd = "%s %s" % (md2html,out)
    log.run("md2html circos report ",cmd,docker="kongdeju/alpine-dev:stable")

    outdict = {}
    outdict["report_md"] = out
    return outdict

class reportWorker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(report,params)

