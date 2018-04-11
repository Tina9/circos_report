import sys
sys.path.append("../circos_report/snv_sv_anno2conf")
from snv_sv_anno2conf import main_snv_sv

params = {"yaml": "data/test_app.yaml"}

def test_main_snv_sv():

    main_snv_sv(params)

if __name__ == "__main__":

    test_main_snv_sv()
