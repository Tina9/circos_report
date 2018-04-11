import sys
sys.path.append("../circos_report/cnv_anno2conf")
from cnv_anno2conf import main_cnv


tarfile = {"yaml": "data/test_app.yaml"}

def test_main_cnv():
    main_cnv(tarfile)

if __name__ == "__main__":
    test_main_cnv()

