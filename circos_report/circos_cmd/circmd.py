import os
from config import circostool
from jbiot import log
from jbiot import jbiotWorker

def circosCMD(params):

    '''arrange outfile to destination directory

    Args:
        params(dict): which has the following keys::

            {
                outconf: "data/circos.snv.conf"
            }
    '''

    confname = params["outconf"] 
    cmd = "perl %s -conf %s" % (circostool,confname)

    tag = "Get the cmd of circos:"
    log.run(tag,cmd)

#==================for omics platfoorm===================
class cirConf_Worker(jbiotWorker):
    def handle_task(self, key, paramsotWorker):
        self.execMyfunc(circos,params)
