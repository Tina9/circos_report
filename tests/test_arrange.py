import sys
sys.path.append("../")
from circos_report.arranger.arrange import arrange

params = {"yaml": "test_app.yaml"}

def test_arrange():

    arrange(params)

if __name__ == "__main__":

    test_arrange()
