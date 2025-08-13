# Installation Guide for DEX File Reader

This guide will walk you through installing the DEX File Reader package and getting started with analyzing vending machine log files.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation Options

### Option 1: Install from Source (Recommended for Development)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AVJdataminer/dex-file-reader.git
   cd dex-file-reader
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package:**
   ```bash
   # Basic installation
   pip install -e .
   
   # With notebook support (for Jupyter notebooks)
   pip install -e ".[notebook]"
   
   # With development tools
   pip install -e ".[dev]"
   
   # With all dependencies
   pip install -e ".[full]"
   ```

### Option 2: Install from PyPI (When Available)

```bash
pip install dex-file-reader
```

### Option 3: Using Make (if you have Make installed)

```bash
# Quick start with all dependencies
make quickstart

# Install with specific dependency sets
make install-notebook  # For Jupyter notebook support
make install-dev       # For development tools
make install-full      # For everything
```

## Verification

After installation, verify that everything works:

```bash
# Test the package structure
python test_package.py

# Test importing
python -c "from dex_reader import DEXReader; print('✅ Package imported successfully!')"

# Test the command-line interface
dex-reader --help
```

## Usage Examples

### Command Line Interface

```bash
# Process all DEX files in the DEX-files directory
dex-reader

# Process a specific file
dex-reader DEX-files/sample.log

# Save to custom output file
dex-reader -o my_report.csv

# Show summary information
dex-reader --summary
```

### Python API

```python
from dex_reader import DEXReader

# Create reader instance
reader = DEXReader()

# Process a single file
sales_data, machine_info = reader.process_dex_file("path/to/dex_file.log")

# Process multiple files
sales_data, machine_info = reader.process_multiple_files("DEX-files/*.log")

# Save to CSV
reader.save_to_csv(sales_data, "output.csv")

# Print summary
reader.print_summary(sales_data, machine_info)
```

### Jupyter Notebook

```python
# Import and use in Jupyter
from dex_reader import DEXReader
import pandas as pd

reader = DEXReader()
sales_data, machine_info = reader.process_multiple_files("DEX-files/*.log")

# Convert to DataFrame for analysis
df = pd.DataFrame(sales_data)
print(f"Processed {len(df)} sales records")
```

## Dependencies

### Core Dependencies (Always Installed)
- `pandas>=1.3.0` - Data manipulation and analysis
- `numpy>=1.20.0` - Numerical computing

### Optional Dependencies

#### Notebook Support (`[notebook]`)
- `jupyter>=1.0` - Jupyter notebook environment
- `matplotlib>=3.3` - Basic plotting
- `seaborn>=0.11` - Statistical data visualization
- `plotly>=5.0` - Interactive plotting

#### Development Tools (`[dev]`)
- `pytest>=6.0` - Testing framework
- `pytest-cov>=2.0` - Coverage reporting
- `black>=21.0` - Code formatting
- `flake8>=3.8` - Code linting
- `mypy>=0.800` - Type checking

#### Full Installation (`[full]`)
- All dependencies from both `[notebook]` and `[dev]`

## Troubleshooting

### Common Issues

1. **Import Error: No module named 'pandas'**
   - Solution: Install dependencies with `pip install -e ".[notebook]"`

2. **Permission Denied**
   - Solution: Use virtual environment or add `--user` flag

3. **SSL Certificate Errors**
   - Solution: Update pip and setuptools, or use `--trusted-host pypi.org`

4. **Package Not Found**
   - Solution: Ensure you're in the correct directory and virtual environment is activated

### Getting Help

- Check the [README.md](README.md) for detailed usage information
- Run `python test_package.py` to diagnose package issues
- Use `make help` to see all available commands
- Check the [GitHub issues](https://github.com/AVJdataminer/dex-file-reader/issues) for known problems

## Development Setup

For contributors and developers:

```bash
# Clone and setup development environment
git clone https://github.com/AVJdataminer/dex-file-reader.git
cd dex-file-reader

# Setup development environment
make setup-dev

# Run all checks
make check

# Format code
make format

# Run tests
make test
```

## Building and Distribution

```bash
# Build distribution packages
make build

# Clean build artifacts
make clean

# Publish to PyPI (requires authentication)
make publish
```

## Next Steps

After successful installation:

1. **Explore the examples:**
   - Run `python example_usage.py`
   - Check out the Jupyter notebooks

2. **Process your DEX files:**
   - Place your `.log` files in the `DEX-files/` directory
   - Run `dex-reader` to analyze them

3. **Customize the analysis:**
   - Modify the code in `dex_reader/core.py`
   - Create your own analysis scripts

4. **Contribute:**
   - Report bugs on GitHub
   - Submit pull requests
   - Improve documentation

## Support

- **Documentation**: [README.md](README.md)
- **Issues**: [GitHub Issues](https://github.com/AVJdataminer/dex-file-reader/issues)
- **Source Code**: [GitHub Repository](https://github.com/AVJdataminer/dex-file-reader)

---

**Happy DEX File Analysis! 🚀**
