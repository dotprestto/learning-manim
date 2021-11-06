# About

This project was created to learn Manim, I'm interested in using this powerful engine in my academic projects.

I am using [Manim Community](https://docs.manim.community/en/stable/index.html).

The tutorial I followed is from [Brian Amedee](https://www.youtube.com/channel/UCnNljeRcRb_Y7Ok_TNtgB2w) and you can find it [here](https://www.youtube.com/watch?v=KHGoFDB-raE).

Another good tutorial is from [Flammable Maths](https://www.youtube.com/channel/UCtAIs1VCQrymlAnw3mGonhw) and you can find it [here](https://www.youtube.com/watch?v=Jfgtl-AW5Oc).

## Installation on Ubuntu

### Requirements

As mentioned in the [docs](https://docs.manim.community/en/stable/installation/linux.html)

```bash
sudo apt update
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg xdg-utils
```

### LaTeX

You should install all libs to avoid errors even if it's heavy.

```bash
sudo apt install texlive texlive-latex-extra texlive-fonts-extra \
texlive-latex-recommended texlive-science texlive-fonts-extra tipa
```

### Installing the lib

For this project

```bash
pipenv install
```

If you don't want to use `pipenv` you can use `pip`. If you don't have `pip` you can install it with `sudo apt install python3-pip`

```bash
pip3 install manim
```

To run this project it's recommended to use `manim==0.12.0`.

## Installing in Other Operating Systems

You can check this videos

-   [Installation of ManimGL and ManimCE master versions (Windows/Mac/Linux) - 2021 Edition
    ](https://www.youtube.com/watch?v=Upztg_Bs-zs)

-   [The Manim Cast #1 - Installing 3B1B's Animation Engine 𝐌𝐚𝐧𝐢𝐦 on Mac and Windows [ feat. @vcubingx ]](https://www.youtube.com/watch?v=Jfgtl-AW5Oc&t=635s)

or you can check the [docs](https://docs.manim.community/en/stable/installation.html).

## Run

```bash
manim scene.py
```

Or

```bash
python3 -m manim scene.py
```
