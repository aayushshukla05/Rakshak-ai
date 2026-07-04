import React, { useState, useEffect } from 'react';

const ActionCenter = () => {
  const [history, setHistory] = useState([]);

  // Fetching history mock
  useEffect(() => {
    // In a real app this would fetch from /api/v1/soar/history
    setHistory([
      {
        report: { synthesis: "CERT-In Advisory CI-2024-001: High risk brute force on VPN", path_risk_level: "HIGH" },
        decision: { status: "success", action: "honeypot_route", target: "192.168.1.100", message: "Traffic redirected to honeypot." }
      },
      {
        report: { synthesis: "MITRE T1048 Exfiltration detected from internal DB.", path_risk_level: "CRITICAL" },
        decision: { status: "success", action: "isolate_host", target: "srv-db-fin-01", message: "Host moved to quarantine VLAN." }
      }
    ]);
  }, []);

  return (
    <div className="w-full h-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4">
      <div className="p-4 pb-2 border-b border-slate-800">
        <h3 className="text-lg font-semibold text-red-400">Autonomous SOAR Actions</h3>
      </div>
      <div className="p-4 flex-1 overflow-y-auto max-h-[300px]">
        {history.length === 0 ? (
          <p className="text-slate-500 text-sm italic">No autonomous actions taken yet.</p>
        ) : (
          <ul className="space-y-4">
            {history.map((item, idx) => (
              <li key={idx} className="bg-slate-950 p-3 rounded border border-slate-800">
                <div className="flex justify-between items-center mb-2">
                  <span className="font-mono text-xs text-blue-400">{item.decision.action.toUpperCase()}</span>
                  <span className="px-2 py-1 bg-green-900/30 text-green-400 text-xs rounded border border-green-800/50">
                    {item.decision.status}
                  </span>
                </div>
                <p className="text-sm font-medium text-slate-200 mb-1">Target: {item.decision.target}</p>
                <p className="text-xs text-slate-400 mb-2">{item.decision.message}</p>
                <div className="mt-2 pt-2 border-t border-slate-800/50">
                  <p className="text-xs text-slate-500 line-clamp-2">Reasoning: {item.report.synthesis}</p>
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
};

export default ActionCenter;
