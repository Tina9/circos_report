import sys,os
sys.path.append("../")
import json

from circos_report.cnv_circos.cnvconf import produce_config

with open("TempltRendrParms_cnv.json", "r") as f:
    circos_input = json.loads(f.read())

def test_pro():

    produce_config(circos_input)

if __name__ == "__main__":

    test_pro()

