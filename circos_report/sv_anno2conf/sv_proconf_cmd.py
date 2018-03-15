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

