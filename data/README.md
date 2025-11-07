# Data Directory

This directory contains sample data files for testing and development.

## Files

- `full-circle-foods-data.xlsx` - Full dataset from the challenge
- `full-circle-foods-data.json` - JSON version of the dataset
- `sample-data.xlsx` - Example Excel file for testing

## Data Format

Your Excel/CSV files should contain:

| Column | Required | Example |
|--------|----------|---------|
| ProductID | ✅ Yes | `P001`, `12345` |
| Category | ✅ Yes | `Produce`, `Dairy`, `Grocery` |
| Product Description | ⚠️ Optional | `Organic Apples`, `Milk 2L` |
| Zero Waste | ⚠️ Optional | `True`, `False`, `Yes`, `No`, `1`, `0` |
| TransactionID | ⚠️ Optional | `TXN001`, `123` |

## Column Name Variations

The parser is flexible and handles these variations:

- **ProductID:** `ProductID`, `Product ID`, `ID`, `product_id`
- **Category:** `Category`, `Cat`, `Product Category`, `category`
- **Description:** `Product Description`, `Description`, `Name`, `Product`
- **Zero Waste:** `Zero Waste`, `ZeroWaste`, `Package Free`, `zero_waste`
- **TransactionID:** `TransactionID`, `Transaction ID`, `Txn ID`, `transaction_id`

## Usage

1. **Testing:** Use `sample-data.xlsx` for quick testing
2. **Development:** Use `full-circle-foods-data.xlsx` for full dataset
3. **Upload:** Place your own files here or upload through the web interface

## Notes

- Files are case-insensitive
- Spaces and underscores are handled automatically
- Missing optional columns are handled gracefully
- The parser validates required columns before processing

---

**Need help?** Check the main [README.md](../README.md) or [QUICK_START.md](../QUICK_START.md).
