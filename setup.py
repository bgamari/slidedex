#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
        name = 'SlideDeX',
        version = '0.0.1',
        scripts = ['SlideDeX'],
        packages = ['slidedex'],
        dependencies = ['gtk', 'poppler', 'gtksourceview2', 'vte'],
        package_data = {
                'slidedex': ['mainwindow.glade'],
        },

        author = 'Robert Schroll',
        author_email = 'rschroll@gmail.com',
        description = 'An editor for LaTeX presentations',
        keywords = 'latex beamer presentation',
        url = 'https://github.com/rschroll/slidedex',
)

