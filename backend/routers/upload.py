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
                df = pd.read_excel(file_obj, engine='openpyxl')
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

