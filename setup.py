from setuptools import setup, find_packages

setup(
    name="plotch",
    version="0.0.0.9",
    packages=find_packages(),
    description="Patchwork for matplotlib",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joseph Barbier",
    author_email="joseph.barbierdarnal@gmail.com",
    url="https://github.com/JosephBARBIERDARNAL/plotch/blob/main/README.md",
    install_requires=["matplotlib"],
)
