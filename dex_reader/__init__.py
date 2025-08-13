"""
DEX Vending Machine Log Reader

A comprehensive tool for parsing and analyzing DEX (Data Exchange) log files
from vending machines, extracting sales data, product information, and machine statistics.

This package provides:
- DEXReader: Main class for parsing DEX files
- Command-line interface for batch processing
- Data export to CSV format
- Sales analysis and reporting capabilities
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"
__license__ = "MIT"

# Import main classes and functions
from .core import DEXReader
from .cli import main

# Define what gets imported with "from dex_reader import *"
__all__ = [
    "DEXReader",
    "main",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

# Package metadata
__package_info__ = {
    "name": "dex-file-reader",
    "version": __version__,
    "description": "DEX vending machine log reader with comprehensive parsing and analysis capabilities",
    "url": "https://github.com/AVJdataminer/dex-file-reader",
    "license": __license__,
}
