"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="graysalgorithms",
    version="0.9.0",
    description="A series of algorithm challenges, derived from FreeCodeCamp.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikejgray/graysalgorithms",
    author="Mike Gray",
    author_email="mike@graywind.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="algorithm challenge challenges development",
    packages=find_packages(),
    python_requires="==3.7.*",
    extras_require={"test": ["pytest"]},
)
