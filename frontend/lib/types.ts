export interface CategoryData {
  category: string;
  count: number;
  percentage: number;
}

export interface ZeroWasteData {
  category: string;
  zeroWasteCount: number;
  totalCount: number;
  adoptionRate: number;
}

export interface RiskProduct {
  productId: string;
  description: string;
  category: string;
  transactionCount: number;
  hasZeroWaste: boolean;
}

export interface Insights {
  summary: string;
  consumer: string;
  business: string;
  policy: string;
}

export interface AnalysisData {
  categoryBreakdown: CategoryData[];
  zeroWasteAdoption: ZeroWasteData[];
  highRiskProducts: RiskProduct[];
  insights: Insights;
  totalProducts: number;
  totalTransactions: number;
  overallAdoptionRate: number;
}

