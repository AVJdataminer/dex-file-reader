#!/usr/bin/env python3
"""
DEX Vending Machine Log Reader

This program reads DEX (Data Exchange) log files from vending machines and extracts
detailed sales information including item counts, prices, and timestamps.

DEX files contain various record types:
- PA1: Product information (slot, price)
- PA2: Sales data (cash/cashless vends and revenue)
- PA5: Last sale date/time information
- EA2: Error/event information
"""

import os
import csv
import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import argparse
import glob


class DEXReader:
    """Class to parse and analyze DEX vending machine log files."""
    
    def __init__(self):
        self.records = []
        self.products = {}
        self.sales_data = []
        
    def parse_dex_file(self, file_path: str) -> Dict:
        """
        Parse a DEX log file and extract all records.
        
        Args:
            file_path: Path to the DEX log file
            
        Returns:
            Dictionary containing parsed records by type
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by lines and filter empty lines
        lines = [line.strip() for line in content.split('\n') if line.strip()]
        
        # Parse each line into record type and fields
        parsed_records = {}
        for line in lines:
            parts = line.split('*')
            if len(parts) < 2:
                continue
                
            record_type = parts[0]
            fields = parts[1:]
            
            if record_type not in parsed_records:
                parsed_records[record_type] = []
            
            parsed_records[record_type].append(fields)
        
        return parsed_records
    
    def extract_sales_data(self, parsed_records: Dict, machine_info: Dict = None) -> List[Dict]:
        """
        Extract detailed sales data from parsed records.
        
        Args:
            parsed_records: Dictionary of parsed records by type
            machine_info: Dictionary containing machine information
            
        Returns:
            List of dictionaries containing sales data
        """
        sales_data = []
        current_product = {}
        
        # Get machine ID for inclusion in sales records
        machine_id = machine_info.get('machine_id', 'Unknown') if machine_info else 'Unknown'
        
        # Process PA1 records (product information)
        if 'PA1' in parsed_records:
            for pa1_record in parsed_records['PA1']:
                if len(pa1_record) >= 2:
                    slot = pa1_record[0].strip()
                    price = pa1_record[1].strip()
                    
                    current_product = {
                        'slot': slot,
                        'price_cents': int(price) if price.isdigit() else 0,
                        'price_dollars': float(price) / 100 if price.isdigit() else 0.0
                    }
        
        # Process PA2 records (sales data)
        if 'PA2' in parsed_records:
            for i, pa2_record in enumerate(parsed_records['PA2']):
                if len(pa2_record) >= 4:
                    # Get corresponding product info if available
                    slot = f"Slot_{i+1}"  # Default slot name
                    if 'PA1' in parsed_records and i < len(parsed_records['PA1']):
                        slot = parsed_records['PA1'][i][0].strip()
                    
                    vends_cash = int(pa2_record[0]) if pa2_record[0].isdigit() else 0
                    cash_sales_cents = int(pa2_record[1]) if pa2_record[1].isdigit() else 0
                    vends_cashless = int(pa2_record[2]) if pa2_record[2].isdigit() else 0
                    cashless_sales_cents = int(pa2_record[3]) if pa2_record[3].isdigit() else 0
                    
                    # Get price from corresponding PA1 record
                    price_cents = 0
                    if 'PA1' in parsed_records and i < len(parsed_records['PA1']):
                        price_str = parsed_records['PA1'][i][1].strip()
                        price_cents = int(price_str) if price_str.isdigit() else 0
                    
                    sales_record = {
                        'machine_id': machine_id,
                        'slot': slot,
                        'price_cents': price_cents,
                        'price_dollars': price_cents / 100.0,
                        'vends_cash': vends_cash,
                        'cash_sales_cents': cash_sales_cents,
                        'cash_sales_dollars': cash_sales_cents / 100.0,
                        'vends_cashless': vends_cashless,
                        'cashless_sales_cents': cashless_sales_cents,
                        'cashless_sales_dollars': cashless_sales_cents / 100.0,
                        'total_vends': vends_cash + vends_cashless,
                        'total_sales_cents': cash_sales_cents + cashless_sales_cents,
                        'total_sales_dollars': (cash_sales_cents + cashless_sales_cents) / 100.0
                    }
                    
                    # Add last sale date/time if available
                    if 'PA5' in parsed_records and i < len(parsed_records['PA5']):
                        pa5_record = parsed_records['PA5'][i]
                        if len(pa5_record) >= 2 and pa5_record[0] and pa5_record[1]:
                            date_str = pa5_record[0]
                            time_str = pa5_record[1]
                            
                            # Parse DEX date format (YYMMDD) and time format (HHMM)
                            try:
                                if len(date_str) == 6 and len(time_str) == 4:
                                    year = 2000 + int(date_str[:2])
                                    month = int(date_str[2:4])
                                    day = int(date_str[4:6])
                                    hour = int(time_str[:2])
                                    minute = int(time_str[2:4])
                                    
                                    last_sale_datetime = datetime(year, month, day, hour, minute)
                                    sales_record['last_sale_datetime'] = last_sale_datetime
                                    sales_record['last_sale_date'] = last_sale_datetime.strftime('%Y-%m-%d')
                                    sales_record['last_sale_time'] = last_sale_datetime.strftime('%H:%M')
                                else:
                                    sales_record['last_sale_datetime'] = None
                                    sales_record['last_sale_date'] = date_str if date_str else ''
                                    sales_record['last_sale_time'] = time_str if time_str else ''
                            except (ValueError, IndexError):
                                sales_record['last_sale_datetime'] = None
                                sales_record['last_sale_date'] = date_str if date_str else ''
                                sales_record['last_sale_time'] = time_str if time_str else ''
                        else:
                            sales_record['last_sale_datetime'] = None
                            sales_record['last_sale_date'] = ''
                            sales_record['last_sale_time'] = ''
                    else:
                        sales_record['last_sale_datetime'] = None
                        sales_record['last_sale_date'] = ''
                        sales_record['last_sale_time'] = ''
                    
                    sales_data.append(sales_record)
        
        return sales_data
    
    def extract_machine_info(self, parsed_records: Dict) -> Dict:
        """
        Extract machine identification and summary information.
        
        Args:
            parsed_records: Dictionary of parsed records by type
            
        Returns:
            Dictionary containing machine information
        """
        machine_info = {}
        
        # Extract machine ID from ID1 record
        if 'ID1' in parsed_records and parsed_records['ID1']:
            id1_record = parsed_records['ID1'][0]
            if len(id1_record) >= 1:
                machine_info['machine_id'] = id1_record[0].strip()
        
        # Extract total sales from VA1 record
        if 'VA1' in parsed_records and parsed_records['VA1']:
            va1_record = parsed_records['VA1'][0]
            if len(va1_record) >= 4:
                machine_info['total_sales_cents'] = int(va1_record[0]) if va1_record[0].isdigit() else 0
                machine_info['total_vends'] = int(va1_record[1]) if va1_record[1].isdigit() else 0
                machine_info['total_sales_dollars'] = machine_info['total_sales_cents'] / 100.0
        
        return machine_info
    
    def process_dex_file(self, file_path: str) -> Tuple[List[Dict], Dict]:
        """
        Process a single DEX file and extract all relevant information.
        
        Args:
            file_path: Path to the DEX log file
            
        Returns:
            Tuple of (sales_data, machine_info)
        """
        parsed_records = self.parse_dex_file(file_path)
        machine_info = self.extract_machine_info(parsed_records)
        sales_data = self.extract_sales_data(parsed_records, machine_info)
        
        # Add file information
        machine_info['source_file'] = os.path.basename(file_path)
        machine_info['file_path'] = file_path
        
        return sales_data, machine_info
    
    def process_multiple_files(self, file_pattern: str) -> Tuple[List[Dict], List[Dict]]:
        """
        Process multiple DEX files matching a pattern.
        
        Args:
            file_pattern: Glob pattern to match DEX files
            
        Returns:
            Tuple of (all_sales_data, all_machine_info)
        """
        all_sales_data = []
        all_machine_info = []
        
        for file_path in glob.glob(file_pattern):
            try:
                sales_data, machine_info = self.process_dex_file(file_path)
                all_sales_data.extend(sales_data)
                all_machine_info.append(machine_info)
                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
        
        return all_sales_data, all_machine_info
    
    def save_to_csv(self, sales_data: List[Dict], output_file: str):
        """
        Save sales data to CSV file.
        
        Args:
            sales_data: List of sales data dictionaries
            output_file: Output CSV file path
        """
        if not sales_data:
            print("No sales data to save.")
            return
        
        df = pd.DataFrame(sales_data)
        df.to_csv(output_file, index=False)
        print(f"Sales data saved to: {output_file}")
    
    def print_summary(self, sales_data: List[Dict], machine_info: List[Dict]):
        """
        Print a summary of the processed data.
        
        Args:
            sales_data: List of sales data dictionaries
            machine_info: List of machine information dictionaries
        """
        if not sales_data:
            print("No sales data found.")
            return
        
        df = pd.DataFrame(sales_data)
        
        print("\n=== SALES SUMMARY ===")
        print(f"Total products: {len(df)}")
        print(f"Total vends: {df['total_vends'].sum()}")
        print(f"Total sales: ${df['total_sales_dollars'].sum():.2f}")
        print(f"Cash sales: ${df['cash_sales_dollars'].sum():.2f}")
        print(f"Cashless sales: ${df['cashless_sales_dollars'].sum():.2f}")
        
        print("\n=== TOP SELLING PRODUCTS ===")
        top_products = df.nlargest(10, 'total_vends')[['slot', 'total_vends', 'total_sales_dollars', 'price_dollars']]
        for _, row in top_products.iterrows():
            print(f"Slot {row['slot']}: {row['total_vends']} vends, ${row['total_sales_dollars']:.2f} revenue, ${row['price_dollars']:.2f} each")
        
        print("\n=== MACHINE INFORMATION ===")
        for info in machine_info:
            print(f"Machine ID: {info.get('machine_id', 'Unknown')}")
            print(f"File: {info.get('source_file', 'Unknown')}")
            print(f"Total machine sales: ${info.get('total_sales_dollars', 0):.2f}")
            print(f"Total machine vends: {info.get('total_vends', 0)}")
            print()


def main():
    """Main function to run the DEX reader."""
    parser = argparse.ArgumentParser(description='Read DEX vending machine log files')
    parser.add_argument('input', nargs='?', default='DEX-files/*.log', 
                       help='Input file or pattern (default: DEX-files/*.log)')
    parser.add_argument('-o', '--output', default='dex_sales_detailed.csv',
                       help='Output CSV file (default: dex_sales_detailed.csv)')
    parser.add_argument('--summary', action='store_true',
                       help='Print summary information')
    
    args = parser.parse_args()
    
    # Create DEX reader
    reader = DEXReader()
    
    # Process files
    if os.path.isfile(args.input):
        # Single file
        sales_data, machine_info = reader.process_dex_file(args.input)
        all_sales_data = sales_data
        all_machine_info = [machine_info]
    else:
        # Multiple files
        all_sales_data, all_machine_info = reader.process_multiple_files(args.input)
    
    # Save to CSV
    reader.save_to_csv(all_sales_data, args.output)
    
    # Print summary if requested
    if args.summary or not args.output:
        reader.print_summary(all_sales_data, all_machine_info)


if __name__ == "__main__":
    main() 