import sys,os
sys.path.append("../circos_report/sv_circos")
import json

from svconf import produce_config

with open("/lustre/users/zhangxu/DevWork/circos_report/circos_report/reporter/TempltRendrParms.json", "r") as f:
    circos_input = json.loads(f.read())

def test_pro():

    produce_config(circos_input)

if __name__ == "__main__":

    test_pro()

