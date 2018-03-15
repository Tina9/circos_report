#try:
#    from config import sys
#    from config import os
#    from config import json
#    from config import jbiot
#    from config import jinja2
#except:
import sys
import os
import json
import jbiot
import jinja2

#from jbiot import jbiotWorker
from jinja2 import Template

def cal_MM(finame):

    # make a list to save the value of the file
    value = []

    with open(finame, 'r') as f:
        for line in f:
            value.append(int(line.rstrip().split("\t")[3]))
    min_value = min(value)
    max_value = max(value)

    return min_value, max_value

def cal_snv_MM(params):

    snp_file = params['plotinfo']['snp_out']
    indel_file = params['plotinfo']['indel_out']

    snp_min, snp_max = cal_MM(snp_file)
    indel_min, indel_max = cal_MM(indel_file)

    params['plotinfo']["snp_min"] = snp_min
    params['plotinfo']["snp_max"] = snp_max
    params['plotinfo']["indel_min"] = indel_min
    params['plotinfo']["indel_max"] = indel_max

    return params

def params_filing(params):

    params = cal_snv_MM(params)

    params['outconf'] = params['prefix'] + '_circos.snv.sv.conf'
    params['plotinfo']['outfile'] = params['prefix'] + '_circos.snv.sv.png'

    return params

def produce_config(pconf_params):
    
    params = params_filing(pconf_params)

    out = params['outconf']
    tpl = params['circos_snv_sv_tmp']
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
