from fastapi import APIRouter
from pydantic import BaseModel
from services.ai_service import generate_insights

router = APIRouter()

@router.post("/insights")
async def get_insights(data: dict):
    """Generate AI insights from analysis data"""
    try:
        insights = generate_insights(data)
        return insights
    except Exception as e:
        return {"error": str(e)}

