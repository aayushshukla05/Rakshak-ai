import React, { useState } from 'react';

const SonificationToggle = () => {
  const [soundEnabled, setSoundEnabled] = useState(false);

  return (
    <div className="w-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex items-center justify-between mt-4 p-4">
      <div>
        <h3 className="text-sm font-semibold text-blue-400">Threat Sonification</h3>
        <p className="text-xs text-slate-400 mt-0.5">Auditory cues for network anomalies</p>
      </div>
      <button 
        onClick={() => setSoundEnabled(!soundEnabled)}
        className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${
          soundEnabled ? 'bg-blue-600' : 'bg-slate-700'
        }`}
      >
        <span 
          className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
            soundEnabled ? 'translate-x-6' : 'translate-x-1'
          }`}
        />
      </button>
    </div>
  );
};

export default SonificationToggle;
