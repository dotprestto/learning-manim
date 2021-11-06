from manim import *


class ValueTrackers(Scene):
    def construct(self):
        # ValueTrackers increases time of scene translation to video
        k = ValueTracker(5)
        num = always_redraw(lambda: DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()

        # rate_func=smooth starts slow, then speeds up, then slows down
        self.play(k.animate.set_value(0), run_time=5, rate_func=linear)
