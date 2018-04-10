import sys
sys.path.append("../circos_report/snv_anno2conf")
from snv_anno2conf import main_snv

tarfile = {"yaml": "test_app.yaml"}

def test_main_snp():

    res = main_snv(tarfile)
    print res

if __name__ == "__main__":

    test_main_snp()
