import os
import sys
import json    
from jbiot import jbiotWorker

#    '''params include keys as follows:
#    {
#        "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
#        "prefix" "22.tumor.ready"
#    }
#    '''

def sv_filing_sep(params):
    
    svinp = params["svinp"]
    prefix = params["prefix"]
    
    outfile = prefix + ".sv_circos.txt"
    lines = []
    with open(svinp, "r") as fr:
        for line in fr:
            if line.split("\t")[0] != "Chr":
                hs1 = line.split("\t")[0].replace("chr", "hs")
                break1  = line.split("\t")[1]
                hs2 = line.split("\t")[4].replace("chr", "hs")
                break2 = line.split("\t")[5]
                lines = [hs1, break1, break1, hs2, break2, break2]

                with open(outfile, "a") as fw:
                    sv_line = "\t".join(lines) + "\n"
                    fw.write(sv_line)
    
    params["plotinfo"]["sv_out"] = outfile
    return params

def sv_filing(jsonfile):

    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    sv_params = sv_filing_sep(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(sv_params, f_w_obj)

#==================for omics platfoorm===================
class svFiling_Worker(jbiotWorker):
    def handle_task(self, key, paramsotWorker):
        self.execMyfunc(sv_filing,params) 

if __name__ == "__main__":
    
    jsonfile = sys.argv[1]
    sv_filing(jsonfile)
