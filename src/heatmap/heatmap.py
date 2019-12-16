import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar

begin = datetime.date(2018, 1, 1)
end = datetime.date(2018, 12, 31)

data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(0, 300)]
    for i in range((end - begin).days + 1)
]


c = (
        Calendar()
        .add("", data, calendar_opts=opts.CalendarOpts(range_="2018"))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Yelp-Calendar-Heatmap"),
            visualmap_opts=opts.VisualMapOpts(
                max_=300,
                min_=0,
                orient="horizontal",
                is_piecewise=True,
                pos_top="230px",
                pos_left="100px",
            ),
        )
    )
c.render()


