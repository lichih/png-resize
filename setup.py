# coding:utf-8
from setuptools import setup, find_packages
from os import path
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='png-resize',
    version='0.1',
    description='Batch PNG Resize Tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://bobo.4649.tw/',
    author='Li-chih Wu',
    author_email='lichihwu@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'tqdm',
        'pillow',
        'optimage',
    ],
)
