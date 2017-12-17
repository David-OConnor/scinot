from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name="scinot",
    version="0.0.1",
    packages=find_packages(),

    install_requires=[],

    author="David O'Connor",
    author_email="david.alan.oconnor@gmail.com",
    url='https://github.com/David-OConnor/fplot',
    description="Express numbers in scientific notation.",
    long_description=readme,
    license="MIT",
    keywords="scientific notation, exponential",
)
