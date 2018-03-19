import sys
sys.path.append("../circos_report/arranger")
from arranger import arr_main

params = {"pngs": ["patient1_circos.multi.png"]}

def test_arranger():

    arr_main(params)
    
if __name__ == "__main__":

    test_arranger()
