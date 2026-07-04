import React, { useState, useEffect } from 'react';

const NarrativeTimeline = () => {
  const [campaign, setCampaign] = useState(null);

  useEffect(() => {
    // Mocking the data that would come from /api/v1/reporting/narrative/srv-db-fin-01
    setCampaign({
      campaign_id: "campaign_srv-db-fin-01",
      target: "srv-db-fin-01",
      current_risk: "CRITICAL",
      timeline: [
        { timestamp: "2026-07-04T08:12:00Z", type: "anomaly", description: "Detected anomalous behavior: unique_hosts_accessed, total_bytes_sent." },
        { timestamp: "2026-07-04T08:12:05Z", type: "intel_match", description: "Threat Intel correlated: MITRE T1048 Exfiltration detected from internal DB." },
        { timestamp: "2026-07-04T08:12:10Z", type: "soar_action", description: "Autonomous action taken: isolate_host. Host srv-db-fin-01 has been moved to quarantine VLAN." }
      ]
    });
  }, []);

  if (!campaign) return null;

  return (
    <div className="w-full h-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4">
      <div className="p-4 pb-2 border-b border-slate-800 flex justify-between items-center">
        <h3 className="text-lg font-semibold text-purple-400">Attack Narrative Timeline</h3>
        <span className={`px-2 py-1 text-xs rounded border ${
          campaign.current_risk === 'CRITICAL' ? 'bg-red-900/30 text-red-400 border-red-800/50' : 'bg-yellow-900/30 text-yellow-400 border-yellow-800/50'
        }`}>
          Risk: {campaign.current_risk}
        </span>
      </div>
      <div className="p-4 flex-1 overflow-y-auto max-h-[300px]">
        <div className="relative border-l border-slate-700 ml-3 space-y-6">
          {campaign.timeline.map((event, idx) => (
            <div key={idx} className="relative pl-6">
              <div className={`absolute -left-[5px] top-1.5 w-2.5 h-2.5 rounded-full border border-slate-900 ${
                event.type === 'soar_action' ? 'bg-red-500' :
                event.type === 'intel_match' ? 'bg-purple-500' : 'bg-blue-500'
              }`}></div>
              <div className="flex flex-col">
                <span className="text-xs text-slate-500">{new Date(event.timestamp).toLocaleTimeString()}</span>
                <span className="text-sm text-slate-300 font-medium">{event.description}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default NarrativeTimeline;
