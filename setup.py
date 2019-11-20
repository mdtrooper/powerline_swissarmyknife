import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="powerline_swissarmyknife",
    version="1.0.0",
    license="GPLv3+",
    author="Miguel de Dios Matias",
    author_email="tres.14159@gmail.com",
    description="A Powerline segment.This segment shows the execution of complex command line defined by user.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mdtrooper/powerline_swissarmyknife",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console"
    ],
    python_requires='>=3.7',
    platforms=['any']
)