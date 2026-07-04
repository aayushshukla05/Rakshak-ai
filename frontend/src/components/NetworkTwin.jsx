import React, { useState } from 'react';

const NetworkTwin = () => {
  const [node, setNode] = useState('ws-user-01');
  const [result, setResult] = useState(null);
  
  const handleSimulate = () => {
    // Mock simulation
    if (node === 'ws-user-01') {
      setResult({
        compromised_node: node,
        simulation_result: 'HIGH RISK',
        critical_paths_exposed: [
          { target: 'srv-db-fin-01', steps: 2, route: ['ws-user-01', 'srv-vpn-01', 'srv-db-fin-01'] },
          { target: 'srv-dc-01', steps: 1, route: ['ws-user-01', 'srv-dc-01'] }
        ]
      });
    } else {
      setResult({
        compromised_node: node,
        simulation_result: 'MODERATE RISK',
        critical_paths_exposed: []
      });
    }
  };

  return (
    <div className="w-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4">
      <div className="p-4 pb-2 border-b border-slate-800">
        <h3 className="text-lg font-semibold text-teal-400">Digital Twin Sandbox</h3>
        <p className="text-xs text-slate-400">Simulate "What-If" compromise scenarios safely.</p>
      </div>
      <div className="p-4 flex flex-col gap-4">
        <div className="flex gap-2">
          <input 
            type="text" 
            value={node} 
            onChange={(e) => setNode(e.target.value)} 
            className="flex-1 bg-slate-950 border border-slate-700 rounded px-3 py-1 text-sm focus:outline-none focus:border-teal-500"
            placeholder="Enter Node ID (e.g., ws-user-01)"
          />
          <button 
            onClick={handleSimulate}
            className="bg-teal-600 hover:bg-teal-500 text-white px-4 py-1 rounded text-sm transition-colors"
          >
            Simulate
          </button>
        </div>
        
        {result && (
          <div className="bg-slate-950 p-3 rounded border border-slate-800 text-sm">
            <div className="flex justify-between items-center mb-2">
              <span className="font-semibold text-slate-300">Result: {result.compromised_node}</span>
              <span className={`px-2 py-0.5 rounded text-xs font-bold ${result.simulation_result === 'HIGH RISK' ? 'bg-red-900/50 text-red-400' : 'bg-yellow-900/50 text-yellow-400'}`}>
                {result.simulation_result}
              </span>
            </div>
            {result.critical_paths_exposed.length > 0 ? (
              <ul className="space-y-2 mt-2">
                {result.critical_paths_exposed.map((path, idx) => (
                  <li key={idx} className="border-l-2 border-slate-700 pl-2">
                    <span className="text-slate-400 text-xs">Exposes: <strong className="text-slate-200">{path.target}</strong> in {path.steps} steps</span>
                    <p className="font-mono text-xs text-teal-300 mt-1">{path.route.join(' → ')}</p>
                  </li>
                ))}
              </ul>
            ) : (
              <p className="text-slate-400 text-xs mt-2">No critical paths exposed directly.</p>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

export default NetworkTwin;
