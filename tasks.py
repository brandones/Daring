#!/usr/bin/env python

import os
from invoke import task

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

COLORS = ["Blue", "Brown", "Green", "Orange Dark", "Orange", "Purple", "Red"]


@task
def build(ctx):
    """Does something"""
    for color in COLORS:
        color_class = color.lower().replace(" ", "-")
        sed_cmd = "sed -i 's/body class=\"[^ ]*/body class=\"{}/' default.hbs".format(
            color_class
        )
        with ctx.cd(BASE_PATH):
            ctx.run(sed_cmd)
        zip_cmd = (
            "zip -r 'themes/Daring {}.zip' assets/ author.hbs default.hbs index.hbs "
            "LICENSE.md package.json page.hbs partials/ post.hbs tag.hbs"
        ).format(color)
        with ctx.cd(BASE_PATH):
            ctx.run(zip_cmd)
