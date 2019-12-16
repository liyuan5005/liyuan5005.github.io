# encoding=utf-8
# MSBD5005 Group Project data visualization for Yelp
# Horizon graph and river graph

import pandas as pd
import numpy as np

def read_data_split():
	df_Lasv=pd.read_csv('/Users/chenpengyao/Desktop/HKUST/BDT/MSBD_5005_DV/Group_Project/filtered_reviews_1000.csv')
	list1=df_Lasv['business_id'].value_counts()
	#print(df_Lasv['business_id'].value_counts())
	store1=list1.index[0]
	store2=list1.index[1]

	def date_process(x):
		return x[0:10]

	df_Lasv['Date']=df_Lasv['date'].apply(date_process)
	#print(df_Lasv['date'][0][0:10])
	df=df_Lasv.sort_values(by="Date",ascending= True)
	df=df[{'business_id','Date','stars','text'}]
	df.index=range(len(df))
	df_test=df.iloc[43509:,:]

	df_store1=df_test[df_test['business_id']==store1]
	df_store2 = df_test[df_test['business_id'] == store2]
	test_1=df_store1.groupby('Date').mean()
	test_2=df_store2.groupby('Date').mean()
	df_store1['pos_neg']=df_store1['stars']-round(test_1.mean()[0],6)
	df_store2['pos_neg'] = df_store2['stars'] - round(test_2.mean()[0], 6)

	def posneg_pross(test):
		def pos(x):
			if x>0:
				return x
			else:
				return None
		def neg(x):
			if x<0:
				return x
			else:
				return None
		def partition(x,a,b):
			if a<=x and x<b:
				return round(x,2)
			else:
				return None
		test['pos']=test['pos_neg'].apply(pos)
		test['neg']=test['pos_neg'].apply(neg)
		test['1_star']=test['stars'].apply(partition,args=(0,1,))
		test['2_star']=test['stars'].apply(partition,args=(1,2,))
		test['3_star']=test['stars'].apply(partition,args=(2,3,))
		test['4_star']=test['stars'].apply(partition,args=(3,4,))
		test['5_star']=test['stars'].apply(partition,args=(4,5,))
		test = test.where(test.notnull(), 0)
		return test

	df_store1=posneg_pross(df_store1)
	df_store2 = posneg_pross(df_store2)
	df_store1.index = range(len(df_store1))
	df_store2.index = range(len(df_store2))

	return df_store1,df_store2

df_store1,df_store2=read_data_split()
#df_.to_excel('/Users/chenpengyao/Desktop/5005horizon_data.xlsx')

"""river plot"""
import pygal
def river_plot(df,n):
	def river_point(df,v1,v2):
		#print('2018-10-14'<=df[df['Date'] < '2018-11-14'])
		df_1=df[df['Date']<v2]
		df_1 = df_1[df_1['Date'] >= v1]
		df_1.index = range(len(df_1))
		x=[]
		def cal(a):
			y=[]
			for i in range(len(df_1)):
				if df_1['stars'][i]==a:
					y.append(df_1['stars'][i])
			return len(y)
		x.append(cal(1))
		x.append(cal(2))
		x.append(cal(3))
		x.append(cal(4))
		x.append(cal(5))
		return x

	#df_test.index=range(len(df_test))
	list=[]
	"""
'2013-11-14','2013-11-29','2013-12-14','2013-12-29','2014-01-14','2014-01-29',
		   '2014-02-14','2014-02-28','2014-03-14','2014-03-29','2014-04-14','2014-04-29',
		   '2014-05-14','2014-05-29','2014-06-14','2014-06-29','2014-07-14','2014-07-29',
		   '2014-08-14','2014-08-29','2014-09-14','2014-09-29','2014-10-14','2014-10-29',
		   '2014-11-14','2014-11-29','2014-12-14','2014-12-29','2015-01-14','2015-01-29',
		   '2015-02-14','2015-02-28','2015-03-14','2015-03-29','2015-04-14','2015-04-29',
		   '2015-05-14','2015-05-29','2015-06-14','2015-06-29','2015-07-14','2015-07-29',
		   '2015-08-14','2015-08-29','2015-09-14','2015-09-29','2015-10-14','2015-10-29',
		   '2015-11-14','2015-11-29','2015-12-14','2015-12-29','2016-01-14','2016-01-29',
		   '2016-02-14','2016-02-28','2016-03-14','2016-03-29','2016-04-14','2016-04-29',
		   '2016-05-14','2016-05-29','2016-06-14','2016-06-29','2016-07-14','2016-07-29',
		   '2016-08-14','2016-08-29','2016-09-14','2016-09-29','2016-10-14','2016-10-29',
		   '2016-11-14','2016-11-29','2016-12-14','2016-12-29','2017-01-14','2017-01-29',
		   '2017-02-14','2017-02-28','2017-03-14','2017-03-29','2017-04-14','2017-04-29',
"""
	list_date=['2017-05-14','2017-05-29','2017-06-14','2017-06-29','2017-07-14','2017-07-29',
		   '2017-08-14','2017-08-29','2017-09-14','2017-09-29','2017-10-14','2017-10-29',
		   '2017-11-14','2017-11-29','2017-12-14','2017-12-29','2018-01-14','2018-01-29',
		   '2018-02-14','2018-02-28','2018-03-14','2018-03-29','2018-04-14','2018-04-29',
		   '2018-05-14','2018-05-29','2018-06-14','2018-06-29','2018-07-14','2018-07-29',
		   '2018-08-14','2018-08-29','2018-09-14','2018-09-29','2018-10-14','2018-10-29',
		   '2018-11-14']
	for i in range(len(list_date)-1):
		list.append(river_point(df,list_date[i],list_date[i+1]))

	df_2=pd.DataFrame(list)
	'''
line_chart = pygal.Line()
line_chart.title = 'River Metaphor for stars'
line_chart.x_labels = map(str, range(2017, 2018))
line_chart.add('one stars', df_2[0])
line_chart.add('two stars', df_2[1])
line_chart.add('three stars', df_2[2])
line_chart.add('four stars', df_2[3])
line_chart.add('five stars', df_2[4])
line_chart.render_to_file("/Users/chenpengyao/Desktop/line-stacked1.svg")
'''

	line_chart = pygal.StackedLine(fill=True)
	line_chart.title = str('River Metaphor of stars for store' + str(n))
	line_chart.x_labels = [2017]
	line_chart.add('one stars', df_2[0])
	line_chart.add('two stars', df_2[1])
	line_chart.add('three stars', df_2[2])
	line_chart.add('four stars', df_2[3])
	line_chart.add('five stars', df_2[4])
	save_path="/Users/chenpengyao/Desktop/line-stacked_store"+str(n)+".svg"
	line_chart.render_to_file(save_path)

river_plot(df_store1,1)
river_plot(df_store2,2)

"""word cloud"""
from os import path
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def generate_wordcloud(text,n,m):
	'''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
	# 设置显示方式
	d = path.dirname('/Users/chenpengyao/Desktop/')
	alice_mask = np.array(Image.open(path.join(d, "river.png")))
	#font_path=path.join(d,"font//msyh.ttf")
	stopwords = set(STOPWORDS)
	if m<3:
		contour_color='red'
		colormap='Reds'
	elif m==3:
		contour_color = 'green'
		colormap = 'Greens'
	else:
		contour_color = 'lightblue'
		colormap = 'Blues'
	wc = WordCloud(contour_color=contour_color,
				   contour_width=1,
				   colormap=colormap,
				   background_color="white",# 设置背景颜色
				   max_words=200, # 词云显示的最大词数
				   mask=alice_mask,# 设置背景图片
				   stopwords=stopwords, # 设置停用词
				   #font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )
	# 生成词云
	wc.generate(text)
	# 生成的词云图像保存到本地
	save_path='store_'+str(n)+'_star_'+str(m)+'.png'
	wc.to_file(path.join(d, save_path))

	# 显示图像
	plt.imshow(wc, interpolation='bilinear')
	# interpolation='bilinear' 表示插值方法为双线性插值
	plt.axis("off")# 关掉图像的坐标
	plt.show()

# 画图
def wordcloud_store(n,m):
	str1=str(m+1)+'_star'
	if n==1:
		df_text = df_store1[df_store1[str1]==m]['text']
	if n==2:
		df_text = df_store2[df_store2[str1] ==m]['text']
	df_text.index=range(len(df_text))
	text=''
	for i in range(len(df_text)):
		text+=str(' '+df_text[i])
	# 生成词云
	if text!='':
		generate_wordcloud(text,n,m)
	else:
		print('Sorry, store_'+str(n)+'_'+str(m)+'_star has no output')

#wordcloud_store(1,2)

for i in range(2):
	for j in range(0,4):
		wordcloud_store(i+1,j+1)

"""正负向分析"""
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

def posneg_plot(df,n):
	def posneg(df, v1, v2):
		# print('2018-10-14'<=df[df['Date'] < '2018-11-14'])
		df_1 = df[df['Date'] < v2]
		df_1 = df_1[df_1['Date'] >= v1]
		df_1.index = range(len(df_1))
		pos = []
		neg = []

		for i in range(len(df_1)):
			if df_1['pos_neg'][i] < 0:
				neg.append(df_1['pos_neg'][i])
			if df_1['pos_neg'][i] > 0:
				pos.append(df_1['pos_neg'][i])
		if len(pos) != 0 and len(neg) != 0:
			return round(np.mean(pos),4), round(np.mean(neg),4)
		if len(neg) == 0:
			return round(np.mean(pos),4),0
		if len(pos) == 0:
			return 0,round(np.mean(neg),4)


		return np.mean(pos),np.mean(neg)

	# df_test.index=range(len(df_test))
	list1 = []
	list2=[]
	"""list_date = ['2017-05-14','2017-05-21', '2017-05-29','2017-06-07', '2017-06-14', '2017-06-21','2017-06-29', '2017-07-07',
				 '2017-07-14','2017-07-21', '2017-07-29','2017-08-07', '2017-08-14', '2017-08-21','2017-08-29', '2017-09-07',
				 '2017-09-14', '2017-09-21', '2017-09-29', '2017-10-07', '2017-10-14', '2017-10-21', '2017-10-29','2017-11-07',
				 '2017-11-14', '2017-11-21', '2017-11-29', '2017-12-07', '2017-12-14', '2017-12-21', '2017-12-29','2018-01-07',
				 '2018-01-14', '2017-01-21', '2017-01-29','2018-01-07','2018-01-14', '2017-01-21', '2017-01-29',
				 '2018-02-07', '2018-02-14', '2017-02-21', '2017-02-29','2018-03-07', '2018-03-14', '2017-03-21', '2017-03-29',
				 '2018-04-07', '2018-04-14', '2017-04-21', '2017-04-29','2018-05-07', '2018-05-14', '2017-05-21', '2017-05-29',
				 '2018-06-07', '2018-06-14', '2018-06-21','2018-06-29', '2018-07-07','2018-07-14','2018-07-21', '2018-07-29',
				 '2018-08-07', '2018-08-14', '2018-08-21','2018-08-29', '2018-09-07','2018-09-14', '2018-09-21', '2018-09-29',
				 '2018-10-07', '2018-10-14', '2018-10-21', '2018-10-29','2018-11-07','2018-11-14'
				 ]"""
	list_date=['2017-05-14','2017-05-29','2017-06-14','2017-06-29','2017-07-14','2017-07-29',
		   '2017-08-14','2017-08-29','2017-09-14','2017-09-29','2017-10-14','2017-10-29',
		   '2017-11-14','2017-11-29','2017-12-14','2017-12-29','2018-01-14','2018-01-29',
		   '2018-02-14','2018-02-28','2018-03-14','2018-03-29','2018-04-14','2018-04-29',
		   '2018-05-14','2018-05-29','2018-06-14','2018-06-29','2018-07-14','2018-07-29',
		   '2018-08-14','2018-08-29','2018-09-14','2018-09-29','2018-10-14','2018-10-29',
		   '2018-11-14']
	for i in range(len(list_date) - 1):
		list1.append(posneg(df, list_date[i], list_date[i + 1])[0])
		list2.append(posneg(df, list_date[i], list_date[i + 1])[1])

	x = ['2017-05-14','2017-05-29','2017-06-14','2017-06-29','2017-07-14','2017-07-29',
		   '2017-08-14','2017-08-29','2017-09-14','2017-09-29','2017-10-14','2017-10-29',
		   '2017-11-14','2017-11-29','2017-12-14','2017-12-29','2018-01-14','2018-01-29',
		   '2018-02-14','2018-02-28','2018-03-14','2018-03-29','2018-04-14','2018-04-29',
		   '2018-05-14','2018-05-29','2018-06-14','2018-06-29','2018-07-14','2018-07-29',
		   '2018-08-14','2018-08-29','2018-09-14','2018-09-29','2018-10-14','2018-10-29',
		   '2018-11-14']
	fig = go.Figure()
	fig.add_trace(go.Bar(x=x, y=list1,name='Positive'))
	fig.add_trace(go.Bar(x=x, y=list2,name='Negative'))

	fig.update_layout(barmode='relative', title_text=str('Half-monthly sentiment for store'+str(n)))
	#pyplt(fig)
	save_path='Store'+str(n)
	fig.write_html('/Users/chenpengyao/Desktop/'+save_path+'.html', auto_open=True)

posneg_plot(df_store1,1)
posneg_plot(df_store2,2)




