'use client';

interface RiskProduct {
  productId: string;
  description: string;
  category: string;
  transactionCount: number;
  hasZeroWaste: boolean;
}

interface RiskProductsProps {
  products: RiskProduct[];
}

export default function RiskProducts({ products }: RiskProductsProps) {
  const highRisk = products
    .filter((p) => !p.hasZeroWaste)
    .sort((a, b) => b.transactionCount - a.transactionCount)
    .slice(0, 10);

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
              Product
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
              Category
            </th>
            <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase">
              Transactions
            </th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {highRisk.map((product) => (
            <tr key={product.productId} className="hover:bg-gray-50">
              <td className="px-4 py-3 text-sm text-gray-900">
                {product.description}
              </td>
              <td className="px-4 py-3 text-sm text-gray-500">
                {product.category}
              </td>
              <td className="px-4 py-3 text-sm text-gray-900">
                {product.transactionCount}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {highRisk.length === 0 && (
        <p className="text-center text-gray-500 py-8">No high-risk products found</p>
      )}
    </div>
  );
}

