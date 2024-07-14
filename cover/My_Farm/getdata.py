import requests
import json
import time

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 檢查請求是否成功
        return response.json()  # 返回 JSON 格式的數據
    except requests.exceptions.RequestException as e:
        print(f"請求失敗: {e}")
        return None

def save_to_json(data, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"成功保存到 {filename}")
    except Exception as e:
        print(f"寫入文件失敗: {e}")

if __name__ == "__main__":
    url = "http://192.168.0.106/getSensorData"
    while True:
        data = fetch_data(url)
        
        if data:
            print("獲取到的數據:", data)  # 打印獲取到的數據
            save_to_json(data, 'sensor_data.json')
        else:
            print("未獲取到有效數據")
        
        time.sleep(600)  # 每五分鐘
