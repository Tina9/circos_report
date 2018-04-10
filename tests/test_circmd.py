import sys
sys.path.append("../circos_report/circmd")
from circmd import circmd

tarfile = {"yaml": "test_app.yaml"}

def test_circosCMD():

    circmd(tarfile)

if __name__ == "__main__":

    test_circosCMD()
