try:
    from config import render
    from config import md2html
except:
    render = "render.py"
    md2html = "md2html.py"
from jbiot import log
import os
from jbiot import jbiotWorker
from jbiot import get_template
from jbiot import yamladd
import yaml
import json

def report(params):
    """ circos_report to markdown file and html file

    Args: report input dict, key is `yaml`, value is yaml file path::

            "xx": path of xx.

    Returns:
        dict : key is `yaml`,value is yaml file path
    """
    # handle input
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin))

    yamlfile = "circos_report.yaml"
    paramstr = json.dumps(indict)
    cmd1 = "echo '%s' > %s " % (paramstr, yamlfile)
    tag1 = "make sure the existed yaml file"
    log.run("tag1", cmd1, i=None, o=[yamlfile]) 

    templ = get_template("circos_report")
    out = "circos_report.md"
    cmd = "%s -t %s -j %s -o %s -y" % (render,templ,yamlin,out)
    log.run("render circos_report template",cmd)
    
    cmd = "%s %s" % (md2html,out)
    log.run("md2html circos_report ",cmd)
    outdict = {}
    outdict["circos_report"] = out
    yamlout = yamladd(yamlin,outdict)
    yamlout["circos_report_outdir"] = os.getcwd()
    return yamlout

class reportWorker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(report,params)
