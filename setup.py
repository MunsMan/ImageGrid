#! /usr/bin/python3
from setuptools import setup, find_packages
from os import path
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')


install_requires = [x.strip() for x in all_reqs if (
    'git+' not in x) and (not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs
                    if 'git+' not in x]


setup(
    name='ImageGrid',
    description='A Command Line Application to split an Image into a Grid of Images',
    version='0.9.0',
    packages=find_packages() + find_packages(where="./grid"),  # list of all packages
    install_requires=install_requires,
    python_requires='>=3.6',  # any python greater than 2.7
    entry_points={'console_scripts': ['grid=grid.main:main']},
    author="Hendrik Munske",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/MunsMan/ImageGrid',
    download_url='https://github.com/MunsMan/ImageGrid.git',
    dependency_links=dependency_links,
    author_email='munsman.github@gmail.com',
)
