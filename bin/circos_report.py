import sys
import os
import yaml

dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../circos_report")
sys.path.append(dirpath)

from docopt import docopt
from snv_circos.snvconf import produce_snv_config
from cnv_circos.cnvconf import produce_cnv_config
from sv_circos.svconf import produce_sv_config
from reporter.circos import circos
from filing.snv_filing import snv_filing
from filing.snv_count import count_snp, count_del
from filing.cnv_filing import cnv_filing
from filing.sv_filing import sv_filing

### get the template input of circos
def ref_resolution(refe):

	circos = {}
	for key1, value1 in refe.items():
		for key2, value2 in value1.items():
			if key2.lower() == "specie":
				species = value2
			elif key2.lower() == "karytotype":
				circos["karytotype"] = value2
			elif key2.lower() == "chrom_unit":
				circos["chrom_unit"] = value2

	return species, circos

def main_circos(tmp):

	for k1,v1 in tmp.items():
		if k1.lower() == "snv":
			for k2,v2 in v1.items():
				snvinput = v2
				prefix = ".".join(snvinput.split("/")[-1].split(".")[:-1])

				### get the circos dict
				circos_species, circos_dict = ref_resolution(ref)

				### make the file meet the input of circos
				snv_snp, snv_del = snv_filing(snvinput, prefix)
				circos_dict["snv"] = count_snp(circos_species, snv_snp, prefix)
				circos_dict["del"] = count_del(circos_species, snv_del, prefix)

				### get the snv circos.conf
				#### produce the snv circos file
				circos_kind = produce_snv_config(circos_dict)

				#### execute the circos.conf of the file
				circos(circos_kind)

		if k1.lower() == "cnv":
			for k2,v2 in v1.items():
				cnvinput = v2
				prefix = ".".join(cnvinput.split("/")[-1].split(".")[:-1])

				### get the circos dict
				circos_species, circos_dict = ref_resolution(ref)

				### make the file meet the input of circos
				circos_dict["cnv"] = cnv_filing(cnvinput, prefix)

				### get the cnv circos.conf
				circos_kind = produce_cnv_config(circos_dict)
				circos(circos_kind)

		if k1.lower() == "sv":
			for k2,v2 in v1.items():
				svinput = v2
				prefix = ".".join(svinput.split("/")[-1].split(".")[:-1])

				### get the circos dict
				circos_species, circos_dict = ref_resolution(ref)

				### make the file meet the input of circos
				circos_dict["SV"] = sv_filing(svinput, prefix)

				### get the sv circos.conf
				circos_kind = produce_sv_config(circos_dict)
				circos(circos_kind)

if __name__ == "__main__":
    usage= """
Usage:
    circos_report.py -i <input> -c <parameter>

Options:
    -h --help                           print this screen
    -i <input> --input=<input>          bam file, yamal format
    -c <parms> --parameter=<parms>      parameters
"""


    args = docopt(usage)
    tmpfile = args['--input']
    refile = args['--parameter']

	#### read in tmpfile
	tmpfi = open(tmpfile, "r")
	tmpe = yaml.load(tmpfi.read())

	#### read in ref file
	refi = open(refile, "r")
	ref = yaml.load(refi.read())

	main_circos(tmpe)
