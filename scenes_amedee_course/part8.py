from manim import *

SVG_PATH = ""
IMG_PATH = ""


class SVGs(Scene):
    def construct(self):
        icon = SVGMobject(f"{SVG_PATH}/icon.svg")
        img = ImageMobject(f"{IMG_PATH}/image.png")

        self.play(DrawBorderThenFill(icon))
        self.play(FadeIn(img))
