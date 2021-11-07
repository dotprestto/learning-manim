from manim import *

# from Brian Amedee in https://youtu.be/Yf9QnATooqA


class Vectors(VectorScene):
    def construct(self):
        plane = self.add_plane(animate=True).add_coordinates()
        vector = self.add_vector([-3, -2], color=YELLOW)

        basis = self.get_basis_vectors()
        self.add(basis)
        self.vector_to_coords(vector=vector)

        vector2 = self.add_vector([2, 2])
        self.write_vector_coordinates(vector=vector2)
