import React from 'react';
import { BookOpen, GitMerge, Check, X } from 'lucide-react';

function Playbooks() {
  return (
    <div className="flex flex-col gap-6">
      <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-400 flex items-center gap-2">
        <BookOpen className="w-6 h-6 text-indigo-400" />
        Autonomous Playbooks
      </h2>
      <p className="text-slate-400 mb-4">
        Playbook version history and LLM-proposed evolutionary changes.
      </p>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg">
          <h3 className="text-lg font-bold text-slate-200 mb-4">Active Playbooks</h3>
          <ul className="space-y-3">
            <li className="p-4 bg-slate-950 rounded-lg border border-slate-700/50 flex justify-between items-center">
              <div>
                <div className="font-bold text-slate-200">Credential Theft (v3)</div>
                <div className="text-xs text-slate-400">Last updated: 2 days ago</div>
              </div>
              <span className="bg-emerald-500/20 text-emerald-400 px-3 py-1 rounded-full text-xs font-bold">Active</span>
            </li>
            <li className="p-4 bg-slate-950 rounded-lg border border-slate-700/50 flex justify-between items-center">
              <div>
                <div className="font-bold text-slate-200">Lateral Movement (v2)</div>
                <div className="text-xs text-slate-400">Last updated: 1 week ago</div>
              </div>
              <span className="bg-emerald-500/20 text-emerald-400 px-3 py-1 rounded-full text-xs font-bold">Active</span>
            </li>
            <li className="p-4 bg-slate-950 rounded-lg border border-slate-700/50 flex justify-between items-center">
              <div>
                <div className="font-bold text-slate-200">Ransomware Containment (v4)</div>
                <div className="text-xs text-slate-400">Last updated: 12 hours ago</div>
              </div>
              <span className="bg-emerald-500/20 text-emerald-400 px-3 py-1 rounded-full text-xs font-bold">Active</span>
            </li>
          </ul>
        </div>

        <div className="bg-slate-900 border border-slate-800 p-6 rounded-xl shadow-lg border-l-4 border-l-indigo-500">
          <h3 className="text-lg font-bold text-slate-200 mb-4 flex items-center gap-2">
            <GitMerge className="w-5 h-5 text-indigo-400" />
            Playbook Evolution Proposal
          </h3>
          
          <div className="mb-4">
            <div className="flex gap-2 text-sm text-slate-300 mb-2">
              <span className="text-slate-500">Target:</span> 
              <span className="font-bold">Lateral Movement</span>
            </div>
            <div className="flex gap-4 text-sm mb-4">
              <span className="bg-slate-800 px-2 py-1 rounded">Current: v2</span>
              <span className="bg-indigo-500/20 text-indigo-300 px-2 py-1 rounded">Proposed: v3</span>
            </div>
          </div>
          
          <div className="bg-slate-950 p-4 rounded-lg font-mono text-sm mb-6 border border-slate-800">
            <div className="text-emerald-400 flex gap-2">
              <span>+</span>
              <span>Add: Parallel isolation of all recent auth hosts</span>
            </div>
            <div className="text-slate-500 flex gap-2 mt-2">
              <span>#</span>
              <span>Reason: Prevents rapid spread via compromised service accounts.</span>
            </div>
            <div className="text-indigo-400 flex gap-2 mt-4 font-bold">
              <span>↳</span>
              <span>Est. improvement: 252s → 45s</span>
            </div>
          </div>
          
          <div className="flex gap-4">
            <button className="flex-1 bg-indigo-600 hover:bg-indigo-500 text-white py-2 rounded-lg font-bold flex justify-center items-center gap-2 transition-colors">
              <Check className="w-4 h-4" /> Approve & Deploy
            </button>
            <button className="flex-1 bg-slate-800 hover:bg-slate-700 text-slate-300 py-2 rounded-lg font-bold flex justify-center items-center gap-2 transition-colors">
              <X className="w-4 h-4" /> Reject
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Playbooks;
