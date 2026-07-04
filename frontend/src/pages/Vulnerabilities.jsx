import React from 'react';
import MitreHeatmap from '../components/MitreHeatmap';
import { AlertTriangle, ShieldAlert } from 'lucide-react';

function Vulnerabilities() {
  return (
    <div className="flex flex-col gap-6">
      <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-400">
        Vulnerabilities & Gap Analysis
      </h2>
      <p className="text-slate-400 mb-4">
        Context-scored CVE table and MITRE ATT&CK coverage gaps based on CERT-In advisories.
      </p>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="flex flex-col gap-6">
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2">
              <ShieldAlert className="w-5 h-5 text-red-400" />
              Prioritized CVEs (Context-Scored)
            </h3>
            <div className="space-y-4">
              {/* Mock CVEs */}
              <div className="p-4 bg-slate-950 rounded-lg border border-red-500/30">
                <div className="flex justify-between items-start mb-2">
                  <div className="font-mono text-red-400 font-bold">CVE-2024-3400</div>
                  <div className="bg-red-500/20 text-red-400 px-2 py-1 rounded text-xs font-bold">Context Score: 9.8</div>
                </div>
                <p className="text-sm text-slate-300">GlobalProtect OS Command Injection. Highly critical due to 3 internet-facing instances.</p>
              </div>
              <div className="p-4 bg-slate-950 rounded-lg border border-orange-500/30">
                <div className="flex justify-between items-start mb-2">
                  <div className="font-mono text-orange-400 font-bold">CVE-2023-46805</div>
                  <div className="bg-orange-500/20 text-orange-400 px-2 py-1 rounded text-xs font-bold">Context Score: 8.2</div>
                </div>
                <p className="text-sm text-slate-300">Ivanti Connect Secure Auth Bypass. Mitigation applied, pending patch window.</p>
              </div>
            </div>
          </div>
        </div>

        <div className="flex flex-col gap-6">
          <MitreHeatmap />
          
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2">
              <AlertTriangle className="w-5 h-5 text-orange-400" />
              Critical Coverage Gaps
            </h3>
            <ul className="space-y-3">
              <li className="flex items-center gap-3 text-sm text-slate-300">
                <span className="bg-red-500/20 text-red-400 px-2 py-1 rounded font-mono text-xs">T1566</span>
                Phishing: Sparse coverage for spearphishing links.
              </li>
              <li className="flex items-center gap-3 text-sm text-slate-300">
                <span className="bg-orange-500/20 text-orange-400 px-2 py-1 rounded font-mono text-xs">T1003</span>
                OS Credential Dumping: Missing telemetry on LSASS access.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Vulnerabilities;
