import bokeh
from bokeh.sampledata.stocks import AAPL,FB,MSFT,GOOG
from bokeh.plotting import figure,output_file, show
import numpy as np

graph = figure(x_axis_type="datetime",title="Stock Closing Price")
graph.xaxis.axis_label = "Date"
graph.yaxis.axis_label = "Price (in USD)"

#Plotting the line graph for Apple
x_axis_coordinates = np.array(AAPL['date'],dtype = np.datetime64)
y_axis_coordinates = AAPL['adj_close']
color = "blue"
legend_label = "APPL"
graph.line(x_axis_coordinates,y_axis_coordinates,color=color,legend_label=legend_label)

#Plotting the line graph for Facebook
x_axis_coordinates = np.array(FB['date'],dtype = np.datetime64)
y_axis_coordinates = FB['adj_close']
color = "black"
legend_label = "FB"
graph.line(x_axis_coordinates,y_axis_coordinates,color=color,legend_label=legend_label)

#Plotting the line graph for Google
x_axis_coordinates = np.array(GOOG['date'],dtype = np.datetime64)
y_axis_coordinates = GOOG['adj_close']
color = "orange"
legend_label = "GOOG"
graph.line(x_axis_coordinates,y_axis_coordinates,color=color,legend_label=legend_label)

#Plotting the line graph for Microsoft
x_axis_coordinates = np.array(MSFT['date'],dtype = np.datetime64)
y_axis_coordinates = MSFT['adj_close']
color = "yellow"
legend_label = "MSFT"
graph.line(x_axis_coordinates,y_axis_coordinates,color=color,legend_label=legend_label)



#Relocate the legend to the left side of the screen
graph.legend.location="top_left"

#display the model
show(graph)