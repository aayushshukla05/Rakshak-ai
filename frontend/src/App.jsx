import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link, useLocation } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import NetworkTwinPage from './pages/NetworkTwinPage';
import IncidentReports from './pages/IncidentReports';
import Vulnerabilities from './pages/Vulnerabilities';
import Playbooks from './pages/Playbooks';
import './index.css';

function NavLink({ to, children }) {
  const location = useLocation();
  const isActive = location.pathname === to;
  
  return (
    <Link 
      to={to} 
      className={`px-4 py-2 rounded-lg font-semibold transition-colors ${
        isActive 
          ? 'bg-indigo-500/20 text-indigo-400' 
          : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
      }`}
    >
      {children}
    </Link>
  );
}

function AppLayout() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-8 font-sans">
      <header className="mb-8 border-b border-slate-800 pb-4 flex flex-col md:flex-row justify-between items-start md:items-end gap-4">
        <div>
          <h1 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 via-indigo-400 to-purple-500 tracking-tight">
            Rakshak.AI
          </h1>
          <p className="text-slate-400 mt-2 text-sm uppercase tracking-widest font-semibold">
            Autonomous Cyber Resilience for CNI
          </p>
        </div>
        
        <nav className="flex flex-wrap gap-2">
          <NavLink to="/">Dashboard</NavLink>
          <NavLink to="/twin">Digital Twin</NavLink>
          <NavLink to="/reports">Incident Reports</NavLink>
          <NavLink to="/vulnerabilities">Vulnerabilities</NavLink>
          <NavLink to="/playbooks">Playbooks</NavLink>
        </nav>

        <div className="flex gap-4 items-center self-start md:self-end">
          <div className="flex items-center gap-2 bg-slate-900 px-4 py-2 rounded-lg border border-slate-800">
            <span className="relative flex h-3 w-3">
              <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
              <span className="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
            </span>
            <span className="text-xs text-slate-400 uppercase tracking-wider font-bold">SOAR Engine Online</span>
          </div>
        </div>
      </header>

      <main>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/twin" element={<NetworkTwinPage />} />
          <Route path="/reports" element={<IncidentReports />} />
          <Route path="/vulnerabilities" element={<Vulnerabilities />} />
          <Route path="/playbooks" element={<Playbooks />} />
        </Routes>
      </main>
    </div>
  );
}

function App() {
  return (
    <Router>
      <AppLayout />
    </Router>
  );
}

export default App;
