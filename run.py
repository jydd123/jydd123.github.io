import os
from collections import defaultdict

# 获取当前工作目录
current_dir = os.getcwd()

# 拼接"html"文件夹的完整路径
html_folder_path = os.path.join(current_dir, "html")

# 获取当前目录下的所有HTML文件名
html_files = [file for file in os.listdir(html_folder_path) if file.endswith('.html')]

# 根据年份和日期对文件进行分组
file_groups = defaultdict(lambda: defaultdict(list))
for file in html_files:
    # 解析文件名格式为"年份-月份-日期_文件名.html"
    year, month, day = file.split('_')[0].split('-')
    file_groups[year][month + '-' + day].append(file)

# 生成HTML文件内容
html_content = ""
for year, months in sorted(file_groups.items(), reverse=True):
    html_content += f"<h3>{year}</h3>\n"
    html_content += "<ul>\n"
    for month_day, files in sorted(months.items(), reverse=True):
        for file in files:
            html_content += f'<li><a href="html/{file}">{file}</a></li>\n'
    html_content += "</ul>\n"

# 生成新的HTML文件
with open('8.微信文章.html', 'w') as f:
    f.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HTML Files List</title>
    </head>
    <body>
        <h1>List of HTML Files</h1>
        {html_content}
    </body>
    </html>
    """)

print("HTML文件列表已按年份和日期生成到'8.微信文章.html'文件中")
