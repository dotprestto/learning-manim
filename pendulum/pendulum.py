from manim import *

# from Brian Amedee in https://www.youtube.com/watch?v=E1EucyJhcLw


class Pendulum(Scene):
    def construct(self):
        time = ValueTracker(0)
        theta_max = 30 * DEGREES
        rod_length = 3
        g = 9.81  # gravity
        w = np.sqrt(g / rod_length)  # angular velocity
        T = 2 * np.pi / w  # period

        p_x = -2.5  # desired x of position
        p_y = 3  # desired y of position
        shift_req = p_x * RIGHT + p_y * UP

        theta = DecimalNumber().set_color(BLACK).move_to(10 * RIGHT)
        theta.add_updater(lambda m: m.set_value(
            theta_max * np.sin(time.get_value() * w)))

        self.add(theta)

        def get_line(x, y):
            line_here = Line(start=ORIGIN+shift_req,
                             end=x*RIGHT+y*UP+shift_req, color=GREY)
            global line_vertical
            line_vertical = DashedLine(
                start=line_here.get_start(), end=line_here.get_start() + rod_length * DOWN, color=GREY)
            return line_here

        line = always_redraw(
            lambda: get_line(
                rod_length*np.sin(theta.get_value()),
                -rod_length*np.cos(theta.get_value())
            )
        )

        self.add(line)
        self.add(line_vertical)

        def angle_arc(theta):
            global angle
            global arc_text

            if theta == 0:
                angle = VectorizedPoint().move_to(10*RIGHT)
                arc_text = VectorizedPoint().move_to(10*RIGHT)
            elif theta > 0:
                angle = Angle(line, line_vertical,
                              quadrant=(1, 1), other_angle=True, fill_opacity=0)
            elif theta < 0:
                angle = Angle(line, line_vertical,
                              quadrant=(1, 1), other_angle=False, fill_opacity=0)

            return angle

        angle = always_redraw(lambda: angle_arc(theta.get_value()))
        self.add(angle)

        arc_text = Tex(r"$\theta$").scale(0.5)
        arc_text.add_updater(lambda m: m.next_to(angle, DOWN))
        self.add(arc_text)

        def get_ball(x, y):
            dot = Dot(fill_color=BLUE, fill_opacity=1).move_to(
                x*RIGHT+y*UP+shift_req).scale(rod_length)
            return dot

        ball = always_redraw(
            lambda: get_ball(
                rod_length*np.sin(theta.get_value()),
                -rod_length*np.cos(theta.get_value())
            )
        )
        self.add(ball)

        self.play(time.animate.set_value(3*T), rate_func=linear, run_time=3*T)
