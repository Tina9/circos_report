karyotype = {{ karytotype }}
chromosomes_units = {{ chrom_unit }}

chromosomes_display_default = yes


<<include /lustre/users/zhangxu/miniconda2/1.circos/ideogram.conf>>
<<include /lustre/users/zhangxu/miniconda2/1.circos/ticks.conf>>

<image>
<<include /lustre/users/zhangxu/miniconda2/etc/image.conf>>
</image>

<plots>

<plot>
type = line
thickness = 2

max_gap = 1u
file = {{ depth }}
color = black
min = 0
max = 1.0
r0 = 1.005r
r1 = 1.05r
fill_color = vdred
</plot>

<plot>
type = line
thickness = 2
max_gap = 1u
file = {{ snv }}
color = black
min = 0
max = 1.0
r0 = 0.5r
r1 = 0.8r
fill_color = vdgreen
</plot>

</plots>

<<include /lustre/users/zhangxu/miniconda2/etc/colors_fonts_patterns.conf>>
<<include /lustre/users/zhangxu/miniconda2/etc/housekeeping.conf>>
