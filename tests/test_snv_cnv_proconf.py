import sys
sys.path.append("../circos_report/snv_cnv_anno2conf")
from snv_cnv_anno2conf import main_snv_cnv

params = {"yaml": "test_app.yaml"} 

def test_main_snv_cnv():

    main_snv_cnv(params)

if __name__ == "__main__":

    test_main_snv_cnv()
