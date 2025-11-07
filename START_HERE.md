# 🚀 Start Here

Welcome to the **Zero-Waste Intelligence Engine** project!

This guide will help you navigate the codebase and get started quickly.

---

## 📋 Quick Navigation

### 🎯 I want to...

| Goal | Go To |
|------|-------|
| **Get started immediately** | [QUICK_START.md](QUICK_START.md) |
| **Understand the project** | [README.md](README.md) |
| **See project structure** | [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) |
| **Learn architecture** | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) |
| **Plan development** | [docs/ROADMAP.md](docs/ROADMAP.md) |
| **Find answers** | [docs/ANSWERS.md](docs/ANSWERS.md) |

---

## 🏃 Quick Start (5 minutes)

### 1. Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env
python main.py
```

### 2. Frontend (New Terminal)
```bash
cd frontend
npm install
npm run dev
```

### 3. Open Browser
- Go to: http://localhost:3000
- Upload your Excel file
- See the magic! ✨

**Full instructions:** [QUICK_START.md](QUICK_START.md)

---

## 📁 Project Structure

```
.
├── frontend/          # Next.js application
├── backend/           # FastAPI application
├── docs/              # Documentation
├── data/              # Sample data
└── README.md          # Main documentation
```

**Detailed structure:** [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

---

## 📚 Documentation

All documentation is organized in the `docs/` folder:

- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - Technical design and decisions
- **[ROADMAP.md](docs/ROADMAP.md)** - 36-hour implementation timeline
- **[ANSWERS.md](docs/ANSWERS.md)** - FAQ and common questions
- **[SUMMARY.md](docs/SUMMARY.md)** - Project overview

---

## 🎯 Key Features

- ✅ **File Upload** - Drag-and-drop Excel/CSV
- ✅ **Data Visualization** - Interactive charts
- ✅ **AI Insights** - Claude-powered analysis
- ✅ **Export Reports** - PDF generation
- ✅ **Multi-Audience** - Consumer, business, policy views

---

## 🛠️ Tech Stack

- **Frontend:** Next.js 14, React, TypeScript, TailwindCSS
- **Backend:** Python, FastAPI, Pandas
- **AI:** Anthropic Claude (with OpenAI fallback)
- **Charts:** Recharts

---

## 🆘 Need Help?

1. **Setup issues?** → [QUICK_START.md](QUICK_START.md)
2. **Architecture questions?** → [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
3. **Implementation questions?** → [docs/ANSWERS.md](docs/ANSWERS.md)
4. **Timeline questions?** → [docs/ROADMAP.md](docs/ROADMAP.md)

---

## ✅ Next Steps

1. ✅ Read [QUICK_START.md](QUICK_START.md)
2. ✅ Set up backend and frontend
3. ✅ Test with sample data in `data/` folder
4. ✅ Review [docs/ROADMAP.md](docs/ROADMAP.md) for development plan
5. ✅ Start building! 🚀

---

## 📊 Sample Data

Test files are available in the `data/` directory:
- `full-circle-foods-data.xlsx` - Full dataset
- `sample-data.xlsx` - Example file

---

**Ready to go?** Start with [QUICK_START.md](QUICK_START.md)!
