from setuptools import setup, find_packages

requirements = []
with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.readlines()

setup(
    name='search_engines',
    version='0.5',
    description='Search Engines Scraper',
    author='Tasos M. Adamopoulos',
    license='MIT',
    packages=find_packages(),
    install_requires=requirements
)
