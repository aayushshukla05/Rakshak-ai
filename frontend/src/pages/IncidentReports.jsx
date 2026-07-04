import React from 'react';
import NarrativeTimeline from '../components/NarrativeTimeline';
import { Download, ShieldCheck, FileText } from 'lucide-react';

function IncidentReports() {
  return (
    <div className="flex flex-col gap-6">
      <div className="flex justify-between items-center bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
        <div>
          <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-red-400 to-orange-400">
            INCIDENT: INC-2026-0047
          </h2>
          <p className="text-slate-400 mt-2 flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-500" />
            Status: Contained
          </p>
        </div>
        <button className="flex items-center gap-2 bg-indigo-500/20 text-indigo-400 hover:bg-indigo-500/30 px-4 py-2 rounded-lg font-semibold transition-colors">
          <Download className="w-4 h-4" />
          Download Forensic PDF
        </button>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <NarrativeTimeline />
        </div>
        <div className="flex flex-col gap-6">
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2">
              <FileText className="w-5 h-5 text-indigo-400" />
              Compliance Status
            </h3>
            <ul className="space-y-3">
              <li className="flex items-center gap-2 text-sm text-slate-300">
                <span className="text-emerald-500 font-bold">✅</span> CERT-In notified (&lt; 6 hrs)
              </li>
              <li className="flex items-center gap-2 text-sm text-slate-300">
                <span className="text-emerald-500 font-bold">✅</span> DPDPA breach notification
              </li>
              <li className="flex items-center gap-2 text-sm text-slate-300">
                <span className="text-slate-500 font-bold">⬜</span> NCIIPC report (pending)
              </li>
              <li className="flex items-center gap-2 text-sm text-slate-300">
                <span className="text-emerald-500 font-bold">✅</span> Evidence package generated
              </li>
            </ul>
          </div>
          
          <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
            <h3 className="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2">
              <ShieldCheck className="w-5 h-5 text-red-400" />
              Blast Radius Summary
            </h3>
            <div className="space-y-4">
              <div>
                <div className="text-slate-400 text-xs uppercase tracking-wider mb-1">Impact Score</div>
                <div className="text-2xl font-mono text-red-400">34.7</div>
              </div>
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <div className="text-slate-400 text-xs uppercase tracking-wider mb-1">Services</div>
                  <div className="text-lg font-mono text-slate-200">3</div>
                </div>
                <div>
                  <div className="text-slate-400 text-xs uppercase tracking-wider mb-1">Users</div>
                  <div className="text-lg font-mono text-slate-200">2,400</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default IncidentReports;
