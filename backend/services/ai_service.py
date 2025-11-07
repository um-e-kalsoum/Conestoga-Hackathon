import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

# Initialize Claude client (only if API key exists)
api_key = os.getenv("ANTHROPIC_API_KEY")
client = None
if api_key:
    try:
        client = Anthropic(api_key=api_key)
    except Exception as e:
        print(f"Warning: Could not initialize Claude client: {e}")

def generate_insights(analysis_data: dict) -> dict:
    """
    Generate AI-powered insights using Claude
    Falls back to template if API fails
    """
    # If no API key or client not initialized, use template
    if not client:
        print("No API key found, using template insights")
        return _generate_template_insights(analysis_data)
    
    try:
        # Extract key metrics
        total_products = analysis_data.get('totalProducts', 0)
        adoption_rate = analysis_data.get('overallAdoptionRate', 0)
        category_breakdown = analysis_data.get('categoryBreakdown', [])
        high_risk_count = len(analysis_data.get('highRiskProducts', []))
        
        # Find top category
        top_category = max(category_breakdown, key=lambda x: x['count']) if category_breakdown else None
        
        # Build prompt
        prompt = f"""Analyze this zero-waste sustainability data and provide actionable insights:

Key Metrics:
- Total Products: {total_products}
- Overall Zero-Waste Adoption Rate: {adoption_rate}%
- Top Category: {top_category['category'] if top_category else 'N/A'} ({top_category['count'] if top_category else 0} products)
- High-Risk Products (popular but no zero-waste option): {high_risk_count}

Provide insights in the following format:
1. A brief summary (2-3 sentences)
2. Consumer-focused recommendation (what consumers can do)
3. Business-focused recommendation (what businesses should consider)
4. Policy-focused recommendation (what policymakers could implement)

Be specific, actionable, and sustainability-focused."""

        # Call Claude API
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )
        
        # Parse response
        response_text = message.content[0].text
        
        # Simple parsing (you can improve this)
        sections = response_text.split('\n\n')
        summary = sections[0] if sections else "Analysis complete."
        consumer = sections[1] if len(sections) > 1 else "Consider choosing zero-waste options when available."
        business = sections[2] if len(sections) > 2 else "Explore expanding zero-waste product offerings."
        policy = sections[3] if len(sections) > 3 else "Consider incentives for zero-waste product adoption."
        
        return {
            'summary': summary,
            'consumer': consumer,
            'business': business,
            'policy': policy
        }
        
    except Exception as e:
        # Fallback to template-based insights
        print(f"AI API error: {e}")
        return _generate_template_insights(analysis_data)

def _generate_template_insights(analysis_data: dict) -> dict:
    """Fallback template-based insights"""
    adoption_rate = analysis_data.get('overallAdoptionRate', 0)
    
    if adoption_rate < 20:
        status = "low"
        recommendation = "significant opportunity for improvement"
    elif adoption_rate < 50:
        status = "moderate"
        recommendation = "good progress with room for growth"
    else:
        status = "strong"
        recommendation = "excellent adoption rate"
    
    return {
        'summary': f"Zero-waste adoption is currently at {adoption_rate}%, indicating {recommendation}.",
        'consumer': f"Look for zero-waste options in your shopping. Currently, {adoption_rate}% of products offer package-free alternatives.",
        'business': f"Consider expanding zero-waste product lines. With {adoption_rate}% adoption, there's opportunity to meet growing consumer demand.",
        'policy': f"Policymakers could incentivize zero-waste adoption through tax benefits or regulations. Current adoption rate: {adoption_rate}%."
    }

