# coding = utf-8
try:
    from config import os
    from config import sys
    from config import json
except:
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

### My own script to seprate the sv file
sv_filing = os.path.join(sdir, "sv_filing.py")
if not os.path.exists(sv_filing):
    sv_filing = "/opt/sv_filing.py"

### My own script to get the conf file
cnv_sv_proconf = os.path.join(sdir, "cnv_sv_proconf.py")
if not os.path.exists(cnv_sv_proconf):
    cnv_sv_proconf = "/opt/cnv_sv_proconf.py"

######################################################
######################################################
######################################################

def filing_cnv_CMD(jsonfile):

    cmd = "python %s %s" % (cnv_filing, jsonfile)
    tag = "use the cnv_filing script to calculate the MM value"
    log.run(tag, cmd)

def filing_sv_CMD(jsonfile):

    cmd = "python %s %s" % (sv_filing, jsonfile)
    tag = "use the sv_filing script to calculate the MM value"
    log.run(tag, cmd)

######################################################
######################################################
######################################################

def confCMD(jsonfile):

    cmd = "python %s %s" % (cnv_sv_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

###########################################################
### main function to get the cmd of cnv_sv_conf file #####
###########################################################

def main_cnv_sv(params):
    
    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.cnv.sv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a cnv_sv json file",cmd)

    filing_cnv_CMD(jsonfile)
    filing_sv_CMD(jsonfile)
    confCMD(jsonfile)

    return params

class conf_CNV_SV_Worker(jbiotWorker):
    def handle_task(self, key, params):
        self.execMyfunc(main_cnv_sv, params)


