import os
import config
from jinja2 import Template


def produce_config(loc):
    
    with open('/lustre/users/zhangxu/DevWork/circos_report/circos_report/reporter/circos_template.md', 'r') as f:
        tmp = f.read()

    template = Template(tmp)
    circos_input = template.render(loc)
        
    with open("circos.conf", "w") as output:
        output.write(circos_input)
    
