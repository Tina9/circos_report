try:
    import config
except:
    pass

from jbiot import jbiotWorker
from jbiot import log
from jbiot import yamladd
import yaml

def data_cycle(indict):

    circos_res = indict["circos_res"]
    pngs = []
    for patient,value in circos_res.items():
        png = value['png']
        pngs.append(png)

    return pngs

def arrange(params):
    """ circos_report arrange output files

    Args:
        params: indict , key is `yaml`, value in yaml file::

            circos_res:
                {
                    patient1: saved circos' info of the patient
                        {
                            conf: the conf file of the specific patient
                            png: the png file of the specific patient
                        }    
                }

    Returns:
        dict : key is `yaml`, value is the path of yaml file

    """

    # handle input
    yamlin = params["yaml"]
    indict = yaml.load(open(yamlin).read())
    pngs = data_cycle(indict)

    # process cmd
    log.move(pngs, "report/circos")

    #handle out
    outdict = {}
    outdict["pngs"] = pngs
    yamlout = yamladd(yamlin,outdict)
    return yamlout

class circos_reportArranger(jbiotWorker):
    def handle_task(self,key,params):
        self.execMyfunc(arrange,params)
