karyotype = {{ karytotype }}
chromosomes_units = {{ chrom_unit }}

chromosomes_display_default = yes


<<include /lustre/users/zhangxu/miniconda2/1.circos/ideogram.conf>>
<<include /lustre/users/zhangxu/miniconda2/1.circos/ticks.conf>>

<image>

dir   = . 
file  = {{ outfile }}
png   = yes
svg   = no

# radius of inscribed circle in image
radius = 1500p

angle_offset = -90

auto_alpha_colors = yes
auto_alpha_steps  = 5

background = white

</image>

<plots>

<plot>
type = histogram
file = {{ indel_out }}
color = red
min = {{ indel_min }}
max = {{ indel_max }}
r0 = 0.65r
r1 = 0.95r
thickness = 10p
fill_under = yes
fill_color = red
orientation = out

<axes>
show = data
thickness = 2
color = grey_a3
<axis>
spacing = 0.1r
</axis>
</axes>

</plot>

<plot>
type = histogram
file = {{ snp_out }}
color = green
min = {{ snp_min }}
max = {{ snp_max }}
r0 = 0.30r
r1 = 0.60r
thickness = 10p
fill_under = yes
fill_color = green
orientation = in

<axes>
show = data
thickness = 2
color = grey_a3
<axis> 
spacing = 0.1r
</axis>
</axes>

</plot>

</plots>

<<include /lustre/users/zhangxu/miniconda2/etc/colors_fonts_patterns.conf>>
<<include /lustre/users/zhangxu/miniconda2/etc/housekeeping.conf>>
