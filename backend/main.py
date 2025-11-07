"""
Zero-Waste Intelligence Engine - Backend API

FastAPI application for processing sustainability data,
generating insights, and exporting reports.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Import routers
from routers import upload, analysis, insights, export

# Initialize FastAPI application
app = FastAPI(
    title="Zero-Waste Intelligence Engine API",
    description="Backend API for sustainability data analysis",
    version="1.0.0"
)

# Configure CORS middleware
# Allows frontend (Next.js) to make requests to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(upload.router, prefix="/api", tags=["upload"])
app.include_router(analysis.router, prefix="/api", tags=["analysis"])
app.include_router(insights.router, prefix="/api", tags=["insights"])
app.include_router(export.router, prefix="/api", tags=["export"])


# Root endpoint
@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Zero-Waste Intelligence Engine API",
        "status": "running",
        "docs": "/docs"
    }


# Health check endpoint
@app.get("/health")
async def health():
    """Health check endpoint for monitoring"""
    return {"status": "healthy"}


# Run the application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True  # Auto-reload on code changes
    )

