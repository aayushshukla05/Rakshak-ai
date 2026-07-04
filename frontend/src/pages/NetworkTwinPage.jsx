import React from 'react';
import NetworkTwin from '../components/NetworkTwin';

function NetworkTwinPage() {
  return (
    <div className="flex flex-col gap-6">
      <h2 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-indigo-400">
        Cyber Digital Twin Sandbox
      </h2>
      <p className="text-slate-400 mb-4">
        Simulate lateral movement and evaluate attack path predictions on your digital twin.
      </p>
      <NetworkTwin />
    </div>
  );
}

export default NetworkTwinPage;
