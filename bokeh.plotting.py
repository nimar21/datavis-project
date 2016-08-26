
# coding: utf-8

# # Data Visualisation with Bokeh 

# Bokeh is a Python interactive visualisation library designed for presentation on modern web browsers. The library’s main aims are as follows:
# 
# •	To provide elegant, concise construction of basic exploratory and advanced custom graphics.
# 
# •	To provide high-performance interactivity over very large or streaming data sets. 
# 
# To offer variety in the level of simplicity or complexity offered to the different users of Bokeh, three interface levels are exposed to the user:
# 
# 1.	bokeh.models: A low-level interface which provides the most flexibility to application developers.
# 2.	bokeh.plotting: An intermediate-level interface which is focused on composing visual glyphs. 
# 3.	bokeh.charts: A high-level interface designed to build complex statistical plots in a quick and simple manner. 
# 
# I am going to focus on the bokeh.plotting interface as this interface provides a nice middleground between the very high-level and very low-level. 

# ## bokeh.plotting

# As mentioned above, the bokeh.plotting interface is a mid-level interface in the Bokeh library. It is focused on the visual glyphs (explored further below) that represent the user's data, while the putting together of plots with sensible default axes, grids, and tools is handled by Bokeh. 
# 
# The key class in the bokeh.plotting interface is the <i>Figure</i> class, which is a subclass of the <i>Plot</i> class. It contains methods for adding glyphs to the plot and also composes default axes, grids, and tools in the proper way without any extra effort. A Figure object can be created by calling the figure() function.
# 
# Before you start any plotting, you must import the parts of the bokeh.plotting interface that you require for your program. For our example, we will require 3 methods:

# In[1]:

from bokeh.plotting import figure, output_notebook, show


# Once you have finished your imports, the basic steps to creating plots with the bokeh.plotting interface are as follows:
# -	Define the data that you are going to use to specify points on the plot. For our example, we will just assign some aribtrary numbers to be the x and y points, however in real life cases, you will naturally be using more meaningful data:

# In[2]:

x_points = [1,2,3,4,5]
y_points = [2,3,4,1,1]


# - Define where you want Bokeh to generate output. The two output methods we will be looking at are:
# 
# >  <b>output_notebook():</b>  Displays the visualisations in Jupyter notebook cells.
# 
# >  <b>output_file(filename):</b>  Generates a standalone, named HTML document which displays the Bokeh visualisation. This method's only mandatory argument is the name of the HTML document (in string form) that the user wishes to save the output to (e.g. "test.html").  Its optional arguments are <i>title, autosave, mode,</i> and <i>root_dir</i>.
# 
# Both of the above methods actually belong to the <i>bokeh.io</i> interface but can also be imported from <i>bokeh.plotting</i> for the convenience of the user. Learn more about the methods and the default values of their optional arguments here: http://bokeh.pydata.org/en/latest/docs/reference/io.html.
# 

# In[3]:

output_notebook()


# - Create a <i>Figure</i> object by calling the <i>figure()</i> method and assign it to a variable. Add some extras to your plot such as a title, tools, and axes labels by making use of the several optional parameters you can pass in to this method. To view the entire list of stylistic attributes you can include in the <i>figure()</i> method, take a look here: http://bokeh.pydata.org/en/latest/docs/user_guide/styling.html#plots; or if you would like to learn more about different ways of configuring the plot's toolbar, see here: http://bokeh.pydata.org/en/0.11.1/docs/user_guide/tools.html (<i>Note:</i> Since the <i>Figure</i> class is a sub-class of <i>Plot</i>, attributes and methods of plots are inherited.)

# In[4]:

plot = figure(title="Our Example Plot", plot_height=500, plot_width=500, x_axis_label='Time', y_axis_label='Temperature')


# If, at a later point, you want to add or change some attributes, you can do so as shown below:

# In[5]:

plot.title_text_alpha=0.8
plot.border_fill_color='whitesmoke'


# The next step is the most fundamental aspect of the <i>bokeh.plotting</i> interface: adding glyphs to the above plot using one or more of the many glyph-generating methods offered by the <i>Figure</i> class. 
# > <b>Key Definition:</b> A <i>glyph</i> is a basic building block of Bokeh plots. Examples of glyphs include scatter markers, lines, patches, and wedges, amongst others. 
# 
# This ability to add various types of glyphs simply using methods is one of the most attractive aspects of the <i>bokeh.plotting</i> interface. It's simple, quick, and effective.
# For our first example, I am going to show you how to add a line glyph to a plot:

# In[6]:

# Add a red line which passes through the co-ordinates assigned to the variables 'x_points' and 'y_points' above 
plot.line(x_points, y_points, line_width=3, line_color="red", line_alpha=0.5)


# Finally, call either the <i>show()</i> or <i>save()</i> method, depending on whether you want to save and display the plot immediately or just save it. In our example, we will use <i>show()</i> as we want to be able to see our results. 

# In[7]:

show(plot)


# Above is the output of our program which displays a simple line graph, the co-ordinates of which correspond to those that we passed into the <i>line()</i> method of our <i>Figure</i> object.
# Let's add some square-shaped scatter markers into our plot using the <i>square()</i> method and then display it again using the <i>show()</i> method.

# In[9]:

plot.square([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="olive", alpha=0.5)
show(plot)


# Let's also add a patch then display it again:

# In[14]:

plot.patch([3, 3.5, 4, 4.5], [5, 7, 5, 6], alpha=0.5, line_width=2)
show(plot)


# And finally some wedges:

# In[16]:

plot.wedge(x=[1, 2, 3], y=[1, 2, 3], radius=0.2, start_angle=0.4, end_angle=4.8, 
           color="green", alpha=0.6, direction="clock")
show(plot)


# As you can see, there are a number of different types of glyphs that can be added to Bokeh plots to represent your data. They include:
# 
#     - asterisk()
#     - circle()
#     - circle_cross()
#     - circle_x()
#     - cross()
#     - diamond()
#     - diamond_cross()
#     - inverted_triangle()
#     - square()
#     - square_cross()
#     - square_x()
#     - triangle()
#     - x()

# For a comprehensive description of the types of <i>parameters, keyword arguments</i>, and <i>other parameters</i> of each of the above glyphs, please refer to the online documentation for the <i>bokeh.plotting</i> interface here: http://bokeh.pydata.org/en/latest/docs/reference/plotting.html
# 
# One slightly different example of glyph-plotting in this interface is the idea of using a single method for plotting multiple glyphs. An example of this is the <i>multi_line()</i> method which allows the user to add more than one <i>line</i> glyph by passing in a <i>list of lists</i> for the set of x co-ordinates and y co-ordinates for all lines. Similarly, the lines' attributes are passed in as a list of values which correspond to each line. This is illustrated below: 

# In[19]:

#Create new plot
plot1 = figure(title="Multi-Line Example", plot_height=500, plot_width=500, x_axis_label='Time', y_axis_label='Temperature')

#Add muliple lines at once using multi_line() method:
plot1.multi_line([[1,2,3],[4,5,6]], [[1,2,3],[6,5,4]], line_width=[3, 5], line_color=["red", "blue"], line_alpha=[0.5, 0.7])

show(plot1)


# Another example of a multi-glyph method is <i>patches()</i> which generates multiple patches.
# > <b>Note:</b> <i>NaN</i> values can be passed to <i>line, multi_line, patch,</i> and <i>patches</i> glyphs. Doing so creates single logical objects which just have disjoint components when rendered. This is illustrated below:

# In[26]:

#Create new plot
plot2 = figure(title="NaN Example", plot_height=500, plot_width=500, x_axis_label='Time', y_axis_label='Temperature')

#Add a line which passes through a NaN co-ordinate:
nan = float('nan')
plot2.line([1, 2, 3, nan, 4, 5], [6, 7, 5, 3, 4, 5], line_width=3, line_color="orange", line_alpha=0.5)

show(plot2)


# Bokeh automatically sets the data bounds of your plot according to the data you are examining. If you want to explicitly set the range yourself, there are two ways of doing so:
# 1. Use a <i>Range1d</i> object to give the start and end points for <i>x_range</i> or <i>y_range</i>. This object must be imported in from the <i>bokeh.models</i> interface.
# 2. More conveniently, pass these values in through parameters of the same name in the <i>figure()</i> method.
# See below for a demonstration of both approaches: 

# In[30]:

from bokeh.plotting import figure, output_notebook, show
from bokeh.models import Range1d

output_notebook()

#Set x range using 'x_range' parameter of the figure() method 
p = figure(title="My Plot", plot_width=400, plot_height=400, x_range=(0, 20))

#Set y range using Range1d object
p.y_range = Range1d(0, 15)

#Add some triangle-shaped scatter markers
p.triangle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)


# You may not always want to use the default axis types generated by Bokeh when you create a plot. For example, if you want the labels of the y-axis to be letters rather than numbers, you can do so as follows:  

# In[33]:

factors = ["a", "b", "c", "d", "e", "f", "g", "h"]
x_points = [32, 10, 73, 22, 18, 42, 66, 54]

output_notebook()

plot3 = figure(y_range=factors, plot_width=400, plot_height=400)

plot3.square(x_points, factors, size=10, fill_color="yellow", line_color="green", line_width=3)

show(plot3)


# Hopefully this notebook has given an insightful overview of the bokeh library. 
# 
# For more information on other Python data visualisation libraries and their application, see the other notebooks in this set.
