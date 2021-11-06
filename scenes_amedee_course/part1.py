from manim import *


class Pith(Scene):
    def construct(self):
        sq = Square(side_length=5, stroke_color=GREEN,
                    fill_color=BLUE, fill_opacity=0.75)
        # run_time=3 tells the animation to run for 3 seconds
        self.play(Create(sq), run_time=3)
        self.wait()  # wait for 1 second
