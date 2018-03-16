try:
    from config import sys
    from config import os
    from config import json
    from config import jbiot
    from config import jinja2
except:
    import os
    import sys
    import json
    import jbiot
    import jinja2

from jbiot import jbiotWorker
from jinja2 import Template

##############################################################################
################### produce the conf file of sv ##############################
##############################################################################

#    '''params include keys as follows:
#    {
#        "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
#        "outconf": "patient1_circos.sv.conf",
#        "prefix": "patient1",
#        "plotinfo": 
#            {"karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt", 
#            "sv_out": "patient1.sv_circos.txt", 
#            "chrom_unit": 1000000, 
#            "species": "data/hs_circos.txt", 
#            "circos_sv_rep_tmp": "data/cirSV_template.md"}, 
#            "prefix": "patient1", 
#            "svinp": "data/22.tumor.ready.mergeavi.anno.txt", 
#            "circos_sv_tmp": "data/circos_sv_template.md"}
#    '''
def params_filing(params):

    params['outconf'] = params['prefix'] + '_circos.sv.conf'
    params['plotinfo']['outfile'] = params['prefix'] + "_circos.sv.png"

    return params

#    '''get the conf file of circos script
#
#    Args:
#        dict: including the needed params
#
#    Return:
#        dict: a dict including circos needed params
#   
#     Dict is as follows:
#        {
#        "outconf": "patient1_circos.sv.conf",
#        "plotinfo":
#            {"karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt",
#            "sv_out": "patient1.sv_circos.txt",
#            "chrom_unit": 1000000,
#            "outfile": "patient1_circos.sv.png"
#            "species": "data/hs_circos.txt",
#            "circos_sv_rep_tmp": "data/cirSV_template.md"},
#        "prefix": "patient1",
#        "svinp": "data/22.tumor.ready.mergeavi.anno.txt",
#        "circos_sv_tmp": "data/circos_sv_template.md"}
#    '''

def produce_config(pconf_params):

    params = params_filing(pconf_params)

    out = params['outconf']
    tpl = params['circos_sv_tmp']
    loc = params['plotinfo']

    with open(tpl, 'r') as f_obj:
        temp = f_obj.read()
    template = Template(temp)
    circos_input = template.render(loc)

    with open(out, 'w') as f_w_obj:
        f_w_obj.write(circos_input)

    return params

if __name__ == "__main__":

    jsonfile = sys.argv[1]
    with open(jsonfile, 'r') as f_obj:
        params = json.load(f_obj)

    params = produce_config(params)

    with open(jsonfile, 'w') as f_w_obj:
        json.dump(params, f_w_obj)
