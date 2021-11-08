from manim import *


class VectorFieldScene(Scene):
    def construct(self):
        def function(pos): return np.sin(
            pos[1] / 2) * RIGHT + np.cos(pos[0] / 2) * UP

        axes = Axes()

        vector_field = ArrowVectorField(
            function,
            colors=[YELLOW, GREEN],
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            length_func=lambda x: x / 2
        )
        self.add(vector_field)

        dot = Dot(point=(ORIGIN+UP+RIGHT))
        dot2 = Dot(point=(ORIGIN+UP+LEFT*3))
        # vector_field.nudge(dot, -2, 90)
        dot.add_updater(vector_field.get_nudge_updater())
        dot2.add_updater(vector_field.get_nudge_updater())

        self.add(axes, dot, dot2)
        self.wait(6)

        stream_lines = StreamLines(
            function, stroke_width=3,
            max_anchors_per_line=30
        ).scale(0.8)

        self.add(stream_lines)
        stream_lines.start_animation(warm_up=True, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
        self.wait(5)

        self.remove(stream_lines)
