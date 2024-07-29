import pandas as pd

# 读取CSV文件
csv_file_path = 'ZL-2401-005.csv'  # 替换为您的CSV文件路径
df = pd.read_csv(csv_file_path, encoding='utf-8')

df['create_date'] = pd.to_datetime(df['create_date'], format='%d/%m/%Y %H:%M:%S')
df_sorted = df.sort_values(by='create_date')

# 选择需要的列
columns_to_include = ['theme', 'module', 'operator', 'create_date', 'status']  # 替换为您需要的列名
df_selected = df_sorted[columns_to_include]

# 自定义表头
custom_headers = ['主题', '分类', '操作者', '操作时间', '状态']  # 替换为您的自定义表头
df_selected.columns = custom_headers

# 自定义转换规则
def transform_column1(value):
    # 根据自定义规则转换 column1 的值
    if value == 0:
        return '未阅读已发送'
    elif value == 1:
        return '已阅读已发送'
    else:
        return 'N/A'
    
# 应用自定义转换规则
df_selected['状态'] = df_selected['状态'].apply(transform_column1)

# 生成Excel文件
excel_file_path = 'ZL-2401-005.xlsx'  # 生成的Excel文件路径
df_selected.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f"Excel文件已生成：{excel_file_path}")