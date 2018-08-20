import setuptools

with open('README.rst') as f:
    readme = f.read()

setuptools.setup(
    name="scinot",
    version="0.0.11",
    

    install_requires=['colorama'],

    author="David O'Connor",
    author_email="david.alan.oconnor@gmail.com",
    url='https://github.com/David-OConnor/scinot',
    description="Display numbers in scientific notation.",
    long_description=readme,
    license="MIT",
    keywords="scientific notation, exponential, REPL",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
    ],
)
