from manim import *

# from Brian Amedee in https://youtu.be/iHKrhtuhYss


class PrismNets(ThreeDScene):
    def construct(self):
        length = 2
        width = 4
        height = 1

        rect_prism = Prism(
            dimensions=[length, width, height]
        ).to_edge(LEFT, buff=1)

        kwargs = {
            "stroke_color": BLUE_D,
            "fill_color": BLUE_D,
            "fill_opacity": 0.8
        }

        bottom = Rectangle(width=width, height=length, **kwargs)

        s1 = Rectangle(height=height, width=width,
                       **kwargs).next_to(bottom, UP, buff=0)
        s2 = Rectangle(height=height, width=width,
                       **kwargs).next_to(bottom, DOWN, buff=0)
        l1 = Rectangle(height=length, width=height,
                       **kwargs).next_to(bottom, LEFT, buff=0)
        l2 = Rectangle(height=length, width=height,
                       **kwargs).next_to(bottom, RIGHT, buff=0)

        top = Rectangle(width=width, height=length,
                        **kwargs).next_to(s1, UP, buff=0)

        net = (
            VGroup(top, bottom, s1, s2, l1, l2)
            .rotate(-PI/2)
            .to_edge(RIGHT, buff=1)
        )

        arrow = Line(
            start=rect_prism.get_right(),
            end=net.get_left(),
            buff=0.2
        ).add_tip()

        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(phi=45*DEGREES, theta=-45*DEGREES)
        self.play(Create(rect_prism))
        self.play(
            LaggedStart(
                Create(arrow),
                Transform(rect_prism.copy(), net)
            ),
            run_time=2,
            lag_ratio=0.5
        )

        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))
        self.stop_ambient_camera_rotation()
