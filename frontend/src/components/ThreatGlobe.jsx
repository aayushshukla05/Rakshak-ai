import React from 'react';

const ThreatGlobe = () => {
  return (
    <div className="w-full h-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col mt-4">
      <div className="p-4 pb-2 border-b border-slate-800">
        <h3 className="text-lg font-semibold text-indigo-400">Global Threat Origins</h3>
      </div>
      <div className="p-4 flex-1 flex items-center justify-center relative min-h-[200px]">
        {/* CSS Abstract Globe Representation for MVP */}
        <div className="relative w-40 h-40 rounded-full border border-indigo-500/30 overflow-hidden flex items-center justify-center shadow-[0_0_30px_rgba(79,70,229,0.2)]">
          <div className="absolute w-[200%] h-[200%] bg-[linear-gradient(rgba(79,70,229,0.1)_1px,transparent_1px),linear-gradient(90deg,rgba(79,70,229,0.1)_1px,transparent_1px)] bg-[size:10px_10px] [transform:rotateX(60deg)] animate-[spin_20s_linear_infinite]" />
          
          {/* Mock Threat Origin Blips */}
          <div className="absolute w-2 h-2 bg-red-500 rounded-full top-10 left-10 shadow-[0_0_10px_rgba(239,68,68,0.8)] animate-pulse"></div>
          <div className="absolute w-1.5 h-1.5 bg-yellow-400 rounded-full top-24 left-20 shadow-[0_0_8px_rgba(250,204,21,0.8)] animate-ping"></div>
          <div className="absolute w-2 h-2 bg-red-500 rounded-full bottom-10 right-8 shadow-[0_0_10px_rgba(239,68,68,0.8)] animate-pulse"></div>
        </div>
        
        <div className="absolute bottom-4 left-4 text-xs text-slate-400">
          <p className="flex items-center gap-1"><span className="w-2 h-2 bg-red-500 rounded-full inline-block"></span> High Severity Source</p>
          <p className="flex items-center gap-1 mt-1"><span className="w-2 h-2 bg-yellow-400 rounded-full inline-block"></span> Monitoring</p>
        </div>
      </div>
    </div>
  );
};

export default ThreatGlobe;
