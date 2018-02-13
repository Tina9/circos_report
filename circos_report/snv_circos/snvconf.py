import os
import config
from jinja2 import Template


def produce_snv_config(loc):
   
    out = "circos.snv.conf"
    with open('/lustre/users/zhangxu/DevWork/circos_report/circos_report/snv_circos/circos_snv_template.md', 'r') as f:
        tmp = f.read()

    template = Template(tmp)
    circos_input = template.render(loc)
        
    with open(out, "w") as output:
        output.write(circos_input)

    return out
