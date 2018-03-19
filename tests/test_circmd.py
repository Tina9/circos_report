import sys
sys.path.append("../circos_report/circos_cmd")
from circmd import circosCMD

params = {"outconf": "data/patient1_circos.multi.conf",}

def test_circosCMD():

    circosCMD(params)

if __name__ == "__main__":

    test_circosCMD()
