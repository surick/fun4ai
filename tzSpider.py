import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取维基百科页面的HTML内容
url = "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones"
response = requests.get(url)
html_content = response.text

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 找到时区列表的表格
table = soup.find('table', {'class': 'wikitable sortable sticky-header-multi'})

if table is None:
    print("未找到表格元素。请检查页面结构是否发生变化。")
    # 打印页面内容的一部分，帮助调试
    #print("页面内容的一部分：", html_content[:5500])

# 提取表格中的数据
data = []
for row in table.find_all('tr')[1:]:  # 跳过表头
    cols = row.find_all('td')
    if len(cols) >= 3:
        country_code = cols[0].text.strip()
        tz_idetifier = cols[1].text.strip()
        utc_offset = cols[4].text.strip()
        time_zone_abbreviation = cols[6].text.strip()
        data.append([country_code, tz_idetifier, utc_offset, time_zone_abbreviation])

# 将数据转换为DataFrame
df = pd.DataFrame(data, columns=['Country code', 'TZ identifier', 'UTC offset', 'Time zone abbreviation'])

# 将DataFrame保存到Excel文件中
output_file = 'tz_database_time_zones.xlsx'
df.to_excel(output_file, index=False)

print(f"时区数据已成功保存到 {output_file}")