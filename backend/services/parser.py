import pandas as pd
from typing import Dict, List, Any

def parse_excel_file(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Parse Excel/CSV data into structured format
    Handles various column name variations
    """
    # Keep original column names - we'll match using normalized versions
    original_columns = list(df.columns)
    
    # Create normalized mapping: normalized_name -> original_name
    normalized_columns = {}
    for col in original_columns:
        # Normalize: lowercase, strip, replace spaces/hyphens with underscores, remove special chars
        normalized = col.strip().lower().replace(' ', '_').replace('-', '_').replace('?', '').replace('!', '').replace('.', '')
        normalized_columns[normalized] = col
    
    # Map common column name variations (using normalized names)
    column_mapping = {
        'productid': ['product_id', 'productid', 'id', 'product'],
        'product_description': ['product_description', 'description', 'product_desc', 'name'],
        'category': ['category', 'cat', 'product_category'],
        'subcategory': ['subcategory', 'sub_category', 'sub_cat'],
        'zero_waste': ['zero_waste', 'zerowaste', 'zero_waste_flag', 'package_free', 'waste_free'],
        'transaction_id': ['transaction_id', 'transactionid', 'transaction', 'txn_id', 'txn'],
    }
    
    # Find actual column names by matching normalized names
    actual_columns = {}
    for standard_name, variations in column_mapping.items():
        for norm_col, orig_col in normalized_columns.items():
            # Check if normalized column matches any variation
            if norm_col in variations or any(var in norm_col for var in variations) or standard_name in norm_col:
                actual_columns[standard_name] = orig_col
                break
    
    # Validate required columns
    required = ['productid', 'category']
    missing = [r for r in required if r not in actual_columns]
    if missing:
        # Show what columns were found and what's missing
        found_columns = list(df.columns)
        raise ValueError(
            f"Missing required columns: {missing}. "
            f"Found columns: {found_columns}. "
            f"Looking for: ProductID (or Product ID, ID) and Category (or Cat)"
        )
    
    # Extract data
    parsed = {
        'products': [],
        'transactions': []
    }
    
    for _, row in df.iterrows():
        try:
            # Get product ID (required)
            product_id = row[actual_columns['productid']]
            if pd.isna(product_id):
                continue  # Skip rows with missing product ID
            
            # Get category (required)
            category = row[actual_columns['category']]
            if pd.isna(category):
                continue  # Skip rows with missing category
            
            product = {
                'productId': str(product_id),
                'description': str(row.get(actual_columns.get('product_description', ''), 'N/A')) if actual_columns.get('product_description') else 'N/A',
                'category': str(category),
                'subcategory': str(row.get(actual_columns.get('subcategory', ''), 'N/A')) if actual_columns.get('subcategory') else 'N/A',
                'hasZeroWaste': _parse_zero_waste_flag(
                    row.get(actual_columns.get('zero_waste', ''), False) if actual_columns.get('zero_waste') else False
                ),
            }
            parsed['products'].append(product)
        except Exception as e:
            # Skip problematic rows and continue
            print(f"Warning: Skipping row due to error: {e}")
            continue
        
        # Handle transactions if available
        if 'transaction_id' in actual_columns:
            txn_id = row[actual_columns['transaction_id']]
            if pd.notna(txn_id):
                parsed['transactions'].append({
                    'transactionId': str(txn_id),
                    'productId': product['productId']
                })
    
    return parsed

def _parse_zero_waste_flag(value: Any) -> bool:
    """Parse zero-waste flag from various formats"""
    if pd.isna(value):
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        # Handle various text formats
        value_lower = value.lower().strip()
        return value_lower in [
            'true', 'yes', '1', 'y', 
            'package-free', 'package free',
            'zero-waste', 'zero waste', 'zerowaste',
            'waste-free', 'waste free'
        ] or 'zero' in value_lower or 'waste' in value_lower
    return False

