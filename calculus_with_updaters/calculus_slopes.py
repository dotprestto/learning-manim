from manim import *

# from Brian Amedee in https://www.youtube.com/watch?v=9dXuQx7wJM0


class CalculusSlopes(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-3, 3],
            y_range=[-4, 14],
            y_length=7,
            x_length=6
        ).add_coordinates()

        graph1 = plane.plot(lambda x: x**2, x_range=[-3, 3], color=RED)
        graph1_lab = (
            MathTex(r"f(x)={x}^{2}")
            .next_to(graph1, UR, buff=0.2)
            .set_color(RED)
            .scale(0.8)
        )

        c = ValueTracker(-4)

        graph2 = always_redraw(
            lambda: plane.plot(
                lambda x: x**2 + c.get_value(), x_range=[-3, 3], color=YELLOW
            )
        )

        graph2_lab = always_redraw(
            lambda: MathTex(r"f(x)={x}^{2}+c")
            .next_to(graph2, UR, buff=0.2)
            .set_color(RED)
            .scale(0.8)
        )

        k = ValueTracker(-3)

        dot1 = always_redraw(
            lambda: Dot().move_to(
                plane.c2p(
                    k.get_value(),
                    graph1.underlying_function(k.get_value())
                )
            )
        )

        dot2 = always_redraw(
            lambda: Dot().move_to(
                plane.c2p(
                    k.get_value(),
                    graph2.underlying_function(k.get_value())
                )
            )
        )

        slope1 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(),
                graph=graph1,
                dx=0.01,
                secant_line_length=5
            )
        )

        slope2 = always_redraw(
            lambda: plane.get_secant_slope_group(
                x=k.get_value(),
                graph=graph2,
                dx=0.01,
                secant_line_length=5
            )
        )

        self.play(
            LaggedStart(
                DrawBorderThenFill(plane),
                Create(graph1),
                Create(graph2),
                run_time=5,
                lag_ratio=1
            )
        )

        self.add(slope1, slope2, dot1, dot2, graph1_lab, graph2_lab)
        self.play(
            k.animate.set_value(0),
            c.animate.set_value(2),
            run_time=5,
            rate_func=linear
        )

        self.play(
            k.animate.set_value(3),
            c.animate.set_value(-2),
            run_time=5,
            rate_func=linear
        )

        self.wait()
