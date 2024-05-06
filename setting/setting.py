"""
@Description: 
@Author: Shen Du
@Date: 2024-04-21 22:55:08
@LastEditTime: 2024-04-22 14:53:17
@LastEditors: Shen Du
"""

# 爬取文件信息
file_info = {
    "2023.txt": "https://www.gov.cn/yaowen/liebiao/202403/content_6939276.htm?pc",
    "2022.txt": "https://www.gov.cn/xinwen/2023-03/15/content_5746959.htm",
    "2021.txt": "https://www.gov.cn/xinwen/2022-03/13/content_5678833.htm",
}
# 停用词路径
stop_words_path = "setting\stop_words.txt"
# 特殊名词表
special_word_list = []
# 字体路径
font_path = "setting\font\STXINGKA.TTF"
# 词云图背景
background_img = "setting\\back_img\\heart.png"
# 柱状图读取词数
bar_nums = 10
# 饼图读取词数
pie_nums = 8
# 词云显示词数
word_cloud_nums = 100
# 词云形状
word_cloud_shape = [
    "circle",
    "cardioid",
    "diamond",
    "triangle-forward",
    "triangle",
    "pentagon",
    "star",
]
# 可视化文件路径
visualization_path = "output\html\data_visual.html"
# 可视化文件渲染布局文件路径
visualization_render_path = (
    "output\html\chart_config.json"
)
