from manim import *

# from Brian Amedee in https://youtu.be/iHKrhtuhYss


class Revolutions(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0, theta=-90*DEGREES)
        text = Tex("Surface Area of a Solid Revolution?")
        self.play(Write(text))
        self.wait()
        self.play(FadeOut(text))

        self.begin_ambient_camera_rotation()
        self.set_camera_orientation(phi=45*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes(
            x_range=[0, 4.1, 1],
            y_range=[-4, 4.1, 1],
            z_range=[-4, 4.1, 1],
            x_length=5,
            y_length=5,
            z_length=5,
        ).add_coordinates()

        function = axes.plot(
            lambda x: 0.25*x**2,
            x_range=[0, 4],
            color=YELLOW
        )
        area = axes.get_area(
            graph=function,
            x_range=[0, 4],
            color=[BLUE_B, BLUE_D]
        )

        surface = Surface(
            lambda u, v: axes.c2p(v, 0.25*v**2*np.cos(u), 0.25*v**2*np.sin(u)),
            u_range=[0, TAU],
            v_range=[0, 4],
            checkerboard_colors=[BLUE_B, BLUE_D],
        )

        self.play(
            Create(function),
            Create(area),
            LaggedStart(
                Create(axes),

                Create(surface),
            ),
            run_time=4,
            lag_ratio=0.5
        )

        self.play(
            Rotating(
                VGroup(function, area),
                axis=RIGHT,
                radians=TAU,
                about_point=axes.c2p(0, 0, 0),
            )
        )
        self.wait(3)
