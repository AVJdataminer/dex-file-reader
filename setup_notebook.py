#!/usr/bin/env python3
"""
Setup script for DEX Analysis Tutorial Notebook

This script helps prepare the environment for running the Jupyter notebook.
It installs required dependencies and sets up the necessary files.
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages for the notebook."""
    print("📦 Installing required packages...")
    
    try:
        # Install notebook requirements
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "notebook_requirements.txt"])
        print("✅ Notebook requirements installed successfully!")
        
        # Install main requirements if not already installed
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Main requirements installed successfully!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    
    return True

def check_files():
    """Check if required files exist."""
    print("🔍 Checking required files...")
    
    required_files = [
        "dex_reader.py",
        "DEX-files/",
        "DEX_Analysis_Tutorial.ipynb"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing required files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    else:
        print("✅ All required files found!")
        return True

def run_sample_analysis():
    """Run a quick sample analysis to verify everything works."""
    print("🧪 Running sample analysis...")
    
    try:
        # Import and test our DEX reader
        from dex_reader import DEXReader
        
        reader = DEXReader()
        sales_data, machine_info = reader.process_multiple_files("DEX-files/*.log")
        
        print(f"✅ Sample analysis successful!")
        print(f"   - Processed {len(sales_data)} sales records")
        print(f"   - Found {len(machine_info)} machine(s)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error in sample analysis: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 Setting up DEX Analysis Tutorial Environment")
    print("=" * 50)
    
    # Check files
    if not check_files():
        print("\n❌ Setup failed: Missing required files")
        return False
    
    # Install requirements
    if not install_requirements():
        print("\n❌ Setup failed: Could not install requirements")
        return False
    
    # Test analysis
    if not run_sample_analysis():
        print("\n❌ Setup failed: Sample analysis failed")
        return False
    
    print("\n✅ Setup completed successfully!")
    print("\n📚 Next steps:")
    print("1. Start Jupyter: jupyter notebook")
    print("2. Open: DEX_Analysis_Tutorial.ipynb")
    print("3. Run all cells to see the analysis")
    print("\n🎯 The notebook will guide you through:")
    print("   - Understanding DEX file format")
    print("   - Reading and parsing data")
    print("   - Creating visualizations")
    print("   - Analyzing sales performance")
    print("   - Machine comparison insights")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 