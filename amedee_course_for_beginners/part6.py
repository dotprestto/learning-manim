from manim import *


class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 4], y_length=5) \
            .to_edge(DOWN) \
            .add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)")

        # plane.get_graph() is deprecated in v0.11.0, use plane.plot() instead
        parabola = plane.plot(
            lambda x: x**2, x_range=[-4, 4], color=GREEN)

        # label for function
        func_label = MathTex("f(x)={x}^{2}").scale(0.6).next_to(
            parabola, UR, buff=0.5).set_color(GREEN)

        # add area rectangles in a specified range with width = dx
        area = plane.get_riemann_rectangles(
            graph=parabola, x_range=[-2, 3], dx=0.2, stroke_width=0.1, stroke_color=YELLOW)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(labels, parabola, func_label)), run_time=3)
        self.wait()

        self.play(Create(area))
        self.wait()
