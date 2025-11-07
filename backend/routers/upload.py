from fastapi import APIRouter, File, UploadFile, HTTPException
from services.parser import parse_excel_file
from services.analyzer import analyze_data
from services.ai_service import generate_insights
import pandas as pd
import io
import traceback

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload and analyze Excel/CSV file
    Returns complete analysis with visualizations data and AI insights
    """
    try:
        # Validate file type
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        # Read file content into memory
        contents = await file.read()
        
        # Reset file pointer for pandas
        file_obj = io.BytesIO(contents)
        
        # Read file into pandas based on extension
        try:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file_obj)
            elif file.filename.endswith(('.xlsx', '.xls')):
                # Check if Excel has multiple sheets
                # Reset file pointer for ExcelFile
                file_obj.seek(0)
                excel_file = pd.ExcelFile(file_obj, engine='openpyxl')
                sheet_names = excel_file.sheet_names
                print(f"DEBUG: Excel sheets found: {sheet_names}")
                
                # Look for sheet with product data (has Product ID or Product Description)
                df = None
                for sheet_name in sheet_names:
                    file_obj.seek(0)  # Reset for each read
                    temp_df = pd.read_excel(file_obj, sheet_name=sheet_name, engine='openpyxl')
                    columns_lower = [col.lower() for col in temp_df.columns]
                    print(f"DEBUG: Sheet '{sheet_name}' columns: {list(temp_df.columns)}")
                    # Check if this sheet has product-related columns
                    has_product_id = any('product' in col and 'id' in col for col in columns_lower)
                    has_category = any('category' in col and 'transaction' not in col for col in columns_lower)
                    has_product_desc = any('product' in col and 'description' in col for col in columns_lower)
                    
                    if has_product_id or (has_category and has_product_desc):
                        df = temp_df
                        print(f"DEBUG: Using sheet '{sheet_name}' with product data")
                        break
                
                # If no product sheet found, use first sheet
                if df is None:
                    file_obj.seek(0)
                    df = pd.read_excel(file_obj, sheet_name=sheet_names[0], engine='openpyxl')
                    print(f"DEBUG: No product sheet found, using first sheet: '{sheet_names[0]}'")
                    print(f"WARNING: First sheet may not contain product data. Columns: {list(df.columns)}")
            else:
                raise HTTPException(
                    status_code=400, 
                    detail=f"Unsupported file type: {file.filename}. Supported: .csv, .xlsx, .xls"
                )
        except Exception as e:
            raise HTTPException(
                status_code=400, 
                detail=f"Error reading file: {str(e)}. Please check file format."
            )
        
        # Check if dataframe is empty
        if df.empty:
            raise HTTPException(status_code=400, detail="File is empty or contains no data")
        
        # Parse and validate data
        try:
            parsed_data = parse_excel_file(df)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=f"Data validation error: {str(e)}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error parsing data: {str(e)}")
        
        # Perform analysis
        try:
            analysis = analyze_data(parsed_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error analyzing data: {str(e)}")
        
        # Generate AI insights (this will fallback to template if API fails)
        try:
            insights = generate_insights(analysis)
        except Exception as e:
            # Use template insights if AI fails
            print(f"Warning: AI insights failed, using template: {e}")
            from services.ai_service import _generate_template_insights
            insights = _generate_template_insights(analysis)
        
        # Combine results
        result = {
            **analysis,
            "insights": insights
        }
        
        return result
        
    except HTTPException:
        # Re-raise HTTP exceptions as-is
        raise
    except Exception as e:
        # Log full error for debugging
        error_trace = traceback.format_exc()
        print(f"Unexpected error: {error_trace}")
        raise HTTPException(
            status_code=500, 
            detail=f"Error processing file: {str(e)}. Check server logs for details."
        )

