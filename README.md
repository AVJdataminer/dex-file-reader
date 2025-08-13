# DEX Vending Machine Log Reader

This program reads DEX (Data Exchange) log files from vending machines and extracts detailed sales information including item counts, prices, and timestamps.

## Features

- **Comprehensive Data Extraction**: Parses all relevant DEX record types (PA1, PA2, PA5, etc.)
- **Sales Analysis**: Extracts cash and cashless sales data with revenue calculations
- **Timestamp Processing**: Converts DEX date/time formats to readable timestamps
- **Multiple File Support**: Process single files or multiple files using glob patterns
- **CSV Export**: Saves detailed sales data to CSV format
- **Summary Reports**: Provides sales summaries and top-selling product analysis

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Process all DEX files in the DEX-files directory:
```bash
python dex_reader.py
```

Process a specific file:
```bash
python dex_reader.py DEX-files/DEX-K3CT42152030316-081300-080425-SCHEDULED.log
```

Process files with a custom pattern:
```bash
python dex_reader.py "*.log"
```

Save to a custom output file:
```bash
python dex_reader.py -o my_sales_report.csv
```

Print summary information:
```bash
python dex_reader.py --summary
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

### Example Usage

Run the example script:
```bash
python example_usage.py
```

### Jupyter Notebook Tutorial

For a comprehensive tutorial with data visualizations and analysis:

1. **Setup the environment:**
```bash
python setup_notebook.py
```

2. **Start Jupyter:**
```bash
jupyter notebook
```

3. **Open the tutorial notebook:**
   - Open `DEX_Analysis_Tutorial.ipynb`
   - Run all cells to see the complete analysis

The notebook includes:
- 📊 **Data Visualizations**: Charts and graphs of sales performance
- 📈 **Performance Analysis**: Machine comparison and product insights
- 🎯 **Advanced Analytics**: Revenue efficiency and trend analysis
- 📋 **Step-by-step Tutorial**: Understanding DEX file format and parsing

## Output Format

The program generates a CSV file with the following columns:

- **machine_id**: Machine identification number
- **slot**: Product slot identifier
- **price_cents**: Price in cents
- **price_dollars**: Price in dollars
- **vends_cash**: Number of cash vends
- **cash_sales_cents**: Cash sales in cents
- **cash_sales_dollars**: Cash sales in dollars
- **vends_cashless**: Number of cashless vends
- **cashless_sales_cents**: Cashless sales in cents
- **cashless_sales_dollars**: Cashless sales in dollars
- **total_vends**: Total number of vends
- **total_sales_cents**: Total sales in cents
- **total_sales_dollars**: Total sales in dollars
- **last_sale_datetime**: Last sale datetime object
- **last_sale_date**: Last sale date (YYYY-MM-DD)
- **last_sale_time**: Last sale time (HH:MM)

## DEX File Format

DEX files contain various record types separated by asterisks (*):

- **PA1**: Product information (slot, price)
- **PA2**: Sales data (cash/cashless vends and revenue)
- **PA5**: Last sale date/time information
- **ID1**: Machine identification
- **VA1**: Total machine sales summary
- **EA2**: Error/event information

## Sample Output

```
=== SALES SUMMARY ===
Total products: 15
Total vends: 156
Total sales: $156.00
Cash sales: $156.00
Cashless sales: $0.00

=== TOP SELLING PRODUCTS ===
Slot 041: 35 vends, $26.25 revenue, $0.75 each
Slot 035: 17 vends, $17.00 revenue, $1.00 each
Slot 030: 12 vends, $12.00 revenue, $1.00 each
Slot 032: 12 vends, $12.00 revenue, $1.00 each
Slot 020: 24 vends, $24.00 revenue, $1.00 each

=== MACHINE INFORMATION ===
Machine ID: WTN11241500105
File: DEX-K3CT42152030316-081300-080425-SCHEDULED.log
Total machine sales: $197.25
Total machine vends: 213
```

## Files Created

1. `dex_reader.py` - Main program with comprehensive DEX parsing
2. `requirements.txt` - Dependencies (pandas)
3. `example_usage.py` - Example script showing usage
4. `README.md` - Complete documentation
5. `dex_sales_detailed.csv` - Generated detailed sales report
6. `DEX_Analysis_Tutorial.ipynb` - Comprehensive Jupyter notebook tutorial
7. `notebook_requirements.txt` - Additional dependencies for the notebook
8. `setup_notebook.py` - Setup script for the notebook environment

## Requirements

- Python 3.6+
- pandas >= 1.3.0

## License

This project is open source and available under the MIT License. 