import requests
from bs4 import BeautifulSoup
import csv

if __name__ == '__main__':
    with open('morioka_temperature.csv', 'a', newline='') as f:
        df = csv.writer(f)
        df.writerow([Year, Date, Temparature])
        for year in range(2018, 2022):
            url = 'http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=33&block_no=47584&year=' + str(year) + '&month=4&day=&view=p1'
            res = requests.get(url)
            content_type_encoding = res.encoding if res.encoding != 'ISO-8859-1' else None
            soup = BeautifulSoup(res.content, 'html.parser', from_encoding=content_type_encoding)
            for day in range(5,35):
                # 日付データ
                date = soup.select('table[class="data2_s"] > tr:nth-of-type(' + str(day) + ') > td:nth-of-type(1) > div > a')

                # 最高気温データ
                temp = soup.select('table[class="data2_s"] > tr:nth-of-type(' + str(day) + ') > td:nth-of-type(8)')
                df.writerow([year, date, temp])
