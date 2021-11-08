from manim import *

# from Brian Amedee in https://youtu.be/FEtYAw3sI9Y


class Surfaces2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        axes = ThreeDAxes()

        graph = axes.plot(
            lambda x: x,
            x_range=[0, 3],
            color=RED_B,
        )

        area = axes.get_area(graph=graph, x_range=[0, 3])

        e = ValueTracker(0)

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(v, v*np.cos(u), v*np.sin(u)),
                u_range=[0, e.get_value()],
                v_range=[0, 3],
                checkerboard_colors=[GREEN, PURPLE]
            )
        )

        self.add(axes, surface)
        self.begin_ambient_camera_rotation(
            rate=PI/15
        )
        self.play(
            LaggedStart(
                Create(graph), Create(area)
            )
        )
        self.play(
            Rotating(
                area,
                axis=RIGHT,
                radians=TAU,
                about_point=axes.c2p(0, 0, 0)
            ),
            e.animate.set_value(TAU),
            run_time=6,
            rate_func=linear
        )
        self.stop_ambient_camera_rotation()
        self.wait()
