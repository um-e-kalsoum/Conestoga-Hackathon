# 🚀 Quick Start Guide

Get your Zero-Waste Intelligence Engine running in **15 minutes**.

---

## Step 1: Backend Setup (5 minutes)

### Create Virtual Environment
```bash
cd backend
python -m venv venv
```

### Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment
```bash
# Copy example file
cp .env.example .env

# Edit .env and add your API key
# ANTHROPIC_API_KEY=sk-ant-...
```

**Get API Key:**
- [Anthropic Claude](https://console.anthropic.com/) (Recommended)
- [OpenAI](https://platform.openai.com/) (Alternative)

---

## Step 2: Start Backend (1 minute)

```bash
# Make sure venv is activated
python main.py
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

✅ Backend is running! Keep this terminal open.

---

## Step 3: Frontend Setup (5 minutes)

**Open a NEW terminal window/tab**

```bash
cd frontend
npm install
npm run dev
```

**Expected Output:**
```
  ▲ Next.js 14.0.4
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

✅ Frontend is running!

---

## Step 4: Test It! (2 minutes)

1. **Open Browser:** http://localhost:3000
2. **Upload File:** Drag and drop your Excel file
3. **View Results:** See charts and insights appear!

---

## ✅ Verification Checklist

- [ ] Backend terminal shows "Uvicorn running"
- [ ] Frontend terminal shows "Ready"
- [ ] Browser opens http://localhost:3000
- [ ] File upload interface appears
- [ ] Can upload Excel/CSV file
- [ ] Charts render after upload

---

## 🐛 Common Issues

### "Module not found" Error
```bash
# Solution: Make sure venv is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### CORS Errors
- ✅ Check backend is running on port **8000**
- ✅ Check frontend is running on port **3000**
- ✅ Verify CORS settings in `backend/main.py`

### API Key Errors
- ✅ Check `.env` file exists in `backend/` directory
- ✅ Verify API key format (no extra spaces)
- ✅ Make sure you have API credits

### File Upload Fails
- ✅ Check file format (`.xlsx`, `.xls`, or `.csv`)
- ✅ Verify required columns exist (ProductID, Category)
- ✅ Check backend terminal for error messages

---

## 📊 Expected Data Format

Your Excel file should have columns like:

| Column Name | Example Values |
|-------------|----------------|
| `ProductID` | `P001`, `12345` |
| `Category` | `Produce`, `Dairy`, `Grocery` |
| `Product Description` | `Organic Apples`, `Milk 2L` |
| `Zero Waste` | `True`, `False`, `Yes`, `No`, `1`, `0` |
| `TransactionID` | `TXN001`, `123` (optional) |

**Note:** The parser is flexible and handles variations in column names!

---

## 🎯 Next Steps

1. ✅ **Test with your actual data file**
2. ✅ **Customize charts** in `frontend/components/`
3. ✅ **Adjust AI prompts** in `backend/services/ai_service.py`
4. ✅ **Add more visualizations** as needed

---

## 💡 Pro Tips

- **Keep both terminals open** - Backend and frontend need to run simultaneously
- **Use browser DevTools** (F12) - See API requests and debug frontend
- **Check API docs** - http://localhost:8000/docs for backend documentation
- **AI fallback works** - If API fails, template insights are used automatically
- **Test early** - Upload your actual Excel file in the first hour

---

## 📚 Need More Help?

- **Architecture Details:** See `docs/ARCHITECTURE.md`
- **Implementation Timeline:** See `docs/ROADMAP.md`
- **FAQ & Answers:** See `docs/ANSWERS.md`

---

**You're all set! Happy coding! 🎉**
