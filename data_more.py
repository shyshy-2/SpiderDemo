#-*- coding = utf-8 -*-
#@Time : XXXXXXXXXXXXXXXX
#@Author : shy-2
#@File : data_more.py
#@Software : PyCharm

import json
import map_draw
import data_get

with open("data.json",'r') as file:
    data = file.read()
    data = json.loads(data)

# print(data)

map = map_draw.Draw_map()
datas = data_get.Get_data()
datas.get_data()
update_time = datas.get_time()
datas.parse_data()

#中国疫情地图数据
def china_map():
    area = []
    confirmed = []
    for each in data:
        # print(each)
        # print('*'*50+'\n')
        area.append(each['area'])
        confirmed.append(each['confirmed'])
    # print(area)
    # print(confirmed)
    map.to_map_china(area,confirmed,update_time)

#省份疫情数据
def province_map():
    for each in data:
        city = []
        confirmeds = []
        province = each['area']
        for each_city in each['subList']:
            city.append(each_city['city'])
            confirmeds.append(each_city['confirmed'])

        # print(city)
        # print(confirmeds)

china_map()