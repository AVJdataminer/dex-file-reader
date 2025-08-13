#!/usr/bin/env python3
"""
Test script to verify the DEX reader package structure
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if the package can be imported correctly."""
    try:
        print("Testing package imports...")
        
        # Test importing the package
        import dex_reader
        print("✅ Package imported successfully")
        print(f"   Version: {dex_reader.__version__}")
        print(f"   Author: {dex_reader.__author__}")
        
        # Test importing the main class
        from dex_reader import DEXReader
        print("✅ DEXReader class imported successfully")
        
        # Test importing the CLI function
        from dex_reader import main
        print("✅ CLI main function imported successfully")
        
        # Test creating an instance
        reader = DEXReader()
        print("✅ DEXReader instance created successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_package_structure():
    """Test if the package structure is correct."""
    print("\nTesting package structure...")
    
    required_files = [
        "dex_reader/__init__.py",
        "dex_reader/core.py", 
        "dex_reader/cli.py",
        "setup.py",
        "pyproject.toml",
        "MANIFEST.in",
        "LICENSE",
        "README.md",
        "requirements.txt"
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - MISSING")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing {len(missing_files)} required files")
        return False
    else:
        print(f"\n✅ All {len(required_files)} required files present")
        return True

def test_basic_functionality():
    """Test basic functionality of the DEX reader."""
    print("\nTesting basic functionality...")
    
    try:
        from dex_reader import DEXReader
        
        # Create reader instance
        reader = DEXReader()
        
        # Test with a sample DEX file if available
        dex_files = [f for f in os.listdir("DEX-files") if f.endswith(".log")]
        
        if dex_files:
            sample_file = os.path.join("DEX-files", dex_files[0])
            print(f"   Testing with sample file: {dex_files[0]}")
            
            # Test parsing
            parsed_records = reader.parse_dex_file(sample_file)
            print(f"   ✅ Parsed {len(parsed_records)} record types")
            
            # Test machine info extraction
            machine_info = reader.extract_machine_info(parsed_records)
            print(f"   ✅ Extracted machine info: {machine_info.get('machine_id', 'Unknown')}")
            
            # Test sales data extraction
            sales_data = reader.extract_sales_data(parsed_records, machine_info)
            print(f"   ✅ Extracted {len(sales_data)} sales records")
            
        else:
            print("   ⚠️  No sample DEX files found for testing")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Functionality test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 DEX Reader Package Test Suite")
    print("=" * 50)
    
    # Run tests
    structure_ok = test_package_structure()
    imports_ok = test_imports()
    functionality_ok = test_basic_functionality()
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 50)
    
    if structure_ok and imports_ok and functionality_ok:
        print("🎉 ALL TESTS PASSED!")
        print("   Your package is ready for installation and distribution!")
    else:
        print("❌ SOME TESTS FAILED")
        if not structure_ok:
            print("   - Package structure issues detected")
        if not imports_ok:
            print("   - Import issues detected")
        if not functionality_ok:
            print("   - Functionality issues detected")
    
    print("\n📦 To install your package:")
    print("   pip install -e .")
    print("\n🚀 To build distribution:")
    print("   python -m build")
    print("\n📤 To upload to PyPI:")
    print("   python -m twine upload dist/*")
