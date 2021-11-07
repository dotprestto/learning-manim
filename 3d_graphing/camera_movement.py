from manim import *

# from Brian Amedee in https://youtu.be/FEtYAw3sI9Y


class CameraMovement(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            y_range=[-6, 6, 1],
            x_range=[-6, 6, 1],
            z_range=[-6, 6, 1],
            x_length=8,
            y_length=6,
            z_length=6,
        )

        graph = axes.plot(
            lambda x: x**2,
            x_range=[-2, 2, 1],
            color=YELLOW,
        )

        rects = axes.get_riemann_rectangles(
            graph=graph,
            x_range=[-2, 2],
            dx=0.1,
            stroke_color=WHITE,

        )

        graph2 = axes.plot_parametric_curve(
            lambda t: np.array([np.cos(t), np.sin(t), t]),
            t_range=[-2*PI, 2*PI],
            color=RED
        )

        self.add(axes, graph, graph2)
        self.wait()

        # CAMERA DEFAULTS: PHI = 0 AND THETA = -90
        # PHI -> up and down movement
        # THETA -> left and right movement
        self.move_camera(phi=60*DEGREES)
        self.wait()
        self.move_camera(theta=-45*DEGREES)

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="theta"
        )  # rotation in radians per second

        self.wait()

        self.play(Create(rects), run_time=3)
        self.play(Create(graph2))
        self.wait()
        self.stop_ambient_camera_rotation()
        self.wait()

        self.begin_ambient_camera_rotation(
            rate=PI/10, about="phi"
        )
        self.wait(2)
        self.stop_ambient_camera_rotation()
