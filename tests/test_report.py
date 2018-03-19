import sys
sys.path.append("../circos_report/reporter")
from report import report

params = {"render_json":"data/report.json",
    "report_template":"data/circos_report_template.md"}

def test_report():

    report(params)

if __name__ == "__main__":

    test_report()
