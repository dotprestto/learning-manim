from manim import *

# from Brian Amedee in https://youtu.be/iHKrhtuhYss


class Conics(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[0, 4.1, 1],
            y_range=[-4, 4.1, 1],
            z_range=[-4, 4.1, 1],
            x_length=5,
            y_length=5,
            z_length=5,
            axis_config={
                "decimal_number_config": {
                    "num_decimal_places": 0
                }
            }
        ).to_edge(LEFT).add_coordinates()

        graph = axes.plot(
            lambda x: 0.25*x**2,
            x_range=[0, 4],
            color=YELLOW,
        )

        surface = always_redraw(
            lambda: Surface(
                lambda u, v: axes.c2p(
                    v, 0.25*v**2*np.cos(u), 0.25*v**2*np.sin(u)),
                u_range=[0, TAU],
                v_range=[0, 4],
                checkerboard_colors=[BLUE_B, BLUE_D],
            )
        )

        dx = ValueTracker(1)
        conic_approx = always_redraw(
            lambda: get_conic_approximations(
                axes=axes, graph=graph, x_range=[0, 4], dx=dx.get_value()
            )
        )

        num_text = MathTex(r"dx=").next_to(axes, UP, buff=0.5)
        num = always_redraw(
            lambda: DecimalNumber().set_value(dx.get_value()).next_to(num_text, RIGHT, buff=0.1)
        )

        axes2 = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 60, 10],
            x_length=5,
            y_length=6,
        ).to_edge(DR)

        def surface_area(x):
            return TAU * x * (1 + (x**2/4))**0.5

        graph2 = axes2.plot(
            surface_area, x_range=[0, 4], color=BLUE
        )
        graph2_label = Tex("Surface Area Function").next_to(
            axes2, UP, buff=0.2)

        # Bowness in the surface area of conics, mathematically incorrect
        # but the animation works
        theta = ValueTracker(45)
        truncated_area = always_redraw(
            lambda: get_rieman_truncated_cones(
                axes=axes2, graph=graph2, dx=dx.get_value(),
                x_range=[0, 4], theta=theta.get_value()
            )
        )

        self.set_camera_orientation(phi=0*DEGREES, theta=-90*DEGREES)
        self.add(axes, graph, surface, conic_approx, num_text, num)
        self.move_camera(phi=30*DEGREES, theta=-100*DEGREES,)
        self.begin_ambient_camera_rotation(rate=0.01)
        self.play(
            LaggedStart(
                Create(conic_approx),
                Write(VGroup(num_text, num)),
                DrawBorderThenFill(axes2),
                run_time=2,
                lag_ratio=0.25
            )
        )
        self.play(ReplacementTransform(
            conic_approx.copy(), truncated_area), run_time=1)
        self.play(dx.animate.set_value(0.1), theta.animate.set_value(5), run_time=3)
        self.add(graph2, graph2_label)
        self.wait()


def get_conic_approximations(axes, graph, x_range, dx, color_a=RED, color_b=GREEN, opacity=1):
    approximations=VGroup()

    for x in np.arange(x_range[0] + dx, x_range[1] + dx, dx):
        k=graph.underlying_function(x)
        if k < 0:
            k=0
            conic_surface=VectorizedPoint()
        else:
            conic_surface=Surface(
                lambda u, v: axes.c2p(v, k*v*np.cos(u), k*v*np.sin(u)),
                u_range=[0, TAU],
                v_range=[x - dx, x],
                checkerboard_colors=[color_a, color_b],
                fill_opacity=opacity,
            )
        approximations.add(conic_surface)

    return approximations


def get_rieman_truncated_cones(
    axes, graph, x_range, dx, color_a=RED, color_b=GREEN, opacity=1,
    stroke_color=WHITE, stroke_width=1, theta=45
):
    truncated_cones=VGroup()

    for x in np.arange(x_range[0], x_range[1], dx):
        points=VGroup()
        p1=axes.c2p(x + dx, 0)
        p2=axes.c2p(x + dx, graph.underlying_function(x + dx))
        p3=axes.c2p(x, graph.underlying_function(x))
        p4=axes.c2p(x, 0)
        truncated_conic=ArcPolygon(
            p1, p2, p3, p4,
            stroke_color=stroke_color,
            stroke_width=stroke_width,
            fill_color=[color_a, color_b],
            fill_opacity=opacity,
            arc_config=[
                {"angle": theta*DEGREES, "color": stroke_color},
                {"angle": 0, "color": stroke_color},
                {"angle": -theta*DEGREES, "color": stroke_color},
                {"angle": 0, "color": stroke_color},
            ]
        )
        truncated_cones.add(truncated_conic)
    return truncated_cones
