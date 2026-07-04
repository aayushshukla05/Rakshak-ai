import React, { useState } from 'react';

const EscalationPanel = () => {
  const [escalated, setEscalated] = useState(false);

  return (
    <div className="w-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4 p-4">
      <div className="pb-2 border-b border-slate-800 mb-4 flex justify-between items-center">
        <h3 className="text-lg font-semibold text-orange-400">Manual Escalation</h3>
        {escalated && <span className="px-2 py-0.5 bg-orange-900/50 text-orange-400 text-xs rounded font-bold border border-orange-700/50">ESCALATED</span>}
      </div>
      <p className="text-xs text-slate-400 mb-4">
        Override autonomous actions and escalate directly to Tier-3 IR team.
      </p>
      <button 
        onClick={() => setEscalated(true)}
        disabled={escalated}
        className={`w-full py-2 rounded font-semibold transition-colors ${
          escalated 
            ? 'bg-slate-800 text-slate-500 cursor-not-allowed' 
            : 'bg-orange-600 hover:bg-orange-500 text-white'
        }`}
      >
        {escalated ? 'Escalation Sent' : 'Escalate to Tier 3'}
      </button>
    </div>
  );
};

export default EscalationPanel;
