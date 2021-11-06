# Requirements

As mentioned in the [docs](https://3b1b.github.io/manim/getting_started/installation.html)

```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg xdg-utils

```

# LaTeX

You should install all libs to avoid errors even if it's heavy.

```bash
sudo apt install texlive texlive-latex-extra texlive-fonts-extra \
texlive-latex-recommended texlive-science texlive-fonts-extra tipa
```

# Installing dependencies

```bash
pipenv install
```

## Run

```bash

manim scene.py
OR
python3 -m manim scene.py
```
