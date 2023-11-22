from distutils.core import setup

from setuptools import find_packages

setup(
    name="spt",
    version="0.1.5",
    description="Scientific matplotlib plot template python module.",
    author="yangsl",
    author_email="3304839708@qq.com",
    url="https://gitee.com/yangsl306/spt",
    packages=find_packages(),
    zip_safe=False,
    install_requires=["matplotlib>=3.7,<3.8"],
    platforms=["all"],
)
