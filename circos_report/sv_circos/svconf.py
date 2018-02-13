import os
import config
from jinja2 import Template


def produce_sv_config(loc):
   
    out = "circos.sv.conf"
    with open('/lustre/users/zhangxu/DevWork/circos_report/circos_report/sv_circos/circos_sv_template.md', 'r') as f:
        tmp = f.read()

    template = Template(tmp)
    circos_input = template.render(loc)
        
    with open(out, "w") as output:
        output.write(circos_input)
    
    return out
