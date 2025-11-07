# Project Structure

Complete overview of the Zero-Waste Intelligence Engine codebase.

---

## 📁 Directory Tree

```
.
│
├── 📄 README.md                    # Main project documentation
├── 📄 START_HERE.md                # Quick navigation guide
├── 📄 QUICK_START.md                # 15-minute setup guide
├── 📄 PROJECT_STRUCTURE.md          # This file
├── 📄 CHANGELOG.md                  # Project changes log
├── 📄 .gitignore                    # Git ignore rules
│
├── 📂 frontend/                    # Next.js frontend application
│   ├── 📂 app/                     # Next.js App Router
│   │   ├── globals.css            # Global styles
│   │   ├── layout.tsx             # Root layout
│   │   └── page.tsx                # Home page
│   │
│   ├── 📂 components/              # React components
│   │   ├── FileUpload.tsx         # File upload with drag-and-drop
│   │   ├── Dashboard.tsx          # Main dashboard container
│   │   ├── CategoryChart.tsx      # Category distribution chart
│   │   ├── ZeroWasteChart.tsx     # Zero-waste adoption chart
│   │   ├── RiskProducts.tsx       # High-risk products table
│   │   └── AIInsights.tsx          # AI-generated insights panel
│   │
│   ├── 📂 lib/                     # Utilities and types
│   │   ├── api.ts                 # API client functions
│   │   └── types.ts               # TypeScript type definitions
│   │
│   ├── package.json                # Node.js dependencies
│   ├── tsconfig.json               # TypeScript configuration
│   ├── next.config.js              # Next.js configuration
│   ├── tailwind.config.js         # TailwindCSS configuration
│   └── postcss.config.js          # PostCSS configuration
│
├── 📂 backend/                     # FastAPI backend application
│   ├── 📂 routers/                 # API route handlers
│   │   ├── upload.py              # File upload endpoint
│   │   ├── analysis.py            # Analysis endpoints
│   │   ├── insights.py            # AI insights endpoint
│   │   └── export.py              # PDF export endpoint
│   │
│   ├── 📂 services/                # Business logic
│   │   ├── parser.py              # Excel/CSV file parsing
│   │   ├── analyzer.py            # Data analysis and metrics
│   │   └── ai_service.py          # AI integration (Claude/OpenAI)
│   │
│   ├── main.py                     # FastAPI application entry point
│   ├── requirements.txt            # Python dependencies
│   └── .env.example                # Environment variables template
│
├── 📂 docs/                        # Project documentation
│   ├── README.md                   # Documentation index
│   ├── ARCHITECTURE.md             # Technical architecture
│   ├── ROADMAP.md                  # Implementation timeline
│   ├── ANSWERS.md                  # FAQ and answers
│   ├── SUMMARY.md                  # Project summary
│   └── challenge-statement.pdf     # Original challenge PDF
│
└── 📂 data/                        # Sample data files
    ├── README.md                   # Data format documentation
    ├── sample-data.xlsx            # Example Excel file
    ├── full-circle-foods-data.xlsx # Full dataset
    └── full-circle-foods-data.json # JSON version
```

---

## 🎯 Key Files Explained

### Frontend Files

| File | Purpose |
|------|---------|
| `app/page.tsx` | Main landing page with file upload |
| `components/FileUpload.tsx` | Drag-and-drop file upload interface |
| `components/Dashboard.tsx` | Main dashboard with all visualizations |
| `components/CategoryChart.tsx` | Pie chart showing category distribution |
| `components/ZeroWasteChart.tsx` | Bar chart showing zero-waste adoption |
| `components/RiskProducts.tsx` | Table of high-risk products |
| `components/AIInsights.tsx` | Display AI-generated insights |
| `lib/api.ts` | Functions to call backend API |
| `lib/types.ts` | TypeScript type definitions |

### Backend Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app initialization and routing |
| `routers/upload.py` | Handles file upload and processing |
| `routers/analysis.py` | Analysis-related endpoints |
| `routers/insights.py` | AI insights generation endpoint |
| `routers/export.py` | PDF report export endpoint |
| `services/parser.py` | Parses Excel/CSV files into structured data |
| `services/analyzer.py` | Calculates metrics and statistics |
| `services/ai_service.py` | Integrates with Claude/OpenAI API |

---

## 🔄 Data Flow

```
1. User uploads file
   └─> frontend/components/FileUpload.tsx
       └─> frontend/lib/api.ts
           └─> backend/routers/upload.py

2. File processing
   └─> backend/services/parser.py
       └─> backend/services/analyzer.py
           └─> backend/services/ai_service.py

3. Response to frontend
   └─> frontend/components/Dashboard.tsx
       ├─> CategoryChart.tsx
       ├─> ZeroWasteChart.tsx
       ├─> RiskProducts.tsx
       └─> AIInsights.tsx
```

---

## 🛠️ Configuration Files

### Frontend
- `package.json` - Node.js dependencies and scripts
- `tsconfig.json` - TypeScript compiler options
- `next.config.js` - Next.js framework configuration
- `tailwind.config.js` - TailwindCSS styling configuration

### Backend
- `requirements.txt` - Python package dependencies
- `.env.example` - Environment variables template
- `main.py` - FastAPI app configuration

---

## 📦 Dependencies

### Frontend
- **Next.js 14** - React framework
- **React 18** - UI library
- **TypeScript** - Type safety
- **TailwindCSS** - Styling
- **Recharts** - Data visualization
- **Axios** - HTTP client
- **react-dropzone** - File upload

### Backend
- **FastAPI** - Web framework
- **Uvicorn** - ASGI server
- **Pandas** - Data processing
- **Openpyxl** - Excel file handling
- **Anthropic** - Claude AI API
- **Reportlab** - PDF generation

---

## 🎨 Component Hierarchy

```
app/page.tsx
└── FileUpload (when no data)
    └── Dashboard (when data loaded)
        ├── CategoryChart
        ├── ZeroWasteChart
        ├── RiskProducts
        └── AIInsights
```

---

## 🔌 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/upload` | POST | Upload and analyze file |
| `/api/insights` | POST | Generate AI insights |
| `/api/export` | POST | Export PDF report |
| `/api/stats` | GET | Get statistics |
| `/health` | GET | Health check |
| `/docs` | GET | API documentation |

---

## 📝 Adding New Features

### Frontend Component
1. Create component in `frontend/components/`
2. Add to `Dashboard.tsx` if needed
3. Update types in `lib/types.ts`

### Backend Endpoint
1. Create route in `backend/routers/`
2. Add business logic in `backend/services/`
3. Register route in `backend/main.py`

### New Visualization
1. Create chart component in `frontend/components/`
2. Add data processing in `backend/services/analyzer.py`
3. Include in dashboard layout

---

## 🧪 Testing Structure

```
tests/
├── frontend/
│   └── components/
└── backend/
    ├── routers/
    └── services/
```

*(Testing structure for future implementation)*

---

## 📚 Documentation Files

All documentation is in the `docs/` directory:

- `ARCHITECTURE.md` - Technical design
- `ROADMAP.md` - Development timeline
- `ANSWERS.md` - FAQ and solutions
- `SUMMARY.md` - Project overview

---

## 🔐 Environment Variables

Create `backend/.env` from `backend/.env.example`:

```env
ANTHROPIC_API_KEY=your_key_here
```

---

## 🚀 Quick Commands

```bash
# Frontend
cd frontend && npm install && npm run dev

# Backend
cd backend && pip install -r requirements.txt && python main.py
```

---

**Need help?** Check the [README.md](../README.md) or [QUICK_START.md](../QUICK_START.md).
