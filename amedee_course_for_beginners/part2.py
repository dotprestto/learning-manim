from manim import *


class Testing(Scene):
    def construct(self):
        # to_edge puts the obj to UL (UP LEFT) edge of the screen
        # buff tells the obj to not touch the edge by 0.5 of the unit
        name = Tex("My Name").to_edge(UL, buff=0.5)

        # shifts obj 3 times the unit to the left
        square = Square(side_length=0.5, fill_color=GREEN,
                        fill_opacity=0.75).shift(LEFT*3)

        # creates a triangle and scales to 0.6 of it's original size
        # set position do DR (DOWN RIGHT) edge
        triangle = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))

        # DrawBorderThenFill doesn't work if fill_opacity is not set
        self.play(DrawBorderThenFill(square), run_time=2)

        self.play(Create(triangle))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time=2)

        # animates simultaneously
        self.play(square.animate.scale(2),
                  triangle.animate.to_edge(DL), run_time=3)
        self.wait()
