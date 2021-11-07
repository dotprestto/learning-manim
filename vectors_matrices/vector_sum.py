from typing import runtime_checkable
from manim import *

# from Brian Amedee in https://youtu.be/Yf9QnATooqA


class VectorSum(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=7,
        ).add_coordinates().shift(RIGHT*2)

        vect1 = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(3, 2),
            stroke_color=YELLOW
        ).add_tip()

        vect1_name = MathTex(r"\vec{v}").next_to(
            vect1, RIGHT, buff=0.1).set_color(YELLOW)

        vect2 = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(-2, 1),
            stroke_color=RED
        ).add_tip()

        vect2_name = MathTex(r"\vec{w}").next_to(
            vect2, RIGHT, buff=0.1).set_color(RED)

        vect3 = Line(
            start=plane.c2p(3, 2),
            end=plane.c2p(1, 3),
            stroke_color=RED
        ).add_tip()

        vect4 = Line(
            start=plane.c2p(0, 0),
            end=plane.c2p(1, 3),
            stroke_color=GREEN
        ).add_tip()

        vect4_name = MathTex(r"\vec{v} + \vec{w}").next_to(
            vect4, RIGHT, buff=0.1).set_color(GREEN)

        group = VGroup(
            plane,
            vect1, vect1_name,
            vect2, vect2_name,
            vect3, vect4, vect4_name
        )

        box = RoundedRectangle(
            height=1.5, width=1.5, corner_radius=0.1, stroke_color=PINK
        ).to_edge(DL)

        self.play(DrawBorderThenFill(plane), run_time=2)
        self.wait()

        self.play(GrowFromPoint(vect1, point=vect1.get_start()),
                  Write(vect1_name), run_time=2)
        self.wait()

        self.play(GrowFromPoint(vect2, point=vect2.get_start()),
                  Write(vect2_name), run_time=2)
        self.wait()

        self.play(Transform(vect2, vect3), vect2_name.animate.next_to(
            vect3, UP, buff=0.1), run_time=2)
        self.wait()

        self.play(
            LaggedStart(GrowFromPoint(vect4, point=vect4.get_start()),
                        Write(vect4_name)), run_time=2, lag_ratio=1)
        self.wait()

        self.add(box)
        self.wait()

        self.play(group.animate.move_to(
            box.get_center()).set(width=1.2), run_time=3)
        self.wait()
