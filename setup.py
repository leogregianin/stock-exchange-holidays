#!/usr/bin/env python
from setuptools import setup, find_packages


__description__ = "Worldwide Stock Exchange holidays (NYSE, CME, B3 and others)"
with open("README.md", "r") as fh:
    __long_description__ = fh.read()


setup(
    name='stock_exchange_holidays',
    version='0.1.0',
    author='Leonardo Gregianin',
    author_email='leogregianin@gmail.com',
    description=__description__,
    long_description=__long_description__,
    long_description_content_type="text/markdown",
    url='https://github.com/leogregianin/stock-exchange-holidays',
    zip_safe=False,
    python_requires='>=3.6',
    license='MIT',
    keywords="stock, holidays",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
