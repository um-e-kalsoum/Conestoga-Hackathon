'use client';

import { useState } from 'react';
import { RefreshCw, Download } from 'lucide-react';
import CategoryChart from './CategoryChart';
import ZeroWasteChart from './ZeroWasteChart';
import RiskProducts from './RiskProducts';
import AIInsights from './AIInsights';
import { AnalysisData } from '@/lib/types';
import { exportReport } from '@/lib/api';

interface DashboardProps {
  data: AnalysisData;
  onReset: () => void;
}

export default function Dashboard({ data, onReset }: DashboardProps) {
  const [exporting, setExporting] = useState(false);

  const handleExport = async () => {
    setExporting(true);
    try {
      await exportReport(data);
    } catch (error) {
      console.error('Export failed:', error);
    } finally {
      setExporting(false);
    }
  };

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold text-gray-900">Analysis Dashboard</h2>
        <div className="flex gap-3">
          <button
            onClick={handleExport}
            disabled={exporting}
            className="flex items-center gap-2 px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50"
          >
            <Download className="w-4 h-4" />
            {exporting ? 'Exporting...' : 'Export Report'}
          </button>
          <button
            onClick={onReset}
            className="flex items-center gap-2 px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300"
          >
            <RefreshCw className="w-4 h-4" />
            New Analysis
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-lg font-semibold mb-4">Category Distribution</h3>
          <CategoryChart data={data.categoryBreakdown} />
        </div>

        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-lg font-semibold mb-4">Zero-Waste Adoption</h3>
          <ZeroWasteChart data={data.zeroWasteAdoption} />
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-lg font-semibold mb-4">High-Risk Products</h3>
          <RiskProducts products={data.highRiskProducts} />
        </div>

        <div className="bg-white rounded-lg shadow-md p-6">
          <h3 className="text-lg font-semibold mb-4">AI-Generated Insights</h3>
          <AIInsights insights={data.insights} />
        </div>
      </div>
    </div>
  );
}

