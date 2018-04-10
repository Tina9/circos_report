karyotype = {{ karytotype }}
chromosomes_units = {{ chrom_unit }}

chromosomes_display_default = yes

<<include /lustre/users/zhangxu/miniconda2/1.circos/ideogram.conf>>
<<include /lustre/users/zhangxu/miniconda2/1.circos/ticks.conf>>

<image>

dir   = . 
#dir  = conf(configdir)
file  = {{ outfile }}
png   = yes
svg   = no

# radius of inscribed circle in image
radius = 1500p

angle_offset = -90

#angle_orientation = counterclockwise

auto_alpha_colors = yes
auto_alpha_steps  = 5

background = white

</image>

<links>

<link>
file = {{ sv_out }}
radius = 0.95r
color = red
bezier_radius = 0.2r
thickness = 3
</link>

</links>

<<include /lustre/users/zhangxu/miniconda2/etc/colors_fonts_patterns.conf>>
<<include /lustre/users/zhangxu/miniconda2/etc/housekeeping.conf>>

