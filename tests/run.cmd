
#### get the snp file of circos: --para=1 --mem=2G --docker=

    /lustre/common/softs/bin/bedtools intersect -a /lustre/users/zhangxu/DevWork/circos_report/circos_report/filing/hs_circos.txt -b patient1.mutect2_snv.anno.snp_snp.txt -wa -c > patient1.mutect2_snv.anno.snp_circos.txt
    /lustre/common/softs/bin/bedtools intersect -a /lustre/users/zhangxu/DevWork/circos_report/circos_report/filing/hs_circos.txt -b patient1.mutect2_snv.anno.snp_snp.txt -wa -c > patient1.mutect2_snv.anno.snp_circos.txt

#### get the del file of circos: --para=1 --mem=2G --docker=

    /lustre/common/softs/bin/bedtools intersect -a /lustre/users/zhangxu/DevWork/circos_report/circos_report/filing/hs_circos.txt -b patient1.mutect2_snv.anno.del_snp.txt -wa -c > patient1.mutect2_snv.anno.del_circos.txt
    /lustre/common/softs/bin/bedtools intersect -a /lustre/users/zhangxu/DevWork/circos_report/circos_report/filing/hs_circos.txt -b patient1.mutect2_snv.anno.del_snp.txt -wa -c > patient1.mutect2_snv.anno.del_circos.txt

#### Get the cmd of circos: --para=1 --mem=2G --docker=

    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.snv.conf
    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.cnv.conf
    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.sv.conf
    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.snv.conf
    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.cnv.conf
    perl /lustre/users/zhangxu/miniconda2/bin/circos -conf circos.sv.conf
