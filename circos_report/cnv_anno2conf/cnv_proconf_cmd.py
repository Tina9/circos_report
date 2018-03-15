#coding = utf-8
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
    """main_cnv params 

    Args:
        params (dict) : the params to ...::

            {
                "" : "",
                "" : ""

            }

    Returns:
        dict : the description of the dict 

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
