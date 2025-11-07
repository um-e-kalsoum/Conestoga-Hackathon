# Troubleshooting Guide

## Common Errors and Solutions

### 500 Internal Server Error

**What it means:** The backend encountered an error processing your file.

**How to debug:**
1. Check the backend terminal - it should show the actual error
2. Look for error messages in the console output
3. Common causes:
   - File format issues
   - Missing required columns
   - API key issues (for AI insights)

**What I fixed:**
- ✅ Better file handling (reads file properly)
- ✅ Better error messages (shows what went wrong)
- ✅ Handles missing API key gracefully
- ✅ Better data validation

**Try again:**
1. Restart the backend server
2. Try uploading your file again
3. Check the backend terminal for specific error messages

---

### "Missing required columns" Error

**What it means:** Your Excel file doesn't have the required columns.

**Required columns:**
- `ProductID` or `Product ID` or `ID`
- `Category` or `Cat`

**Solution:**
- Check your Excel file has these columns
- Column names are case-insensitive
- Spaces are handled automatically

---

### "Error reading file" Error

**What it means:** The file format is incorrect or corrupted.

**Solution:**
- Make sure file is `.xlsx`, `.xls`, or `.csv`
- Try opening the file in Excel to verify it's valid
- Try exporting as a new `.xlsx` file

---

### AI Insights Not Working

**What it means:** The AI API call failed (or no API key).

**Solution:**
- The app will automatically use template insights if AI fails
- To use real AI: Add your API key to `backend/.env`
- Check `backend/.env.example` for format

---

### CORS Errors

**What it means:** Frontend can't connect to backend.

**Solution:**
- Make sure backend is running on port 8000
- Make sure frontend is running on port 3000
- Check `backend/main.py` CORS settings

---

## Debugging Steps

### 1. Check Backend Logs
Look at the terminal where you ran `python main.py`. It will show:
- Error messages
- Stack traces
- What went wrong

### 2. Check File Format
- Open your Excel file
- Verify it has data
- Check column names match expected format

### 3. Test with Sample Data
- Try uploading `data/sample-data.xlsx` first
- If that works, your file might have format issues

### 4. Check Browser Console
- Press F12 in browser
- Go to Console tab
- Look for error messages

---

## Getting Help

If you're still stuck:
1. Check the backend terminal for error messages
2. Copy the full error message
3. Check what step failed (upload, parse, analyze, AI)
4. Look at the specific error detail

---

## Recent Fixes

**Fixed in latest update:**
- ✅ File reading issue (now uses BytesIO properly)
- ✅ Better error messages (shows what went wrong)
- ✅ Missing API key handling (uses template insights)
- ✅ Data validation (handles missing data better)
- ✅ Error logging (shows full error in terminal)

**Try restarting the backend and uploading again!**

