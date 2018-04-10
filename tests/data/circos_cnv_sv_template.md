karyotype = {{ karytotype }}
chromosomes_units = {{ chrom_unit }}

chromosomes_display_default = yes

<<include /lustre/users/zhangxu/miniconda2/1.circos/ideogram.conf>>
<<include /lustre/users/zhangxu/miniconda2/1.circos/ticks.conf>>

<image>

dir = .
file = {{ outfile }}
png = yes
svg = no

# radius of inscribed circle in image
radius = 1500p

angle_offset = -90

auto_alpha_colors = yes
auto_alpha_steps = 5

background = white

</image>

<links>

<link>
file = {{ sv_out }}
radius = 0.60r
color = red
bezier_radius = 0.02r
thickness = 3
</link>

</links>

<plots>

<plot>
type = scatter
file = {{ cnv_out }}
fill_color = vlgreen
stroke_color = black
glyph = circle
glyph_size = 10
max = {{ cnv_max }}
min = {{ cnv_min }}
r0 = 0.62r
r1 = 0.95r

<backgrounds>

<background>
color = vlgreen_a4
</background>

</backgrounds>

<axes>
<axis>
color = lgreen
thickness = 1 
spacing = 0.05r
</axis>

<axis>
color = green
thickness = 4 
position = 2 
</axis>
</axes>

</plot>

</plots>

<<include /lustre/users/zhangxu/miniconda2/etc/colors_fonts_patterns.conf>>
<<include /lustre/users/zhangxu/miniconda2/etc/housekeeping.conf>>
