#coding=utf-8
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
### My own script to seprate the snv file
snv_filing = os.path.join(sdir, "snv_filing.py")
if not os.path.exists(snv_filing):
    snv_filing = "/opt/snv_filing.py"

### My own script to count the snv file
snv_count = os.path.join(sdir, "snv_count.py")
if not os.path.exists(snv_count):
    snv_count = "/opt/snv_count.py"

### My own script to get the conf file
snv_proconf = os.path.join(sdir,"snv_proconf.py")
if not os.path.exists(snv_proconf):
    snv_proconf = "/opt/snv_proconf.py"


######################################################
######################################################
######################################################

def filingCMD(jsonfile):
    ''' write the cmd of filint in run.cmd
    Dict are as follows:
        {"indel": "patient1.indel_snp.txt", 
         "prefix": "patient1", 
        }
    '''

    cmd = "python %s %s" % (snv_filing, jsonfile)
    tag = "use the snv_filing script to get the separated file"
    log.run(tag, cmd)

def countCMD(jsonfile):
    
    cmd = "python %s %s" % (snv_count, jsonfile)
    tag = "use the snv_count script to get the counted file"
    log.run(tag, cmd)

def confCMD(jsonfile):
    ''' write the cmd to get conf in run.cmd

    Args:
        Dict are as follows:
            {'indel': 'data/patient1.indel_snp.txt', 
            'snvinp': 'data/patient1.mutect2_snv.anno.tsv', 
            'plotinfo': {'indel_out': 'data/patient1.indel_circos.txt', 
                        'snp_out': 'data/patient1.snp_circos.txt', 
                        'chrom_unit': 1000000, 
                        'species': 'data/hs_circos.txt',
                        'karytotype': '/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt'}, 
            'prefix': 'patient1', 
            'cirSNV': 'data/circos_snv_template.md', 
            'snp': 'data/patient1.snp_snp.txt'}

    Returns
        Dict
    '''

    cmd = "python %s %s" % (snv_proconf, jsonfile)
    tag = "get the conf file of circos"
    log.run(tag, cmd)

def main_snv(params):
    '''params include keys as follows:
        {
        "snvinp": "data/patient1.mutect2_snv.anno.tsv",
        "prefix": "patient1",
        }
    '''
    jsonfile = params['prefix'] + "_transfer.json"

    ### get the input file of circmd
    params["outconf"] = params['prefix'] + '_circos.snv.conf'

    paramstr = json.dumps(params)

    cmd = "echo '%s' > %s " % (paramstr,jsonfile)
    log.run("produce a snv json file",cmd)

    filingCMD(jsonfile)
    countCMD(jsonfile)
    confCMD(jsonfile)

    return params

class confSNV_Worker(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(main_snv,params)
    
