from fastapi import APIRouter
from fastapi.responses import Response
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from io import BytesIO

router = APIRouter()

@router.post("/export")
async def export_report(data: dict):
    """Export analysis as PDF report"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    story = []
    styles = getSampleStyleSheet()
    
    # Title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#16a34a'),
        spaceAfter=30,
    )
    story.append(Paragraph("Zero-Waste Intelligence Report", title_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Summary
    story.append(Paragraph("Executive Summary", styles['Heading2']))
    summary_text = f"""
    Total Products Analyzed: {data.get('totalProducts', 0)}<br/>
    Overall Zero-Waste Adoption: {data.get('overallAdoptionRate', 0)}%<br/>
    Total Transactions: {data.get('totalTransactions', 0)}
    """
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # AI Insights
    insights = data.get('insights', {})
    story.append(Paragraph("Key Insights", styles['Heading2']))
    story.append(Paragraph(insights.get('summary', 'No insights available'), styles['Normal']))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("Recommendations", styles['Heading2']))
    story.append(Paragraph("<b>For Consumers:</b>", styles['Normal']))
    story.append(Paragraph(insights.get('consumer', ''), styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>For Businesses:</b>", styles['Normal']))
    story.append(Paragraph(insights.get('business', ''), styles['Normal']))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph("<b>For Policymakers:</b>", styles['Normal']))
    story.append(Paragraph(insights.get('policy', ''), styles['Normal']))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    
    return Response(
        content=buffer.read(),
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=zero-waste-report.pdf"}
    )

