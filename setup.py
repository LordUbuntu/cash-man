from setuptools import setup, find_packages


with open("README.md", 'r') as f:
    long_description = f.read()


setup(
    name="cashman",
    version="0.0.0",  # SemVer... Major, Minor, Patch
    description="A cli tool to track personal expenses",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LordUbuntu/cash-man",
    license="Unlicense",
    author="Jacobus Burger",
    author_email="therealjacoburger@gmail.com",
    packages=find_packages(),
    install_requires=["rich==13.3.4", "click==8.1.3"],
)
