import sys,os
sys.path.append("../")
from circos_report.reporter.report import report

params = {"yaml":"data/test_app.yaml"}

def test_report():
    report(params)

if __name__ == '__main__':
    test_report()
