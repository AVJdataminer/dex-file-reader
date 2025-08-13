#!/usr/bin/env python3
"""
Command Line Interface for DEX Vending Machine Log Reader

This module provides the CLI interface for processing DEX files from the command line.
"""

import os
import argparse
import sys
from .core import DEXReader


def main():
    """Main CLI function for the DEX reader."""
    parser = argparse.ArgumentParser(
        description='Read DEX vending machine log files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process all DEX files in the DEX-files directory
  dex-reader
  
  # Process a specific file
  dex-reader DEX-files/DEX-K3CT42152030316-081300-080425-SCHEDULED.log
  
  # Process files with a custom pattern
  dex-reader "*.log"
  
  # Save to a custom output file
  dex-reader -o my_sales_report.csv
  
  # Print summary information
  dex-reader --summary
  
  # Process multiple specific files
  dex-reader file1.log file2.log file3.log
        """
    )
    
    parser.add_argument(
        'input', 
        nargs='*', 
        default=['DEX-files/*.log'],
        help='Input file(s) or pattern (default: DEX-files/*.log)'
    )
    
    parser.add_argument(
        '-o', '--output', 
        default='dex_sales_detailed.csv',
        help='Output CSV file (default: dex_sales_detailed.csv)'
    )
    
    parser.add_argument(
        '--summary', 
        action='store_true',
        help='Print summary information'
    )
    
    parser.add_argument(
        '--version', 
        action='version', 
        version='%(prog)s 1.0.0'
    )
    
    args = parser.parse_args()
    
    # Create DEX reader
    reader = DEXReader()
    
    # Process files
    all_sales_data = []
    all_machine_info = []
    
    if len(args.input) == 1 and '*' in args.input[0]:
        # Single pattern - use glob
        pattern = args.input[0]
        print(f"Processing files matching pattern: {pattern}")
        all_sales_data, all_machine_info = reader.process_multiple_files(pattern)
    else:
        # Multiple specific files
        print(f"Processing {len(args.input)} specific files:")
        for file_path in args.input:
            if os.path.isfile(file_path):
                try:
                    sales_data, machine_info = reader.process_dex_file(file_path)
                    all_sales_data.extend(sales_data)
                    all_machine_info.append(machine_info)
                    print(f"  ✅ {file_path}")
                except Exception as e:
                    print(f"  ❌ Error processing {file_path}: {e}")
            else:
                print(f"  ⚠️  File not found: {file_path}")
    
    if not all_sales_data:
        print("\n❌ No sales data found. Check your input files and try again.")
        sys.exit(1)
    
    # Save to CSV
    if args.output:
        reader.save_to_csv(all_sales_data, args.output)
    
    # Print summary if requested or if no output file specified
    if args.summary or not args.output:
        reader.print_summary(all_sales_data, all_machine_info)
    
    print(f"\n✅ Processing complete!")
    print(f"   Total records: {len(all_sales_data)}")
    print(f"   Machines processed: {len(all_machine_info)}")
    if args.output:
        print(f"   Output saved to: {args.output}")


if __name__ == "__main__":
    main()
