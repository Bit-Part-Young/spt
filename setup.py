from pathlib import Path
from typing import List

from setuptools import find_packages, setup

THIS_DIR = Path(__file__).parent

with open(THIS_DIR / "docs/description.md", encoding="utf-8") as f:
    long_description = f.read()


def read_requirements(filepath: Path) -> List[str]:
    with open(filepath, encoding="utf-8") as fd:
        return [
            package.strip("\n")
            for package in fd.readlines()
            if not package.startswith("#")
        ]


requirements = read_requirements(THIS_DIR / "requirements.txt")


setup(
    name="spt",
    version="0.2.0",
    description="Scientific matplotlib plot rcParams configuration template python package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="yangsl",
    author_email="3304839708@qq.com",
    url="https://gitee.com/yangsl306/spt",
    packages=find_packages(),
    zip_safe=False,
    install_requires=requirements,
    python_requires=">3.6",
    platforms=["all"],
)
