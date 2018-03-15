try:
    from config import os
    from config import sys
    from config import json
except:
    import os
    import sys
    import json

from jbiot import jbiotWorker

############################################################################################################
################## convert the output of cnvkit into the circos input ######################################
############################################################################################################

def cnv_filing_count(params):
    '''params include keys as follows:
        {
        "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt",
        "prefix": "22.tumor.ready",
         }    
    '''

    cnvinp = params["cnvinp"]
    prefix = params["prefix"]

    out_file = prefix + ".cnv_circos.txt"
    lines = []
    with open(cnvinp, "r") as cnv:
        for line in cnv:
            if line.split("\t")[0] != "Chr":
                hs = line.split("\t")[0].replace("chr", "hs")
                start = line.split("\t")[1] 
                end = line.split("\t")[2]
                cp = line.split("\t")[6]
                lines = [hs, start, end, cp]
                with open(out_file, "a") as fw:
                    cnv_line = "\t".join(lines) + "\n"
                    fw.write(cnv_line)

    params["plotinfo"]["cnv_out"] = out_file
    return params

def cnv_filing(jsonfile):

    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    cnv_params = cnv_filing_count(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(cnv_params, f_w_obj)

#================for omics platfoorm===================
class cnvFiling_Worker(jbiotWorker):
    def handle_task(self, key, paramsotWorker):
        self.execMyfunc(cnv_filing,params)

if __name__ == "__main__":

    jsonfile = sys.argv[1]
    cnv_filing(jsonfile)

