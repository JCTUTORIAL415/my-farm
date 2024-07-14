import requests
from bs4 import BeautifulSoup
import json

from datetime import datetime


def main():
    # 獲取當前時間
    current_time = datetime.now()
    # 提取年、月、日
    year = current_time.year
    month = current_time.month
    day = current_time.day
    # 將公元年份轉換為民國年份
    roc_year = year - 1911
    # 格式化時間為字符串，只包含年月日
    formatted_time = f"{roc_year}/{month:02d}/{day:02d}/"

    url = 'https://amis.afa.gov.tw/m_veg/VegProdDayTransInfo.aspx'

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '514758',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'amis.afa.gov.tw',
        'Origin': 'https://amis.afa.gov.tw',
        'Referer': 'https://amis.afa.gov.tw/m_veg/VegProdDayTransInfo.aspx',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }



    response = requests.post(url)

    print(response.status_code)

    def payload(response):
        __EVENTVALIDATION=''
        __VIEWSTATE=''

        for a in response.text.split('\n'):
            if '__VIEWSTATE' in a:
                a=a.split('"')
                for j in a:
                    if j[0]=='/':
                        __VIEWSTATE=j
            if '__EVENTVALIDATION' in a:
                a=a.split('"')
                for j in a:
                    if j[0]=='/':
                        __EVENTVALIDATION=j
        return [__EVENTVALIDATION,__VIEWSTATE]
        
    a=payload(response)

    data = {
    "ctl00$ScriptManager_Master": "ctl00$ScriptManager_Master|ctl00$contentPlaceHolder$btnQuery",
    "ctl00_contentPlaceHolder_ucVegMarket": "ALL",
    "ctl00_contentPlaceHolder_ucVegProduct": "ALL",
    "__EVENTTARGET": "ctl00$contentPlaceHolder$ucVegMarket$radlMarketRange$0",
    "__EVENTARGUMENT": "",
    "__LASTFOCUS": "",           
    "__VIEWSTATE": a[1],
    "__VIEWSTATEGENERATOR": "A2607747",
    "__EVENTVALIDATION": a[0],
    "ctl00$contentPlaceHolder$ucDateScope$rblDateScope": "D",
    "ctl00$contentPlaceHolder$ucSolarLunar$radlSolarLunar": "S",
    "ctl00$contentPlaceHolder$txtSTransDate": formatted_time,
    "ctl00$contentPlaceHolder$txtETransDate": formatted_time,
    "ctl00$contentPlaceHolder$ucVegMarket$radlMarketRange": "A",
    "ctl00$contentPlaceHolder$ucVegProduct$radlProductRange": "A",
    "__ASYNCPOST": "true",
    "ctl00$contentPlaceHolder$btnQuery": "查詢"
    }

    resp = requests.post(url, data=data, headers=headers)


    # 找到表格行
    soup = BeautifulSoup(resp.text.split('|0|hiddenField|')[0], 'lxml')

    # 找到第三个 table
    target_table = soup.find_all('table')[2]

    # 找到表格行
    rows = target_table.find_all('tr')

    # 提取表头
    headers = [header.text.strip() for header in rows[0].find_all('td')]

    # 提取数据行
    data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(dict(zip(headers, cols)))

    # 转换为 JSON
    json_data = json.dumps(data, ensure_ascii=False, indent=2)
    # print(json_data)
    with open('veg_data.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
    print()

if __name__ == '__main__':
    main()

main()