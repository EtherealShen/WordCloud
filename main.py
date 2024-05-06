'''
@Description: 
@Author: Shen Du
@Date: 2024-04-17 18:48:56
@LastEditTime: 2024-04-22 22:37:49
@LastEditors: Shen Du
'''

from data_crawled import data_crawled
from data_operation import data_operate
from data_visualization import data_visual


if __name__ == "__main__":
    # 爬取数据
    crawled = data_crawled()
    crawled.run()
    # 数据分割、清洗、存储
    operate = data_operate()
    operate.run(save="all")
    # 数据可视化
    view = data_visual()
    view.run()
