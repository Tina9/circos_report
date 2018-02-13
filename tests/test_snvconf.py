import sys,os
sys.path.append("../")
import json

from circos_report.snv_circos.snvconf import produce_snv_config as produce_config

with open("data/TempltRendrParms_snv.json", "r") as f:
    circos_input = json.loads(f.read())

def test_pro():

    produce_config(circos_input)

if __name__ == "__main__":

    test_pro()

