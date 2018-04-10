import sys 
sys.path.append("../circos_report/cnv_sv_anno2conf")
from cnv_sv_anno2conf import main_cnv_sv

params = {"yaml": "test_app.yaml"}

def test_main_cnv_sv():

    main_cnv_sv(params)

if __name__ == "__main__":

    test_main_cnv_sv()

