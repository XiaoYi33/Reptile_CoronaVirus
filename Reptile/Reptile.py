import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm


class CoronaVirusSpider(object):
    def __init__(self):
        self.home_url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def get_conten_from_url(self, url):
        # 获取数据
        response = requests.get(url)
        return response.content.decode()

    def parse_home_page(self, home_page, tag_id):
        # 解析内容，提取解析后的python数据
        soup = BeautifulSoup(home_page, 'lxml')
        script = soup.find(id=tag_id)
        text = script.text
        # 获取json格式字符串
        json_str = re.findall(r'\[.+\]', text)[0]
        # 把json字符串转换成python数据
        data = json.loads(json_str)
        return data

    def load(self, path):
        with open(path, encoding='utf-8') as fp:
            data = json.load(fp)
        return data

    def save(self, data, path):
        # 保存数据
        with open(path, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False)

    # 获取最近一天各国疫情信息数据
    def crawl_last_day_corona_virus(self):

        # 发送请求，获取首页内容
        home_page = self.get_conten_from_url(self.home_url)
        # 解析首页内容
        last_day_corona_virus = self.parse_home_page(home_page, tag_id='getListByCountryTypeService2true')
        # 保存数据
        self.save(last_day_corona_virus, 'data/last_day_corona_virus.json')

    # 获取各国疫情信息数据
    def crawl_corona_virus(self):
        last_day_corona_virus = self.load('data/last_day_corona_virus.json')
        # print(last_day_corona_virus)
        corona_virus = self.parse_corona_virus(last_day_corona_virus, '采集各国以来的疫情数据信息')
        self.save(corona_virus, 'data/corona_virus.json')

    # 获取国内疫情信息数据
    def crawl_corona_virus_of_china(self):
        last_day_corona_virus_of_china = self.load('data/last_day_corona_virus_of_china.json')
        # print(last_day_corona_virus)
        corona_virus_of_china = self.parse_corona_virus(last_day_corona_virus_of_china, '采集各省以来的疫情数据信息')
        self.save(corona_virus_of_china, 'data/corona_virus_of_china.json')

    def parse_corona_virus(self, last_day_corona_virus, desc):
        data = []
        for country in tqdm(last_day_corona_virus, desc):
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.get_conten_from_url(statistics_data_url)
            statistics_data = json.loads(statistics_data_json_str)['data']
            for one_day in statistics_data:
                one_day['provinceName'] = country['provinceName']
            data.extend(statistics_data)
        return data

    def crawl_last_day_corona_virus_of_china(self):
        home_page = self.get_conten_from_url(self.home_url)
        last_day_corona_virus_of_china = self.parse_home_page(home_page, tag_id='getAreaStat')
        self.save(last_day_corona_virus_of_china, 'data/last_day_corona_virus_of_china.json')

    def run(self):
        self.crawl_last_day_corona_virus()
        self.crawl_last_day_corona_virus_of_china()
        self.crawl_corona_virus()
        self.crawl_corona_virus_of_china()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
