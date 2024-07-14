import time
import requests as req
import json
import schedule

def Main():
    # 定义API URL
    api_url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001"

    # 定义请求参数
    params_list = [
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "基隆市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "宜蘭縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "花蓮縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "臺東縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "澎湖縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "金門縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "連江縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "臺北市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "新北市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "桃園市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "臺中市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "臺南市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "高雄市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "新竹縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "新竹市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "苗栗縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "彰化縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "南投縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "雲林縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "嘉義縣"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "嘉義市"},
        {"Authorization": "CWA-A48B1C25-73BD-4DFB-8FCC-D8BC0EC033E2", "locationName": "屏東縣"},
    ]

    # 初始化结果字典
    weather_data = {}

    # 遍历参数列表并获取天气数据
    for params in params_list:
        location_name = params["locationName"]
        weather_data[location_name] = {}

        # 发送请求并解析响应
        res = req.get(api_url, params=params)
        res_data = res.json()

        # 检查location列表是否包含数据
        if "records" in res_data and "location" in res_data["records"] and len(res_data["records"]["location"]) > 0:
            location_data = res_data["records"]["location"][0]

            # 遍历获取的天气元素
            for i in range(5):
                if i < len(location_data["weatherElement"]):
                    name = location_data["weatherElement"][i]["elementName"]
                    value = location_data["weatherElement"][i]["time"][0]["parameter"]["parameterName"]
                    weather_data[location_name][name] = value
                    print(location_name, name, value)
        else:
            print(f"No data found for {location_name}")

    # 打印完整的天气数据字典
    print(weather_data)

    with open('Weather.json', 'w', encoding='utf-8') as json_file:
        json.dump(weather_data, json_file, ensure_ascii=False, indent=4)

    print("天气数据已保存到 Weather.json 文件中")

if __name__ == '__main__':
    # 设置定时任务
    schedule.every().day.at("05:00:00").do(Main)

    # 运行定时任务
    while True:
        schedule.run_pending()
        time.sleep(1)
