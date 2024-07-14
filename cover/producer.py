import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def main():
    formatted_time = "2024-06-26 22:22:22"
    url = "https://qrc.afa.gov.tw/ProducerSearch?pageSize=100"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referer": "https://qrc.afa.gov.tw/ProducerSearch?pageSize=100",
        # Add more headers if necessary based on actual requests from your browser
    }

    # GET request to retrieve initial page and extract __VIEWSTATE and __EVENTVALIDATION
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract any data you need from the HTML using BeautifulSoup
        # For example:
        producer_containers = soup.find_all('div', class_='producer-container')
        producers = []

        for container in producer_containers:
            producer_info = {}

            a_tag = container.find('a')
            if a_tag:
                producer_info['href'] = a_tag['href']

            product_name_tag = container.find('span', class_='product-name')
            if product_name_tag:
                producer_info['product_name'] = product_name_tag.text.strip()

            contact_address_tag = container.find('span', class_='contact-address')
            if contact_address_tag:
                producer_info['contact_address'] = contact_address_tag.text.strip()

            producers.append(producer_info)

        # Print or process the extracted data as needed
        for producer in producers:
            print(producer)

if __name__ == '__main__':
    main()

