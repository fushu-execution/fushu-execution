# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 21:13:31 2021

@author: Asus
"""
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Pie
from pyecharts.faker import Faker
#调用数据
src_filename = '../第一次作业/output/result.csv'
src_file = open(src_filename, 'r',encoding='utf-8')

line_list = src_file.readlines()
src_file.close()
del line_list[0]
word_list=[]
cnt_list=[]
for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))
    
bar = (
    Bar()
    .add_xaxis(word_list[0:10])
    .add_yaxis("", cnt_list[0:10],color=Faker.rand_color())
    .set_global_opts(title_opts=opts.TitleOpts(title="柱状图",subtitle=('《中国人的精神》词频统计')))
    .render(".\柱状图.html")
)

'''DataPair=[]
for i in range(10):
    DataPair.append((word_list[i],cnt_list[i]))
    
pie = (   
    Pie()
    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )


    Pie()
    .add(series_name='词语'
        ,data_pair=DataPair)
    .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple",'grey','brown','dark blue'])
    .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="饼状图", pos_top="48%"),
        legend_opts=opts.LegendOpts(pos_top="48%"),
    )
grid = (
    Grid()
    .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(pie, grid_opts=opts.GridOpts(pos_top="60%"))
    .render(".\柱状图和饼状图.html")
)'''


