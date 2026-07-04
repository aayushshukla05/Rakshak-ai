import React from 'react';
import NetworkGraph from '../components/NetworkGraph';
import ActionCenter from '../components/ActionCenter';
import NarrativeTimeline from '../components/NarrativeTimeline';
import ThreatGlobe from '../components/ThreatGlobe';
import ShapChart from '../components/ShapChart';
import MitreHeatmap from '../components/MitreHeatmap';
import EscalationPanel from '../components/EscalationPanel';
import SonificationToggle from '../components/SonificationToggle';

function Dashboard() {
  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 xl:grid-cols-5 gap-6">
      {/* Left Column - Intelligence */}
      <aside className="lg:col-span-1 flex flex-col gap-6">
        <ThreatGlobe />
        <MitreHeatmap />
        <ShapChart />
        <SonificationToggle />
      </aside>

      {/* Center Column - Visualization & Simulation */}
      <section className="lg:col-span-2 xl:col-span-3 flex flex-col gap-6">
        <div className="flex-1 min-h-[400px]">
          <NetworkGraph />
        </div>
        <div className="grid grid-cols-1 gap-6">
          <NarrativeTimeline />
        </div>
      </section>
      
      {/* Right Column - SOAR & Actions */}
      <aside className="lg:col-span-1 flex flex-col gap-6">
        <ActionCenter />
        <EscalationPanel />
      </aside>
    </div>
  );
}

export default Dashboard;
