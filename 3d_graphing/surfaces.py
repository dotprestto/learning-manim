from manim import *

# from Brian Amedee in https://youtu.be/FEtYAw3sI9Y


class Surfaces(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        axes = ThreeDAxes()

        graph = axes.plot(
            lambda x: x**2,
            x_range=[-2, 2]
        )
        # create a surface
        surface = ParametricSurface(
            lambda u, v: axes.c2p(v*np.cos(u), v*np.sin(u), 0.5*v**2),
            u_range=[0, TAU],  # 2 * PI
            v_range=[0, 3],
            checkerboard_colors=[GREEN, RED]
        )

        group = VGroup(axes, graph, surface)

        self.add(axes, graph)
        self.begin_ambient_camera_rotation(rate=PI/20)
        self.play(Create(surface))
        self.play(group.animate.shift(LEFT*5))
