import pandas as pd
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from bs4 import BeautifulSoup

# 读取 CSV 文件，指定编码为 UTF-8
df = pd.read_csv('ZL-2401-005.csv', encoding='utf-8')

# 按照时间列进行排序
df['create_date'] = pd.to_datetime(df['create_date'], format='%d/%m/%Y %H:%M:%S')
df = df.sort_values(by='create_date')

# 创建一个继承了 HTMLMixin 的 PDF 类
class PDF(FPDF):
    def header(self):
        self.set_font('SIMHEI', '', 12)
        self.cell(0, 10, 'ZL-2401-005 系统通知', 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')

    def chapter_title(self, title):
        self.set_font('SIMHEI', '', 12)
        self.cell(0, 10, title, 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='L')
        self.ln(10)

# 实例化 PDF
pdf = PDF()

# 添加黑体字体
pdf.add_font('SIMHEI', '', 'SIMHEI.TTF')
pdf.add_font('SIMHEI', 'B', 'SIMHEI.TTF')

# 添加页面
pdf.add_page()

# 循环遍历 CSV 数据
size = 1
for index, row in df.iterrows():
    size = size + 1
    pdf.chapter_title(' ')
    html_content = row['content'].replace('border:1px solid #ddd;', '')
    soup = BeautifulSoup(html_content, 'html.parser')
    # 遍历解析的 HTML 内容，并逐步写入 PDF
    for element in soup:
        pdf.write_html(str(element))
print(f'size ${size -1}')

# 保存 PDF 文件
pdf.output('ZL-2401-005.pdf')