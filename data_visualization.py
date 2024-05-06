"""
@Description: 
@Author: Shen Du
@Date: 2024-04-22 10:05:32
@LastEditTime: 2024-04-22 10:26:13
@LastEditors: Shen Du
"""

from pyecharts.charts import Bar, Pie, Page, WordCloud
from pyecharts import options as opts

from setting import setting as st


class data_visual:
    def __init__(self) -> None:
        self.dict = {"2023": {}, "2022": {}, "2021": {}}
        self.bar = None
        self.pie1 = None
        self.pie2 = None
        self.pie3 = None
        self.wordCloud1 = None
        self.wordCloud2 = None
        self.wordCloud3 = None

    def read_data(self, nums):
        self.dict = {"2023": {}, "2022": {}, "2021": {}}
        for i in range(1, 4):
            with open("./output/txt/202{}.txt".format(i), "r", encoding="utf-8") as f:
                for j, line in enumerate(f):
                    if j >= nums:
                        break
                    line = line.strip()
                    word, number = line.split(": ")
                    self.dict["202{}".format(i)][word] = int(number)
            f.close()

    def bar_generate(self):
        self.read_data(st.bar_nums)
        list_2023 = list(self.dict["2023"].values())
        list_2022 = list(self.dict["2022"].values())
        list_2021 = list(self.dict["2021"].values())
        self.bar = (
            Bar(init_opts=opts.InitOpts(width="1500px", height="800px", chart_id="bar"))
            .add_xaxis(list(self.dict["2023"].keys()))
            .add_yaxis("2023", list_2023)
            .add_yaxis("2022", list_2022)
            .add_yaxis("2021", list_2021)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="近三年出现频率最高的词",
                    pos_left="40%",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                ),
                toolbox_opts=opts.ToolboxOpts(),
                legend_opts=opts.LegendOpts(pos_top="10%"),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)),
            )
        )

    def pie_generate(self):
        self.read_data(st.pie_nums)
        list_2023 = list(self.dict["2023"].items())
        list_2022 = list(self.dict["2022"].items())
        list_2021 = list(self.dict["2021"].items())
        self.pie1 = (
            Pie(init_opts=opts.InitOpts(width="800px", height="500px", chart_id="pie1"))
            .add("", list_2023, center=["50%", "50%"])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2023关键词饼图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                    pos_left="25%",
                ),
                legend_opts=opts.LegendOpts(
                    pos_top="10%",
                    pos_left="85%",
                    orient="vertical",
                    textstyle_opts=opts.TextStyleOpts(font_size=20),
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b}: {c}", position="outside", font_size=20
                ),
            )
        )
        self.pie2 = (
            Pie(init_opts=opts.InitOpts(width="800px", height="500px", chart_id="pie2"))
            .add("", list_2022, center=["50%", "50%"])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2022关键词饼图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                    pos_left="35%",
                ),
                legend_opts=opts.LegendOpts(
                    pos_top="10%",
                    pos_left="90%",
                    orient="vertical",
                    textstyle_opts=opts.TextStyleOpts(font_size=20),
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b}: {c}", position="outside", font_size=20
                ),
            )
        )
        self.pie3 = (
            Pie(init_opts=opts.InitOpts(width="800px", height="500px", chart_id="pie3"))
            .add("", list_2021, center=["50%", "50%"])
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2021关键词饼图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=30),
                    pos_left="35%",
                ),
                legend_opts=opts.LegendOpts(
                    pos_top="10%",
                    pos_left="90%",
                    orient="vertical",
                    textstyle_opts=opts.TextStyleOpts(font_size=20),
                ),
            )
            .set_series_opts(
                label_opts=opts.LabelOpts(
                    formatter="{b}: {c}", position="outside", font_size=20
                ),
            )
        )

    def wordCloud_generate(self):
        self.read_data(st.word_cloud_nums)
        list_2023 = list(self.dict["2023"].items())
        list_2022 = list(self.dict["2022"].items())
        list_2021 = list(self.dict["2021"].items())
        self.wordCloud1 = (
            WordCloud(
                init_opts=opts.InitOpts(
                    width="1000px", height="1000px", chart_id="wordCloud1"
                )
            )
            .add("", list_2023, word_size_range=[20, 60], mask_image=st.background_img)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2023年报告词云图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=40),
                    pos_left="28%",
                )
            )
        )
        self.wordCloud2 = (
            WordCloud(
                init_opts=opts.InitOpts(
                    width="1000px", height="1000px", chart_id="wordCloud2"
                )
            )
            .add("", list_2022, word_size_range=[20, 60], mask_image=st.background_img)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2022年报告词云图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=40),
                    pos_left="28%",
                )
            )
        )
        self.wordCloud3 = (
            WordCloud(
                init_opts=opts.InitOpts(
                    width="1000px", height="100px", chart_id="wordCloud3"
                )
            )
            .add("", list_2021, word_size_range=[20, 60], mask_image=st.background_img)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="2021年报告词云图",
                    title_textstyle_opts=opts.TextStyleOpts(font_size=40),
                    pos_left="28%",
                )
            )
        )

    def page_generate(self):    
        page = Page(layout=Page.DraggablePageLayout)
        page.add(
            self.bar,
            self.pie1,
            self.pie2,
            self.pie3,
            self.wordCloud1,
            self.wordCloud2,
            self.wordCloud3,
        )
        page.render(st.visualization_path)

    def run(self):
        self.bar_generate()
        self.pie_generate()
        self.wordCloud_generate()
        self.page_generate()
        Page.save_resize_html(
            st.visualization_path,
            cfg_file=st.visualization_render_path,
            dest=st.visualization_path,
        )


if __name__ == "__main__":
    view = data_visual()
    view.run()
