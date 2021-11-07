from manim import *

# from Brian Amedee in https://youtu.be/Yf9QnATooqA


class Matrix(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            show_basis_vectors=True,
            leave_ghost_vectors=True
        )

    def construct(self):
        matrix = [[1, 2], [2, 1]]

        matrix_tex = (
            MathTex(
                r"A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}"
            )
            .to_edge(UL)
            .add_background_rectangle()
        )

        unit_square = self.get_unit_square()
        text = always_redraw(
            lambda: Tex("Det(A)")
            .set(width=0.7)
            .move_to(
                unit_square.get_center()
            )
        )

        vect = self.get_vector([1, -2], color=PURPLE_B)

        rect1 = Rectangle(
            height=2, width=1, stroke_color=BLUE_A,
            fill_color=BLUE_D, fill_opacity=0.6
        ).shift(2*UP + 2*LEFT)

        circ1 = Circle(
            radius=1, stroke_color=BLUE_A,
            fill_color=BLUE_D, fill_opacity=0.6
        ).shift(2*DOWN + 1*RIGHT)

        self.add_transformable_mobject(vect, unit_square, rect1, circ1)
        self.add_background_mobject(matrix_tex, text)
        self.apply_matrix(matrix)

        self.wait()
