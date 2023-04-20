from setuptools import setup, find_packages

setup(
    name="census",
    version='0.0.1',
    author='Harsha',
    author_email='harsha99ar@gmail.com',
    packages=find_packages(),
    install_requires = ["pandas","numpy","flask"]
    )