from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.charts import Pie
from pyecharts.charts import Bar
import pandas as pd

# 获取源数据
json_str = pd.read_json('data/last_day_corona_virus.json')
json_str_of_china = pd.read_json('data/last_day_corona_virus_of_china.json')

phase = ['国内累计病例', '国内累计治愈病例', '国内累计死亡病例']


# 获取国内疫情数据
def GetData():
    confirmedCount = 0
    curedCount = 0
    deadCount = 0
    for i in json_str_of_china['confirmedCount']:
        confirmedCount += int(i)
    for i in json_str_of_china['curedCount']:
        curedCount += int(i)
    for i in json_str_of_china['deadCount']:
        deadCount += int(i)
    list1 = [confirmedCount, curedCount, deadCount]
    return list1

# 获取15个国家的疫情数据
def GetData2(a):
    list1 = []
    s = 0
    for i in json_str[a]:
        list1.append(i)
        s+=1
        if(s==15):
            break
    return list1



# 构造漏斗图
def CV_Funnel():
    c = (
        Funnel()
        .add("阶段", [list(z) for z in zip(phase, GetData())])
        .set_global_opts(title_opts=opts.TitleOpts(title="漏斗图"))
        .render("visual_view/国内疫情数据漏斗图.html")
    )
# 构造饼图
def CV_Pie():
    c = (
        Pie()
        .add("", [list(z) for z in zip(phase, GetData())])
        .set_colors(["purple", "pink", "orange"])
        .set_global_opts(title_opts=opts.TitleOpts(title="国内疫情数据对比"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .render("visual_view/国内疫情数据饼图.html")
    )

# 构造柱形图
def CV_Bar():
    c = (
        Bar()
        .add_xaxis(GetData2('provinceName'))
        .add_yaxis("累计病例", GetData2('confirmedCount'), stack="stack1")
        .add_yaxis("治愈病例", GetData2('curedCount'), stack="stack1")
        .add_yaxis("死亡病例", GetData2('deadCount'), stack="stack1")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="疫情数据对比"))
        .render("visual_view/世界疫情数据柱形图.html")
    )

CV_Funnel()
CV_Pie()
CV_Bar()

