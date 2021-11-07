from manim import *

# from Brian Amedee in https://www.youtube.com/watch?v=kXqAme1jCmg


def get_horizontal_line_to_graph(axes, function, x, width, color):
    group = VGroup()
    line = DashedLine(
        start=axes.c2p(0, function.underlying_function(x)),
        end=axes.c2p(x, function.underlying_function(x)),
        stroke_width=width,
        stroke_color=color
    )

    dot = Dot().set_color(color).move_to(axes.c2p(x, function.underlying_function(x)))
    group.add(line, dot)
    return group


class Derivatives(Scene):
    def construct(self):
        k = ValueTracker(-3)

        # Setting plane 1
        plane1 = (
            NumberPlane(
                x_range=[-3, 4, 1],
                y_range=[-8, 9, 2],
                x_length=5,
                y_length=5,
            )
            .add_coordinates()
            .shift(LEFT * 3.5)
        )

        func1 = plane1.plot(
            lambda x: (1 / 3)*(x ** 3),
            x_range=[-3, 3],
            color=RED_C
        )

        func1_label = (
            MathTex(r"f(x)=\frac{1}{3} x^{3}")
            .set(width=2.5)
            .next_to(plane1, UP, buff=0.2)
            .set_color(RED_C)
        )

        moving_slope = always_redraw(
            lambda: plane1.get_secant_slope_group(
                x=k.get_value(),
                graph=func1,
                dx=0.05,
                secant_line_length=4,
                secant_line_color=YELLOW
            )
        )

        dot = always_redraw(
            lambda: Dot()
            .set_color(YELLOW)
            .move_to(
                plane1.c2p(
                    k.get_value(), func1.underlying_function(k.get_value())
                )
            )
        )

        # Setting plane 2
        plane2 = (
            NumberPlane(
                x_range=[-3, 4, 1],
                y_range=[0, 11, 2],
                x_length=5,
                y_length=5,
            )
            .add_coordinates()
            .shift(RIGHT * 3.5)
        )

        func2 = always_redraw(
            lambda: plane2.plot(
                lambda x: x ** 2,
                x_range=[-3, k.get_value()],
                color=GREEN
            )
        )

        func2_label = (
            MathTex(r"f'(x)={x}^2")
            .set(width=2.5)
            .next_to(plane2, UP, buff=0.2)
            .set_color(GREEN)
        )

        moving_h_line = always_redraw(
            lambda: get_horizontal_line_to_graph(
                axes=plane2, function=func2, x=k.get_value(), width=4, color=YELLOW
            )
        )

        slope_value_text = (
            Tex("Slope value: ")
            .next_to(plane1, DOWN, buff=0.1)
            .set_color(YELLOW)
            .add_background_rectangle()
        )

        slope_value = always_redraw(
            lambda: DecimalNumber(num_decimal_places=1)
            .set_value(func2.underlying_function(k.get_value()))
            .next_to(slope_value_text, RIGHT, buff=0.2)
            .set_color(YELLOW)
        ).add_background_rectangle()

        # Play
        self.play(
            LaggedStart(
                DrawBorderThenFill(plane1),
                DrawBorderThenFill(plane2),
                Create(func1),
                Write(func1_label),
                Write(func2_label),
                run_time=5,
                lag_ratio=0.5
            )
        )

        self.add(
            moving_slope, moving_h_line, func2,
            slope_value, slope_value_text, dot
        )

        self.play(k.animate.set_value(3), run_time=15, rate_func=linear)
        self.wait()
