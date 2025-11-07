'use client';

interface Insights {
  summary: string;
  consumer: string;
  business: string;
  policy: string;
}

interface AIInsightsProps {
  insights: Insights;
}

export default function AIInsights({ insights }: AIInsightsProps) {
  return (
    <div className="space-y-4">
      <div className="bg-green-50 border-l-4 border-green-500 p-4 rounded">
        <h4 className="font-semibold text-green-900 mb-2">Key Insight</h4>
        <p className="text-green-800">{insights.summary}</p>
      </div>

      <div className="space-y-3">
        <div className="bg-blue-50 p-4 rounded">
          <h4 className="font-semibold text-blue-900 mb-2">For Consumers</h4>
          <p className="text-blue-800 text-sm">{insights.consumer}</p>
        </div>

        <div className="bg-purple-50 p-4 rounded">
          <h4 className="font-semibold text-purple-900 mb-2">For Businesses</h4>
          <p className="text-purple-800 text-sm">{insights.business}</p>
        </div>

        <div className="bg-orange-50 p-4 rounded">
          <h4 className="font-semibold text-orange-900 mb-2">For Policymakers</h4>
          <p className="text-orange-800 text-sm">{insights.policy}</p>
        </div>
      </div>
    </div>
  );
}

