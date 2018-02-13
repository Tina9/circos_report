import sys,os
sys.path.append("../circos_report")
import json

from cnv_circos.cnvconf import produce_cnv_config

with open("data/TempltRendrParms_cnv.json", "r") as f:
    circos_input = json.loads(f.read())

def test_pro():

    produce_cnv_config(circos_input)

if __name__ == "__main__":

    test_pro()

