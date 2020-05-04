#-*- coding = utf-8 -*-
#@Time : XXXXXXXXXXXXXX
#@Author : shy-2
#@File : data_get.py
#@Software : PyCharm

import requests
from lxml import etree
import re
import json

class Get_data():
    #获取数据
    def get_data(self):
        response = requests.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3')
        with open('html.txt','w') as file:
            file.write(response.text)

    #提取更新时间
    def get_time(self):
        with open('html.txt','r') as file:
            text = file.read()
        time = re.findall('"mapLastUpdatedTime":"(.*?)"',text)[0]
        # print(time)
        return time

    #解析数据
    def parse_data(self):
        with open('html.txt','r') as file:
            text = file.read()
        html = etree.HTML(text)
        result = html.xpath('//script[@type="application/json"]/text()')
        # print(result)
        result = result[0]
        result = json.loads(result)
        result = result['component'][0]['caseList']
        result = json.dumps(result)
        with open("data.json",'w') as file:
            file.write(result)
            print("数据写入成功……")





