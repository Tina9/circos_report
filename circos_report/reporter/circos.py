import os
from config import circostool
from jbiot import log

def circos():

    cmd = "perl %s -conf circos.conf" % circostool

    tag = "Get the cmd of circos:"
    log.run(tag,cmd)

