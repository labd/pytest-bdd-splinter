import re

from setuptools import find_packages, setup

docs_require = ["mkdocs>=1.0.4", "mkdocs-material==4.4.0"]

install_requires = ["pytest>=4.0.0", "pytest-bdd>=3.0.0", "pytest-splinter>=2.0.0"]

tests_require = [
    "coverage==4.2",
    "Flask==1.0.3",
    # Linting
    "isort==4.2.5",
    "flake8==3.0.3",
    "flake8-blind-except==0.1.1",
    "flake8-debugger==1.4.0",
]

with open('README.md') as fh:
    long_description = re.sub(
        '<!-- start-no-pypi -->.*<!-- end-no-pypi -->\n', '', fh.read(), flags=re.M | re.S)

setup(
    name="pytest-bdd-splinter",
    version="0.2.0",
    description="Common steps for pytest bdd and splinter integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/labd/pytest-bdd-splinter",
    author="Lab Digital",
    author_email="opensource@labdigital.nl",
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={"docs": docs_require, "test": tests_require},
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    zip_safe=False,
    entry_points={},
)
