'use client';

import { useState } from 'react';
import FileUpload from '@/components/FileUpload';
import Dashboard from '@/components/Dashboard';
import { AnalysisData } from '@/lib/types';

export default function Home() {
  const [analysisData, setAnalysisData] = useState<AnalysisData | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAnalysisComplete = (data: AnalysisData) => {
    setAnalysisData(data);
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-green-50 to-blue-50 p-8">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            Zero-Waste Intelligence Engine
          </h1>
          <p className="text-lg text-gray-600">
            Transform transaction data into actionable sustainability insights
          </p>
        </div>

        {!analysisData ? (
          <FileUpload
            onAnalysisComplete={handleAnalysisComplete}
            loading={loading}
            setLoading={setLoading}
          />
        ) : (
          <Dashboard data={analysisData} onReset={() => setAnalysisData(null)} />
        )}
      </div>
    </main>
  );
}

