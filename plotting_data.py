from motion_detect import df
from bokeh.plotting import figure, show, output_file
from bokeh.models  import HoverTool, ColumnDataSource

f = figure(x_axis_type="datetime", height=200, title="Motion Graph")

f.yaxis.ticker.desired_num_ticks = 1

df["Start_str"] = df["Start"].dt.strftime("%Y-%m-%D %H:%M:%S")
df["End_str"] = df["End"].dt.strftime("%Y-%m-%D %H:%M:%S")

col_data_source= ColumnDataSource(df)
f.quad(left="Start", right="End", top=1, bottom=0, color="yellow", source=col_data_source)


hover = HoverTool(tooltips=[("Start: ", "@Start_str"), ("End: ", "@End_str")])
f.add_tools(hover)

output_file("motion_data.html")

show(f)