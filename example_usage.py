#!/usr/bin/env python3
"""
Example usage of the DEX Reader program.

This script demonstrates how to use the DEXReader class to process
vending machine log files and extract sales information.
"""

from dex_reader import DEXReader
import os

def main():
    """Example usage of the DEX reader."""
    
    # Create a DEX reader instance
    reader = DEXReader()
    
    # Process all DEX files in the DEX-files directory
    print("Processing DEX files...")
    sales_data, machine_info = reader.process_multiple_files("DEX-files/*.log")
    
    # Save detailed sales data to CSV
    output_file = "dex_sales_detailed.csv"
    reader.save_to_csv(sales_data, output_file)
    
    # Print summary information
    reader.print_summary(sales_data, machine_info)
    
    # Display some sample data
    if sales_data:
        print("\n=== SAMPLE SALES DATA ===")
        for i, record in enumerate(sales_data[:5]):  # Show first 5 records
            print(f"Machine {record['machine_id']} - Slot {record['slot']}:")
            print(f"  Price: ${record['price_dollars']:.2f}")
            print(f"  Total vends: {record['total_vends']}")
            print(f"  Total sales: ${record['total_sales_dollars']:.2f}")
            if record['last_sale_date']:
                print(f"  Last sale: {record['last_sale_date']} at {record['last_sale_time']}")
            print()

if __name__ == "__main__":
    main() 