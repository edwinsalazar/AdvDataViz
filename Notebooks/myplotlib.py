#!/usr/bin/env python
# coding: utf-8



# Histogram
def hist(data, color="dodgerblue", edgecolor="black", label="Age"):
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()

    ax.hist(data, color=color, edgecolor=edgecolor)

    ax.set_title('Histogram', fontsize=16)
    ax.set_xlabel(label, fontsize=16);



# Boxplot
def boxplot(data, labels=[1], median_color="black", patch_artist=False, box_color=["dodgerblue"]):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize = (5, 3))

    bplot = ax.boxplot(data, patch_artist=patch_artist, 
                             medianprops={"color":median_color, "linewidth":2}, tick_labels=labels)
    
    if patch_artist:
        for patch, color in zip(bplot['boxes'], box_color):
            patch.set_facecolor(color);



# Scatterplot
def scatter(x, y, alpha=.3, size = 200, color="mediumblue"):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.scatter(x=x, y=y, alpha=alpha, s = size, c = color);



# Barplot
def bar(labels, height, color="deepskyblue"):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.bar(x = labels, height=height, color=color, edgecolor="black")



# Pie chart
def pie(labels, values, colors):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize = (15, 5))
    ax.pie(x=values, labels=labels, colors=colors, autopct='%.1f%%',
        wedgeprops = {"edgecolor" : "black", 
                      'linewidth': 1, 
                      'antialiased': True});





