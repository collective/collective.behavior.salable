from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open(os.path.join("README.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "salable", "docs", "INSTALL.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "salable", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "salable", "docs", "CONTRIBUTORS.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "behavior", "salable", "docs", "CREDITS.rst")).read())


setup(
    name='collective.behavior.salable',
    version='0.4',
    description="Behavior to make content salable.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.behavior.salable/',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.behavior'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'plone.behavior',
        'plone.directives.form',
        'setuptools'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
