import pandas as pd
import xlwt

# 获取源数据
json_str = pd.read_json('data/last_day_corona_virus.json')


provinceName = []
confirmedCount = []
currentConfirmedCount = []
curedCount = []
deadCount = []
deadRate = []
deadRateRank = []
confirmedCountRank = []
deadCountRank = []

# 提取相关信息
for i in json_str['provinceName']:
    provinceName.append(i)
for i in json_str['confirmedCount']:
    confirmedCount.append(i)
for i in json_str['currentConfirmedCount']:
    currentConfirmedCount.append(i)
for i in json_str['curedCount']:
    curedCount.append(i)
for i in json_str['deadCount']:
    deadCount.append(i)
for i in json_str['deadRate']:
    deadRate.append(i)
for i in json_str['deadRateRank']:
    deadRateRank.append(i)
for i in json_str['confirmedCountRank']:
    confirmedCountRank.append(i)
for i in json_str['deadCountRank']:
    deadCountRank.append(i)


# 保存至excel表
file = xlwt.Workbook('encoding = utf-8')
sheet1 = file.add_sheet('sheet1', cell_overwrite_ok=True)
sheet1.write(0, 0, "provinceName")
sheet1.write(0, 1, "confirmedCount")
sheet1.write(0, 2, "currentConfirmedCount")
sheet1.write(0, 3, "curedCount")
sheet1.write(0, 4, "deadCount")
sheet1.write(0, 5, "deadRate")
sheet1.write(0, 6, "deadRateRank")
sheet1.write(0, 7, "confirmedCountRank")
sheet1.write(0, 8, "deadCountRank")


for i in range(len(provinceName)):
    sheet1.write(i + 1, 0, provinceName[i])
    sheet1.write(i + 1, 1, confirmedCount[i])
    sheet1.write(i + 1, 2, currentConfirmedCount[i])
    sheet1.write(i + 1, 3, curedCount[i])
    sheet1.write(i + 1, 4, deadCount[i])
    sheet1.write(i + 1, 5, deadRate[i])
    sheet1.write(i + 1, 6, deadRateRank[i])
    sheet1.write(i + 1, 7, confirmedCountRank[i])
    sheet1.write(i + 1, 8, deadCountRank[i])
file.save("data/corona_virus.xls")


