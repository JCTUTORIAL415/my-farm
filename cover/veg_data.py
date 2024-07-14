import json
with open("veg_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 現在您可以使用讀取的資料，例如列印它
print(data)
organized_data = {}

# 迭代原始資料，將資料整理成以產品為鍵，不同市場價格為值的形式
for item in data:
    product_name = item["產品"]
    market = item["市場"]
    price_info = {"上價": item["上價"], "中價": item["中價"], "下價": item["下價"], "平均價(元/公斤)": item["平均價(元/公斤)"], "跟前一交易日比較%": item["跟前一交易日比較%"], "交易量(公斤)": item["交易量(公斤)"]}
    
    if product_name not in organized_data:
        organized_data[product_name] = {}
    
    organized_data[product_name][market] = price_info

# 輸出整理後的資料
for product_name, market_prices in organized_data.items():
    print(f"產品名稱: {product_name}")
    for market, prices in market_prices.items():
        print(f"市場: {market}, 價格資訊: {prices}")

with open("officialveg.json", "w", encoding='utf-8') as file:
    json.dump(organized_data, file, ensure_ascii=False, indent=4)
    

product_names = list(organized_data.keys())
print(product_names)
