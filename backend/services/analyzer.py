from typing import Dict, List, Any
from collections import Counter, defaultdict

def analyze_data(parsed_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Analyze parsed data and generate metrics for visualization
    """
    products = parsed_data['products']
    transactions = parsed_data['transactions']
    
    # Category breakdown
    category_counts = Counter(p['category'] for p in products)
    total_products = len(products)
    category_breakdown = [
        {
            'category': cat,
            'count': count,
            'percentage': round((count / total_products) * 100, 2)
        }
        for cat, count in category_counts.items()
    ]
    
    # Zero-waste adoption by category
    category_zero_waste = defaultdict(lambda: {'zero_waste': 0, 'total': 0})
    for product in products:
        cat = product['category']
        category_zero_waste[cat]['total'] += 1
        if product['hasZeroWaste']:
            category_zero_waste[cat]['zero_waste'] += 1
    
    zero_waste_adoption = [
        {
            'category': cat,
            'zeroWasteCount': data['zero_waste'],
            'totalCount': data['total'],
            'adoptionRate': round((data['zero_waste'] / data['total']) * 100, 2) if data['total'] > 0 else 0
        }
        for cat, data in category_zero_waste.items()
    ]
    
    # Transaction counts per product
    transaction_counts = Counter(t['productId'] for t in transactions)
    
    # High-risk products (popular but no zero-waste option)
    product_map = {p['productId']: p for p in products}
    high_risk_products = []
    
    for product_id, tx_count in transaction_counts.items():
        if product_id in product_map:
            product = product_map[product_id]
            if not product['hasZeroWaste']:
                high_risk_products.append({
                    'productId': product_id,
                    'description': product['description'],
                    'category': product['category'],
                    'transactionCount': tx_count,
                    'hasZeroWaste': False
                })
    
    # Sort by transaction count (descending)
    high_risk_products.sort(key=lambda x: x['transactionCount'], reverse=True)
    
    # Overall adoption rate
    total_zero_waste = sum(1 for p in products if p['hasZeroWaste'])
    overall_adoption_rate = round((total_zero_waste / total_products) * 100, 2) if total_products > 0 else 0
    
    return {
        'categoryBreakdown': category_breakdown,
        'zeroWasteAdoption': zero_waste_adoption,
        'highRiskProducts': high_risk_products[:20],  # Top 20
        'totalProducts': total_products,
        'totalTransactions': len(transactions),
        'overallAdoptionRate': overall_adoption_rate
    }

