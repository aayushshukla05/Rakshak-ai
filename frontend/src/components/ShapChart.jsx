import React from 'react';

const ShapChart = () => {
  const shapData = [
    { feature: 'unique_hosts_accessed', value: 0.45 },
    { feature: 'total_bytes_sent', value: 0.32 },
    { feature: 'auth_failures', value: 0.15 },
    { feature: 'process_hollowing', value: 0.08 }
  ];

  return (
    <div className="w-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4 p-4">
      <div className="pb-2 border-b border-slate-800 mb-4">
        <h3 className="text-lg font-semibold text-pink-400">SHAP Explainability</h3>
        <p className="text-xs text-slate-400">AI feature importance for current anomaly</p>
      </div>
      <div className="flex flex-col gap-3">
        {shapData.map((item, idx) => (
          <div key={idx} className="flex flex-col">
            <div className="flex justify-between text-xs mb-1">
              <span className="font-mono text-slate-300">{item.feature}</span>
              <span className="text-slate-400">+{item.value.toFixed(2)}</span>
            </div>
            <div className="w-full bg-slate-800 rounded-full h-1.5">
              <div 
                className="bg-pink-500 h-1.5 rounded-full" 
                style={{ width: `${item.value * 200}%` /* Scaled for visual effect */ }}
              ></div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ShapChart;
