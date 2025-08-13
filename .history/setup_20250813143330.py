#!/usr/bin/env python3
"""
Setup script for DEX Vending Machine Log Reader

This package provides tools to parse and analyze DEX (Data Exchange) log files
from vending machines, extracting sales data, product information, and machine statistics.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements from requirements.txt
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Get version from the module
def get_version():
    version_file = os.path.join("dex_reader", "__init__.py")
    if os.path.exists(version_file):
        with open(version_file, "r", encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("__version__"):
                    return line.split("=")[1].strip().strip('"\'')
    return "1.0.0"

setup(
    name="dex-file-reader",
    version=get_version(),
    author="Your Name",
    author_email="your.email@example.com",
    description="A comprehensive tool for parsing and analyzing DEX vending machine log files",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/AVJdataminer/dex-file-reader",
    project_urls={
        "Bug Reports": "https://github.com/AVJdataminer/dex-file-reader/issues",
        "Source": "https://github.com/AVJdataminer/dex-file-reader",
        "Documentation": "https://github.com/AVJdataminer/dex-file-reader#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "notebook": [
            "jupyter>=1.0",
            "matplotlib>=3.3",
            "seaborn>=0.11",
            "plotly>=5.0",
        ],
        "full": [
            "jupyter>=1.0",
            "matplotlib>=3.3",
            "seaborn>=0.11",
            "plotly>=5.0",
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "dex-reader=dex_reader.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "dex_reader": ["*.txt", "*.md", "*.csv", "*.log"],
    },
    keywords="dex vending machine log parser analysis sales data",
    license="MIT",
    zip_safe=False,
)
