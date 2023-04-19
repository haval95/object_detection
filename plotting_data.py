from motion_detect import df
from bokeh.plotting import figure, show, output_file

f = figure(x_axis_type="datetime", height=200, title="Motion Graph")

f.yaxis.ticker.desired_num_ticks = 1
f.quad(left=df["Start"], right=df["End"], top=1, bottom=0, color="yellow")

output_file("motion_data.html")

show(f)