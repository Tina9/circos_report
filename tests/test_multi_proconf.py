import sys 
sys.path.append("../circos_report/multi_anno2conf")
from multi_anno2conf import main_multi

params = {"yaml": "data/test_app.yaml"}

def test_main_multi():

    main_multi(params)

if __name__ == "__main__":

    test_main_multi()

