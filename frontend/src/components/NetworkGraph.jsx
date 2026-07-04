import React, { useEffect, useRef, useState } from 'react';
import cytoscape from 'cytoscape';

const NetworkGraph = () => {
  const containerRef = useRef(null);
  const cyRef = useRef(null);
  const [nodes, setNodes] = useState([]);
  const [edges, setEdges] = useState([]);

  // Mock data for initial rendering
  useEffect(() => {
    setNodes([
      { data: { id: 'srv-dc-01', label: 'Domain Controller', type: 'server', zone: 'internal' } },
      { data: { id: 'srv-db-fin-01', label: 'Finance DB', type: 'server', zone: 'internal' } },
      { data: { id: 'srv-vpn-01', label: 'VPN Gateway', type: 'vpn_gateway', zone: 'dmz' } },
      { data: { id: 'ws-user-01', label: 'WS-Rajesh', type: 'workstation', zone: 'internal' } },
    ]);
    setEdges([
      { data: { source: 'srv-vpn-01', target: 'srv-dc-01', label: 'CONNECTS_TO' } },
      { data: { source: 'ws-user-01', target: 'srv-db-fin-01', label: 'CONNECTS_TO' } },
      { data: { source: 'ws-user-01', target: 'srv-dc-01', label: 'AUTHENTICATES_TO' } }
    ]);
  }, []);

  useEffect(() => {
    if (!containerRef.current) return;

    cyRef.current = cytoscape({
      container: containerRef.current,
      elements: { nodes, edges },
      style: [
        {
          selector: 'node',
          style: {
            'background-color': '#1f2937',
            'label': 'data(label)',
            'color': '#f9fafb',
            'text-valign': 'bottom',
            'text-margin-y': 5,
            'font-size': '12px',
            'border-width': 2,
            'border-color': '#3b82f6',
            'width': 40,
            'height': 40
          }
        },
        {
          selector: 'node[zone = "dmz"]',
          style: {
            'border-color': '#ef4444',
          }
        },
        {
          selector: 'edge',
          style: {
            'width': 2,
            'line-color': '#4b5563',
            'target-arrow-color': '#4b5563',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'label': 'data(label)',
            'font-size': '10px',
            'color': '#9ca3af',
            'text-rotation': 'autorotate',
            'text-margin-y': -10
          }
        }
      ],
      layout: {
        name: 'cose',
        padding: 50,
        nodeRepulsion: 400000,
        idealEdgeLength: 100,
      }
    });

    return () => {
      if (cyRef.current) {
        cyRef.current.destroy();
      }
    };
  }, [nodes, edges]);

  return (
    <div className="w-full h-full bg-slate-900 border border-slate-800 text-slate-100 rounded-lg shadow-lg flex flex-col">
      <div className="p-4 pb-2 border-b border-slate-800">
        <h3 className="text-lg font-semibold text-blue-400">Network Topology</h3>
      </div>
      <div className="p-4 flex-1">
        <div 
          ref={containerRef} 
          className="w-full h-[400px] bg-slate-950 rounded-md border border-slate-800"
        />
      </div>
    </div>
  );
};

export default NetworkGraph;
