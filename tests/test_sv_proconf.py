import sys
sys.path.append("../circos_report/sv_anno2conf")
from sv_anno2conf import main_sv

tarfile = {"yaml": "data/test_app.yaml"}

def test_main_sv():
    main_sv(tarfile)

if __name__ == "__main__":
    test_main_sv() 
