#!/usr/bin/env python
# -*- coding: utf-8 -*-


from pyecharts import Bar

def draw_bar():
	bar = Bar("我的第一个图表", "这里是副标题")
	bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
	bar.show_config()
	bar.render()

from pyecharts import EffectScatter

def draw_e_scatter():
	v1 = [10, 20, 30, 40, 50, 60]
	v2 = [25, 20, 15, 10, 60, 33]
	es = EffectScatter("动态散点图示例")
	es.add("effectScatter", v1, v2)
	es.render()

from pyecharts import Funnel
def draw_funnel():
	attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	value = [20, 40, 60, 80, 100, 120]
	funnel = Funnel("漏斗图示例")
	funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
	funnel.render()

from pyecharts import Geo
def draw_geo():
	data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
	geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",          width=1200, height=600, background_color='#404a59')
	attr, value = geo.cast(data)
	geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
	geo.show_config()
	geo.render()

from pyecharts import Graph
def draw_graph():
	nodes = [{"name": "结点1", "symbolSize": 10},
	         {"name": "结点2", "symbolSize": 20},
	         {"name": "结点3", "symbolSize": 30},
	         {"name": "结点4", "symbolSize": 40},
	         {"name": "结点5", "symbolSize": 50},
	         {"name": "结点6", "symbolSize": 40},
	         {"name": "结点7", "symbolSize": 30},
	         {"name": "结点8", "symbolSize": 20}]
	links = []
	for i in nodes:
		for j in nodes:
			links.append({"source": i.get('name'), "target": j.get('name')})
	graph = Graph("关系图-环形布局示例")
	graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
	graph.show_config()
	graph.render()

from pyecharts import Line
def draw_line():
	attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	v1 = [5, 20, 36, 10, 10, 100]
	v2 = [55, 60, 16, 20, 15, 80]
	line = Line("折线图示例")
	line.add("商家A", attr, v1, mark_point=["average"])
	line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
	line.add("商家C", attr, v1, is_step=True, is_label_show=True)
	line.show_config()
	line.render()

def draw_fill():
	attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
	v1 = [5, 20, 36, 10, 10, 100]
	v2 = [55, 60, 16, 20, 15, 80]
	line = Line("折线图-面积图示例")
	line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
	line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
	line.show_config()
	line.render()

from pyecharts import Liquid
def draw_liquid():
	liquid = Liquid("水球图示例")
#	liquid.add("Liquid", [0.6])
	#liquid.add("Liquid", [0.8, 0.6, 0.5, 0.4, 0.3], is_liquid_outline_show=False)
	liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=True, shape='diamond')
	liquid.show_config()
	liquid.render()

from pyecharts import Map
def draw_map():
	value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
	attr = ["福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"]
	map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
	map.add("", attr, value, maptype="china", is_visualmap=True, visual_text_color='#000')
	map.show_config()
	map.render()

from pyecharts import Parallel
def draw_parallel():
	c_schema = [
	    {"dim": 0, "name": "data"},
	    {"dim": 1, "name": "AQI"},
	    {"dim": 2, "name": "PM2.5"},
	    {"dim": 3, "name": "PM10"},
	    {"dim": 4, "name": "CO"},
	    {"dim": 5, "name": "NO2"},
	    {"dim": 6, "name": "CO2"},
	    {"dim": 7, "name": "等级",    "type": "category", "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}
	]
	data = [
	    [1, 91, 45, 125, 0.82, 34, 23, "良"],
	    [2, 65, 27, 78, 0.86, 45, 29, "良"],
	    [3, 83, 60, 84, 1.09, 73, 27, "良"],
	    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
	    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
	    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
	    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
	    [8, 89, 65, 78, 0.86, 51, 26, "良"],
	    [9, 53, 33, 47, 0.64, 50, 17, "良"],
	    [10, 80, 55, 80, 1.01, 75, 24, "良"],
	    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
	    [12, 99, 71, 142, 1.1, 62, 42, "良"],
	    [13, 95, 69, 130, 1.28, 74, 50, "良"],
	    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
	]
	parallel = Parallel("平行坐标系-用户自定义指示器")
	parallel.config(c_schema=c_schema)
	parallel.add("parallel", data)
	parallel.show_config()
	parallel.render()


from pyecharts import WordCloud
def draw_wordcloud():
	name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications',
	        'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
	        'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham',
	        'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
	value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555,
	         550, 462, 366, 360, 282, 273, 265]
	wordcloud = WordCloud(width=1300, height=620)
	#wordcloud.add("", name, value, word_size_range=[20, 100])
	wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
	wordcloud.show_config()
	wordcloud.render()


from pyecharts import Bar, Line
def draw_bar_custom():
	attr = ['A', 'B', 'C', 'D', 'E', 'F']
	v1 = [10, 20, 30, 40, 50, 60]
	v2 = [15, 25, 35, 45, 55, 65]
	v3 = [38, 28, 58, 48, 78, 68]
	bar = Bar("Line - Bar 示例")
	bar.add("bar", attr, v1)
	line = Line()
	line.add("line", v2, v3)
	#bar.custom(line.get_series())
	bar.show_config()
	bar.render()

import math
from pyecharts import Polar

def draw_polar_love():
	data = []
	for i in range(101):
	    theta = i / 100 * 360
	    r = 5 * (1 + math.sin(theta / 180 * math.pi))
	    data.append([r, theta])
	hour = [i for i in range(1, 25)]
	polar = Polar("极坐标系示例", width=1200, height=600)
	polar.add("Love", data, angle_data=hour, boundary_gap=False,start_angle=0)
	polar.show_config()
	polar.render()

import math
from pyecharts import Polar
def draw_polar_flower():
	data = []
	for i in range(361):
	    t = i / 180 * math.pi
	    r = math.sin(2 * t) #* math.cos(2 * t)
	    data.append([r, i])
	polar = Polar("极坐标系示例", width=1200, height=600)
	polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
	polar.show_config()
	polar.render()

import math
from pyecharts import Polar
def draw_polar_butterfly():
	data = []
	for i in range(361):
	    t = i / 180 * math.pi
	    #r = math.sin(1 * t) * math.cos(3 * t)
	    r = math.sin(2 * t) * math.cos(3 * t)
	    data.append([r, i])
	polar = Polar("极坐标系示例", width=1200, height=600)
	polar.add("Color-Flower", data, start_angle=0, symbol=None, axis_range=[0, None],
	          area_color="#f71f24", area_opacity=0.6)
	polar.render()


from pyecharts import Line
def draw_line_mark():
	attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
	line = Line("折线图示例")
	line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10], mark_point=["max", "min"], mark_line=["average"])
	line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],
	         mark_line=["average"], yaxis_formatter="°C")
	line.show_config()
	line.render()

import random
from pyecharts import Pie
def draw_pie_mulit():
	attr = ['A', 'B', 'C', 'D', 'E', 'F']
	pie = Pie("饼图示例", width=1000, height=600)
	pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[25, 50],is_random=True)
	pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[25, 50],rosetype='area')
	#pie.add("", attr, [random.randint(0, 100) for _ in range(6)], radius=[50, 55], center=[65, 50],is_random=True)
	#pie.add("", attr, [random.randint(20, 100) for _ in range(6)], radius=[0, 45], center=[65, 50],rosetype='radius')
	pie.show_config()
	pie.render()

def draw_bar_multi():
	attr = ["{}月".format(i) for i in range(1, 13)]
	v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
	v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
	bar = Bar("柱状图示例")
	bar.add("蒸发量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
	bar.add("降水量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
	bar.show_config()
	bar.render()


import math
from pyecharts import Polar
def draw_polar_snail():
	data = []
	for i in range(5):
		for j in range(101):
			theta = j / 100 * 360
			alpha = i * 360 + theta
			r = math.pow(math.e, 0.003 * alpha)
			data.append([r, theta])
	polar = Polar("极坐标系示例")
	polar.add("", data, symbol_size=0, symbol='circle', start_angle=-25, is_radiusaxis_show=False,          area_color="#f3c5b3", area_opacity=0.5, is_angleaxis_show=False)
	polar.show_config()
	polar.render()
from pyecharts import Line, Bar, Overlap
import math
def draw_line_tax():
	tax_rate_law=[
		[
			[3500,0],
			[0,3],
			[1500,10],
			[4500,20],
			[9000,25],
			[35000,30],
			[55000,35],
			[80000,45],
		]
	]

	tax_rate=[ x[0] for x in tax_rate_law[0] ]

	print(tax_rate)
	print((len(tax_rate)))

	quick_num =[0] * len(tax_rate)
	rates=tax_rate_law[0]
	print(range(2,len(tax_rate)))
	for i in range(2,len(tax_rate)):
		#print(i)
		#print(rates[i][0])
		quick_num[i]=(rates[i][0])*(rates[i][1] - rates[i-1][1])/100 +  quick_num[i-1]
	print(quick_num),
	rates={}
	rates['quick_num'] = quick_num[0:]
	rates['basic'] =tax_rate_law[0][0][0]
	rates['start'] = [ x[0] + tax_rate_law[0][0][0] for x in tax_rate_law[0] ]
	rates['start'][0] = 0
	rates['rate'] = [x[1] for x in tax_rate_law[0]]
	print ('-------------------------------------------')
	print(rates)
	print ('-------------------------------------------')

	def calc_tax(income):

		i=len(rates['start'])-1
		print('begin calc income: ', income, ', i: ', i)

		while(i>=0):
			print ('now compare: ', income, rates['start'][i])
			if(int(income) >= int(rates['start'][i])):
				ret = (income -rates['basic'])* rates['rate'][i]/100-rates['quick_num'][i]
				print('income %d, level:%d rate: %d,%f, tax:%f'%(income , rates['start'][i],rates['rate'][i],rates['quick_num'][i], ret))
				return ret
			i = i-1
		return 0

	def calc_tax_rate(income, tax):
		if(not income):
			return 0;
		return tax/income*100

	datas={}
	datas['income'] = rates['start'] + [rates['start'][-1] * 13/10,rates['start'][-1] * 15/10,rates['start'][-1] * 20/10,]
	datas['tax'] = [calc_tax(x) for x in datas['income']]
	datas['rate'] = [calc_tax_rate(datas['income'][i], datas['tax'][i]) for i in range(0, len(datas['income']))]

	print(datas)
	attr = datas['income']
	line = Line("纳税曲线")
	line.add("纳税曲线图", attr, datas['tax'], mark_point=["max", "min"])
	line2 = Line("纳税比例曲线")
	line2.add("纳税比例曲线图", attr, datas['rate'], mark_point=["max", "min"],yaxis_formatter="%")

	overlap = Overlap()
	# 默认不新增 x y 轴，并且 x y 轴的索引都为 0
	overlap.add(line)
	# 新增一个 y 轴，此时 y 轴的数量为 2，第二个 y 轴的索引为 1（索引从 0 开始），所以设置 yaxis_index = 1
	# 由于使用的是同一个 x 轴，所以 x 轴部分不用做出改变
	overlap.add(line2, yaxis_index=1, is_add_yaxis=True)
	overlap.render()

	#line.add("纳税曲线图", attr, datas['tax'], mark_point=["max", "min"], mark_line=["average"])
	#line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0], mark_point=["max", "min"],   mark_line=["average"], yaxis_formatter="°C")
	#line.show_config()
	#line.render()

if __name__ == '__main__':
	draw_line_tax()