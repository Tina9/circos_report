import os
from config import circostool
from jbiot import log

def circos(kind):

    cmd = "perl %s -conf %s" % (circostool,kind)

    tag = "Get the cmd of circos:"
    log.run(tag,cmd)

