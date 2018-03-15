
#### produce a multi json file --para=1 --mem=2G --docker= --singularity=

    echo '{"outconf": "patient1_circos.multi.conf", "cnvinp": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/22.tumor.ready.cnv.info.anno.txt", "prefix": "patient1", "report_template": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_report_template.md", "svinp": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/22.tumor.ready.mergeavi.anno.txt", "circos_multi_tmp": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_multi_template.md", "snvinp": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/test.mutect2_snv.anno.txt", "plotinfo": {"chrom_unit": 1000000, "species": "/lustre/users/zhangxu/DevWork/circos_report/tests/data/hs_circos.txt", "karytotype": "/lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt"}}' > patient1_transfer.json

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

#### Get the cmd of circos: --para=1 --mem=2G --docker= --singularity=

    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf patient1_circos.multi.conf

#### arrange files --para=1 --mem=2G --docker= --singularity=

    cp patient1_circos.multi.png report

#### produce the needer reporter json file --para=1 --mem=2G --docker= --singularity=

    echo '{"plot_of_circos": ["patient1_circos.multi.png"], "plot_of_text": "circos\u56fe\u7531\u91cc\u5230\u5916\u4f9d\u6b21\u4e3asv,cnv,snp\u548cindel\u7684\u7ed3\u679c"}' > report.json

#### render mapping circos template --para=1 --mem=2G --docker=kongdeju/alpine-dev:stable --singularity=

    /lustre/users/kongdeju/DevWork/jbiot/jbiot/render.py -t /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_report_template.md -j report.json -o circos_report.md

#### md2html circos report  --para=1 --mem=2G --docker=kongdeju/alpine-dev:stable --singularity=

    /lustre/users/kongdeju/DevWork/jbiot/jbiot/md2html.py circos_report.md
