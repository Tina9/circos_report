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
type = scatter
file = {{ cnv }}
fill_color = grey
stroke_color = black
glyph = circle
glyph_size = 10
max = 8
min = 0
r0 = 0.20r
r1 = 0.95r

<backgrounds>

<background>
color = vlgreen_a4
y0  = 0.95r
</background>

<background>
color = vlgreen_a4
y0 = 0.75r
</background>

<background>
color = vlgreen_a4
y0  = 0.55r
</background>

<background>
color = vlgreen_a4
y0  = 0.25r
</background>

<background>
color = vlgreen_a4
y0  = 0.05r
</background>

</backgrounds>

</plot>

</plots>

<<include /lustre/users/zhangxu/miniconda2/etc/colors_fonts_patterns.conf>>
<<include /lustre/users/zhangxu/miniconda2/etc/housekeeping.conf>>
