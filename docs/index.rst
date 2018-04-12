=============
circos_report
=============

This is the documentation of **circos_report**.


.. Note::

    code reviewed by deju @ 2018-4-12


Installation
============
use git to clone code::

    git clone git@123.57.226.13:/expan/DevRepos/circos_report.git

Usage
=====

just type circos_report.py -h::

    Usage:
        cnv_report.py -c <parameter>
    
    Options:
        -c, --conf <params>    params file for soft in yaml format

Here is a sample yaml file which the following keys are needed::

    cnv_annos: 
        patient1: 22.tumor.ready.cnv.info.anno.txt
    sv_annos: 
        patient1: patient1.mergeavi.anno.txt
    snv_annos: 
        patient1: /lustre/users/zhangxu/DevWork/circos_report/tests/data/test.mutect2_snv.anno.txt
    circos_chrom_unit: 1000000
    circos_cnv_sv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_cnv_sv_template.md
    circos_cnv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_cnv_template.md
    circos_karytotype: /lustre/users/zhangxu/miniconda2/data/karyotype/karyotype.human.hg19.txt
    circos_multi_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_multi_template.md
    circos_report_template: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_report_template.md
    circos_snv_cnv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_snv_cnv_template.md
    circos_snv_sv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_snv_sv_template.md
    circos_snv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_snv_template.md
    circos_species: /lustre/users/zhangxu/DevWork/circos_report/tests/data/hs_circos.txt
    circos_sv_tmp: /lustre/users/zhangxu/DevWork/circos_report/tests/data/circos_sv_template.md

Contents
========

.. toctree::
   :maxdepth: 2

   License <license>
   Authors <authors>
   Changelog <changes>
   Module Reference <api/modules>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
