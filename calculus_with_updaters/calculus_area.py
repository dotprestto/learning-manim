from manim import *

# from Brian Amedee in https://www.youtube.com/watch?v=9dXuQx7wJM0


class CalculusArea(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5],
            x_length=8,
            y_range=[-10, 10],
            y_length=7,
        ).add_coordinates()

        graph = axes.plot(
            lambda x: 0.1 * (x - 4) * (x - 1) * (x - 3),
            color=YELLOW,
        )

        self.add(axes, graph)

        dx_list = [1, 0.5, 0.3, 0.1, 0.05, 0.025, 0.01]

        # Creates a VGroup list of riemann_rectangles
        # varying the dx from dx_list
        # using list comprehension -> [x for x in x_list] -> [x1, x2, ..., xn]
        # and spread operator (*[x1, x2, ..., xn]) -> (x1, x2, ..., xn)
        rectangles = VGroup(
            *[
                axes.get_riemann_rectangles(
                    graph=graph,
                    x_range=[-5, 5],
                    stroke_width=0.1,
                    stroke_color=WHITE,
                    dx=dx,
                )
                for dx in dx_list
            ]
        )

        first_area = rectangles[0]
        for i, _ in enumerate(dx_list[1:], start=1):
            new_area = rectangles[i]
            self.play(Transform(first_area, new_area), run_time=3)
            self.wait(0.5)

        self.wait()
