import setuptools


with open("README.md", 'r') as f:
    long_description = f.read()


setuptools.setup(
    name="cashman",
    version="0.0.0",  # SemVer... Major, Minor, Patch
    description="track personal expenses",
    long_description=long_description,
    license="Unlicense",
    author="Jacobus Burger",
    author_email="therealjacoburger@gmail.com",
    packages=["cashman"],
    install_requires=["rich==13.3.4", "click==8.1.3"],
)
