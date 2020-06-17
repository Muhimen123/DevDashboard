from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import csv


plt.style.use('fivethirtyeight')


def graph_bar():
    data = pd.read_csv('data.csv')
    views = list(data['Views'])[::-1]
    comments = list(data['Comments'])[::-1]
    reactions = list(data['Reactions'])[::-1]

    x_axis = np.arange(len(views))
    x = [i for i in range(len(views))]
    width = 0.30

    plt.title("Histogram for Views, comments, reactions")
    plt.xticks(ticks=x)
    plt.bar(x_axis, views, width=width, label='TotalViews')
    plt.bar(x_axis - width, comments, width=width, label="TotalComments")
    plt.bar(x_axis + width, reactions, width=width, label="TotalReactins")

    plt.xlabel("Post numbers")
    plt.ylabel("Popularity")
    plt.legend()
    plt.show()


def graph_bar_filter(cmd):
    data = pd.read_csv('data.csv')
    cmd = cmd.replace('graph-bar-', '')
    cmd = cmd.split('-')
    values = []
    for attributes in cmd:
        values.append(list(data[attributes.title()][::-1]))

    x_axis = np.arange(len(values[0]))
    x_ticks = [i for i in range(len(values[0]))]

    width = 0.30

    plt.xticks(ticks=x_ticks)
    tit = ''

    for i in range(len(values)):
        plt.bar(x_axis + width * i, values[i], label=cmd[i], width=width)
        tit += cmd[i] + ' '

    plt.title(f"Histrogram of {tit}")
    plt.xlabel("Post numbers")
    plt.ylabel("Popularity")
    plt.legend()
    plt.show()


def graph_bar_tags():
    all_tags = []
    tag_per_views = []

    with open('data.csv', mode='r') as file:
    # Gathering all the tags used throughout the all the post
        csv_reader = csv.DictReader(file)
        ln = 0
        for row in csv_reader:
            tags = row['Tags']
            tags = tags.replace('[', '').replace(']', '').replace("'", '')
            tags = tags.split(', ')
            for tag in tags:
                if tag not in all_tags and len(tag) != 0:
                    all_tags.append(tag)

    tags_with_views = []
    with open('data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tags = row["Tags"]
            tags = tags.replace('[', '').replace(']', '').replace("'", '').split(', ')
            views = int(row['Views'])
            tags_with_views.append([tags, views])

    for tag in all_tags:
        tmpViews = 0
        for tags in tags_with_views:
            if tag in tags[0]:
                tmpViews += tags[1]
        
        tag_per_views.append([tag, tmpViews])

    x_axis = [i for i in range(len(tag_per_views))]
    views = [i[1] for i in tag_per_views]
    x_ticks = [i[0] for i in tag_per_views]
    
    plt.xticks(ticks=x_axis, labels=x_ticks, fontsize=8, rotation=30)
    plt.bar(x_axis, views)
    plt.show()


def graph_progress():
    data = pd.read_csv('data.csv')
    views = list(data['Views'])[::-1]
    comments = list(data['Comments'])[::-1]
    reactions = list(data['Reactions'])[::-1]

    inc_views = [views[0]]
    inc_comments = [comments[0]]
    inc_reactions = [reactions[0]]

    for i in range(1, len(views)):
        inc_views.append(inc_views[i-1] + views[i])
        inc_comments.append(inc_comments[i-1] + comments[i])
        inc_reactions.append(inc_reactions[i-1] + reactions[i])

    x_axis = [i for i in range(len(views))]

    plt.title('Ojive Curve for Views, commetns, reactions')
    plt.xticks(ticks=x_axis)
    plt.plot(x_axis, inc_views, label="Views", marker='o')
    plt.plot(x_axis, inc_comments, label="Comments", marker='o')
    plt.plot(x_axis, inc_reactions, label="Reactions", marker='o')
    plt.xlabel("Post numbers")
    plt.ylabel("Popularity")
    plt.legend()
    plt.show()


def graph_progress_filter(cmd):
    data = pd.read_csv('data.csv')

    view = list(data['Views'])[::-1]
    comment = list(data['Comments'])[::-1]
    reaction = list(data['Reactions'])[::-1]

    views = [view[0]]
    comments = [comment[0]]
    reactions = [reaction[0]]

    for i in range(1, len(view)):
        views.append(views[i-1] + view[i])
        comments.append(comments[i-1] + comment[i])
        reactions.append(reactions[i-1] + reaction[i])

    x_axis = [i for i in range(len(view))]

    cmd = cmd.replace("graph-progress-", "")
    cmd = cmd.split('-')
    values = []

    for i in cmd:
        if i == 'views':
            values.append(views)
        elif i == 'comments':
            values.append(comments)
        elif i == 'reactions':
            values.append(reactions)

    title = ''

    for i in range(len(values)):
        plt.plot(x_axis, values[i], label=cmd[i], marker='o')
        title += cmd[i] + ' '

    plt.xticks(ticks=x_axis)
    plt.title(f"Ojive line of {title}")
    plt.xlabel("Post numbers")
    plt.ylabel("Popularity")
    plt.legend()
    plt.show()


def graph_pie_tags():
    all_tags = []

    with open('data.csv', mode='r') as file:
    # Gathering all the tags used throughout the all the post
        csv_reader = csv.DictReader(file)
        ln = 0
        for row in csv_reader:
            tags = row['Tags']
            tags = tags.replace('[', '').replace(']', '').replace("'", '')
            tags = tags.split(', ')
            for tag in tags:
                if tag not in all_tags and len(tag) != 0:
                    all_tags.append(tag)

    unfiltered_tags = []
    with open('data.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            tags = row["Tags"]
            tags = tags.replace('[', '').replace(']', '').replace("'", '').split(', ')
            unfiltered_tags.append(tags)


    tags_count = []
    for tag in all_tags:
        count = 0
        for tags in unfiltered_tags:
            if tag in tags:
                count += 1
    
        tags_count.append(count)

    mx = max(tags_count)
    explode = []
    for val in tags_count:
        if val == mx:

            explode.append(0.1)
        else:
            explode.append(0)

    plt.pie(tags_count, labels=all_tags, rotatelabels=90, explode=explode)
    my_circle=plt.Circle( (0,0), 0.7, color='white')
    p=plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()

def progress_avg(filters):
    attributes = filters.split('-')
    if len(attributes) == 2:
        attributes = ['Views', 'Reactions', 'Comments']
    else:
        attributes = attributes[2:]

    data = pd.read_csv('data.csv')

    for attribute in attributes:
        tmp = list(data[attribute.title()])[::-1]
        curr_sum = 0
        ls = []
        for i in range(len(tmp)):
            curr_sum += tmp[i]
            tmp_avg = curr_sum // (i + 1)
            ls.append(tmp_avg)

        x_axis = [i for i in range(len(ls))]
        plt.plot(x_axis, ls, label=attribute.title(), marker='o')
        plt.legend()
    plt.show()
