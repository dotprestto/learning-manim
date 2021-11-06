from manim import *


class Updaters(Scene):
    def construct(self):
        num = MathTex("ln(2)")
        box = always_redraw(lambda: SurroundingRectangle(
            num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5))

        # next_to puts the object next and bellow (DOWN) to box obj
        name = always_redraw(lambda: Tex(
            "My Name").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT*2), run_time=2)
        self.wait()
