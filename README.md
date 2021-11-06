# About

This project was created to learn Manim, I'm interested in using this powerful engine in my academic projects.

The tutorial I followed is from Brian Amedee and you can find it [here](https://www.youtube.com/watch?v=KHGoFDB-raE).

Another good tutorial is from [Flammable Maths](https://www.youtube.com/channel/UCtAIs1VCQrymlAnw3mGonhw) and you can find it [here](https://www.youtube.com/watch?v=Jfgtl-AW5Oc).

## Requirements

As mentioned in the [docs](https://3b1b.github.io/manim/getting_started/installation.html)

```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg xdg-utils

```

## LaTeX

You should install all libs to avoid errors even if it's heavy.

```bash
sudo apt install texlive texlive-latex-extra texlive-fonts-extra \
texlive-latex-recommended texlive-science texlive-fonts-extra tipa
```

## Installing dependencies

```bash
pipenv install
```

## Run

```bash
manim scene.py
OR
python3 -m manim scene.py
```
