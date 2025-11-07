# Zero-Waste Intelligence Engine

> Transform transaction data into actionable sustainability insights through interactive visualizations and AI-powered analysis.

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.9+
- **API Key** from [Anthropic](https://console.anthropic.com/) or [OpenAI](https://platform.openai.com/)

### Installation

#### 1. Backend Setup
```bash
cd backend
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API key
python main.py
```

#### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

#### 3. Access the Application
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000
- **API Documentation:** http://localhost:8000/docs

---

## Project Structure

```
.
├── frontend/                 # Next.js application
│   ├── app/                 # Next.js app router
│   ├── components/          # React components
│   └── lib/                 # Utilities and types
│
├── backend/                  # FastAPI application
│   ├── routers/             # API endpoints
│   ├── services/            # Business logic
│   └── main.py              # Application entry point
│
├── docs/                     # Documentation
│   ├── ARCHITECTURE.md      # Technical architecture
│   ├── ROADMAP.md           # Implementation timeline
│   ├── ANSWERS.md           # FAQ and answers
│   └── SUMMARY.md           # Project overview
│
├── data/                     # Sample data files
│   └── full-circle-foods-data.xlsx
│
├── README.md                 # This file
├── START_HERE.md             # Navigation guide
├── QUICK_START.md            # Setup guide
└── PROJECT_STRUCTURE.md      # Detailed structure
```

**New to the project?** Start with [START_HERE.md](START_HERE.md)

---

## 🎯 Features

- **File Upload** - Drag-and-drop Excel/CSV support
- **Data Visualization** - Interactive charts and graphs
- **Zero-Waste Analysis** - Adoption rate calculations
- **Risk Identification** - High-waste-risk products
- **AI Insights** - Claude-powered recommendations
- **Multi-Audience Reports** - Consumer, business, policy insights
- **Export** - PDF report generation

---

## 📊 Data Format

Your Excel/CSV file should contain:

| Column | Required | Variations |
|--------|----------|------------|
| Product ID |  Yes | `ProductID`, `Product ID`, `ID` |
| Category |  Yes | `Category`, `Cat`, `Product Category` |
| Description |  Optional | `Product Description`, `Description`, `Name` |
| Zero Waste |  Optional | `Zero Waste`, `ZeroWaste`, `Package Free` |
| Transaction ID |  Optional | `TransactionID`, `Transaction ID`, `Txn ID` |

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| [START_HERE.md](START_HERE.md) | Navigation guide for new users |
| [QUICK_START.md](QUICK_START.md) | 15-minute setup guide |
| [TEAM_WALKTHROUGH.md](TEAM_WALKTHROUGH.md) | Tasks for teammates to work on |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | Complete file structure overview |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Technical design and decisions |
| [docs/ROADMAP.md](docs/ROADMAP.md) | 36-hour development timeline |
| [docs/ANSWERS.md](docs/ANSWERS.md) | FAQ and common questions |
| [docs/SUMMARY.md](docs/SUMMARY.md) | Project overview and summary |

---

## 🔧 Development

### Running in Development Mode

**Backend:**
```bash
cd backend
source venv/bin/activate
python main.py
```

**Frontend:**
```bash
cd frontend
npm run dev
```

### Environment Variables

Create `backend/.env`:
```env
ANTHROPIC_API_KEY=your_api_key_here
# OR
OPENAI_API_KEY=your_api_key_here
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Module not found | Activate venv and run `pip install -r requirements.txt` |
| CORS errors | Check both servers are running on correct ports |
| API key errors | Verify `.env` file exists and key is correct |
| File upload fails | Check file format and required columns |

See [Quick Start Guide](QUICK_START.md) for detailed troubleshooting.

---

## 🎯 Hackathon Timeline

- **Hours 0-8:** Foundation (file upload → basic chart)
- **Hours 8-16:** Core analytics (full dashboard)
- **Hours 16-24:** AI integration (insights generation)
- **Hours 24-32:** Polish & export (professional finish)
- **Hours 32-36:** Presentation prep (demo ready)

See [Implementation Roadmap](docs/ROADMAP.md) for detailed breakdown.

---

## 📝 License

MIT License - Feel free to use this for your hackathon project!

---

## 🙏 Acknowledgments

Built for the **Full Circle Food Challenge** hackathon.

**Tech Stack:**
- Frontend: Next.js 14, React, TypeScript, TailwindCSS, Recharts
- Backend: Python, FastAPI, Pandas, Anthropic Claude
- Tools: VSCode, Git, npm, pip

---

**Need help?** Check the [documentation](docs/) or open an issue.
