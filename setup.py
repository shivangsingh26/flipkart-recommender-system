from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Flipkart-Product-Recommendation-System',
    version='1.0.0',
    author='Shivang Singh',
    packages=find_packages(),
    install_requires=requirements,
)