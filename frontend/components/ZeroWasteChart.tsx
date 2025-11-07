'use client';

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

interface ZeroWasteData {
  category: string;
  zeroWasteCount: number;
  totalCount: number;
  adoptionRate: number;
}

interface ZeroWasteChartProps {
  data: ZeroWasteData[];
}

export default function ZeroWasteChart({ data }: ZeroWasteChartProps) {
  const chartData = data.map((item) => ({
    category: item.category,
    'Zero-Waste': item.zeroWasteCount,
    'Non Zero-Waste': item.totalCount - item.zeroWasteCount,
    'Adoption Rate': item.adoptionRate,
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <BarChart data={chartData}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="category" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="Zero-Waste" fill="#22c55e" />
        <Bar dataKey="Non Zero-Waste" fill="#ef4444" />
      </BarChart>
    </ResponsiveContainer>
  );
}

