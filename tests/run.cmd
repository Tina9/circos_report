
#### produce a multi json file --para=1 --mem=2G --docker= --singularity=

    echo '{"outconf": "patient1_circos.multi.conf", "circos_multi_tmp": "data/circos_multi_template.md", "snvinp": "data/test.mutect2_snv.anno.txt", "circos_report_template": "data/circos_report_template.md", "plotinfo": {"chrom_unit": 1000000, "species": "data/hs_circos.txt", "karytotype": "data/karyotype.human.hg19.txt"}, "prefix": "patient1", "svinp": "data/22.tumor.ready.mergeavi.anno.txt", "cnvinp": "data/22.tumor.ready.cnv.info.anno.txt"}' > patient1_transfer.json

#### use the snv_filing script to get the separated file --para=1 --mem=2G --docker= --singularity=

    python /lustre/users/zhangxu/DevWork/circos_report/circos_report/multi_anno2conf/snv_filing.py patient1_transfer.json

#### use the snv_count script to get the counted file --para=1 --mem=2G --docker= --singularity=

    python /lustre/users/zhangxu/DevWork/circos_report/circos_report/multi_anno2conf/snv_count.py patient1_transfer.json

#### use the cnv_filing script to calculate the MM value --para=1 --mem=2G --docker= --singularity=

    python /lustre/users/zhangxu/DevWork/circos_report/circos_report/multi_anno2conf/cnv_filing.py patient1_transfer.json

#### use the sv_filing script to calculate the MM value --para=1 --mem=2G --docker= --singularity=

    python /lustre/users/zhangxu/DevWork/circos_report/circos_report/multi_anno2conf/sv_filing.py patient1_transfer.json

#### get the conf file of circos --para=1 --mem=2G --docker= --singularity=

    python /lustre/users/zhangxu/DevWork/circos_report/circos_report/multi_anno2conf/multi_proconf.py patient1_transfer.json
