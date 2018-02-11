import sys
import os
import yaml

dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../circos_report")
sys.path.append(dirpath)

from docopt import docopt
from snv_circos.snvconf import produce_snv_config
from cnv_circos.cnvconf import produce_cnv_config
from sv_circos.svconf import produce_sv_config
from reporter.circos import circos

def snv_circos_report():

    produce_snv_config(circos_input)

def cnv_circos_report():

    produce_cnv_config(circos_input)

def sv_circos_report():

    produce_sv_config(circos_input)
    
def draw_circos(infile, way):

    if way == "snv":
        snv_circos_report()
    elif way == "cnv":
        cnv_circos_report()
    elif way == "sv":
        sv_circos_report()

    circos()

if __name__ == "__main__":
    usage= """
Usage:
    cnv_report.py -i <input> -c <parameter>

Options:
    -h --help                           print this screen
    -i <input> --input=<input>          yamal format
    -c <parms> --parameter=<parms>      cnv, sv or snv
"""
    args = docopt(usage)
    yamlfile = args['--input']
    ways = args['--parameter']

    with open(yamlfile, 'r') as f:
        circos_input = yaml.load(f.read())

    draw_circos(circos_input, ways)

