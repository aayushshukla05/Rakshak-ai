import React from 'react';

const MitreHeatmap = () => {
  // 3x3 Mock of MITRE ATT&CK Matrix Categories
  const categories = [
    { name: 'Initial Access', active: false },
    { name: 'Execution', active: true },
    { name: 'Persistence', active: false },
    { name: 'Privilege Esc', active: false },
    { name: 'Defense Evasion', active: true },
    { name: 'Credential Access', active: false },
    { name: 'Discovery', active: true },
    { name: 'Lateral Movement', active: true },
    { name: 'Exfiltration', active: false }
  ];

  return (
    <div className="w-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4 p-4">
      <div className="pb-2 border-b border-slate-800 mb-4">
        <h3 className="text-lg font-semibold text-emerald-400">MITRE ATT&CK Mapping</h3>
      </div>
      <div className="grid grid-cols-3 gap-2">
        {categories.map((cat, idx) => (
          <div 
            key={idx} 
            className={`flex items-center justify-center text-center text-xs p-2 rounded border ${
              cat.active 
                ? 'bg-emerald-900/40 border-emerald-600/50 text-emerald-300' 
                : 'bg-slate-950 border-slate-800 text-slate-600'
            }`}
          >
            {cat.name}
          </div>
        ))}
      </div>
    </div>
  );
};

export default MitreHeatmap;
