# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import matplotlib.pyplot as plt
 
# x axis values
x = [1,2,3,4,5,6]
# corresponding y axis values
y = [2,4,1,5,2,6]
 
# plotting the points 
plt.plot(x, y, color='blue', linestyle='dotted', linewidth = 5,
         marker='*', markerfacecolor='red', markersize=18)
 
# setting x and y axis range
plt.ylim(1,8)
plt.xlim(1,8)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
plt.legend()
# function to show the plot
plt.show()


import matplotlib.pyplot as plt
activities=['apple','samsung','redmi','lenovo']
slices = [3, 7, 8, 6]
colors = ['r', 'y', 'g', 'b']
plt.pie(slices, labels = activities, colors=colors, 
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0),
        radius = 1.2, autopct = '%1.1f%%')
plt.legend()
plt.show()



import matplotlib.pyplot as plt
import numpy as np
 
# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
 
# potting the points
plt.plot(x, y)
 
# function to show the plot
plt.show()

import matplotlib.pyplot as plt
x=[1,3,5,7,9,10,15]
y=[2,4,6,9,11,14,17,]
plt.scatter(x,y,label="scatter",marker="*",color="red",s=30)
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.show()

x = [1,2,3,4,5,6,11,15]
# corresponding y axis values
y = [2,4,1,5,2,6,8,9]
 
# plotting the points 
plt.plot(x, y, color='yellow', linestyle='dashed', linewidth = 5,
         marker='*', markerfacecolor='orange', markersize=18)
 
# setting x and y axis range
plt.ylim(1,20)
plt.xlim(1,20)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
 
# giving a title to my graph
plt.title('Some cool customizations!')
plt.legend()
# function to show the plot
plt.show()

import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1,y1,label="line1",color="red")
x2 = [1,2,3]
y2 = [4,1,3]
plt.plot(x2,y2,label="line2",color="purple")
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title("two line in one")
plt.legend()
plt.show()


import matplotlib.pyplot as plt
x1 = [1,2,3]
y1 = [2,4,1]
plt.plot(x1,y1,label="line1",color="red",linestyle="dotted")
plt.xlabel('x_axis')
plt.ylabel('y_axis')
plt.title("two line in one")
plt.legend()
plt.show()

import matplotlib.pyplot as plt
 
# x-coordinates of left sides of bars 
left = [1, 2, 3, 4, 5]
 
# heights of bars
height = [10, 24, 36, 40, 5]
 
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']
 
# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()



