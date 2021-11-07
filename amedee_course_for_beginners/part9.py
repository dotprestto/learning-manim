from manim import *


class Configs(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10, 2], y_range=[0, 10, 2],
                  x_length=7, y_length=7, axis_config={
            "include_members": True,
            "font_size": 30,
            "incluse_tip": True,
            "number_to_exclude": [0],
            "numbers_with_elongated_ticks": [0, 2]
        })

        self.add(ax)
        self.wait()
