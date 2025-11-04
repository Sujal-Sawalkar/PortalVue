import React, { useState } from "react";
import "./App.css";
import jsPDF from 'jspdf';

export default function App() {
  const [url, setUrl] = useState("");
  const [scanning, setScanning] = useState(false);
  const [results, setResults] = useState(null);

  const handleScan = (e) => {
    e.preventDefault();
    if (!url) return;
    setScanning(true);
    setResults(null);

    // Simulate scanning
    setTimeout(() => {
      setResults({
        accessibility: 85,
        security: 72,
        performance: 81,
        codeQuality: 79,
      });
      setScanning(false);
    }, 2000);
  };
  const handleDownloadPDF = () => {
  const doc = new jsPDF();
  
  doc.setFontSize(20);
  doc.text('Government Portal Audit Report', 20, 20);
  
  doc.setFontSize(12);
  doc.text(`URL: ${url}`, 20, 35);
  doc.text(`Scan Date: ${new Date().toLocaleDateString()}`, 20, 45);
  
  doc.setFontSize(14);
  doc.text('Scores', 20, 60);
  doc.setFontSize(11);
  doc.text(`Accessibility: ${results.accessibility}/100`, 20, 70);
  doc.text(`Security: ${results.security}/100`, 20, 80);
  doc.text(`Performance: ${results.performance}/100`, 20, 90);
  doc.text(`Code Quality: ${results.codeQuality}/100`, 20, 100);
  
  doc.setFontSize(14);
  doc.text('Issues Found', 20, 120);
  doc.setFontSize(10);
  doc.text('• Missing alt text on 8 images — affects blind users.', 20, 130);
  doc.text('• No keyboard navigation support for menus.', 20, 140);
  doc.text('• Low color contrast on buttons.', 20, 150);
  
  doc.addPage();
  doc.setFontSize(14);
  doc.text('AI Recommendations', 20, 20);
  doc.setFontSize(10);
  doc.text('1. Add Alt Text to Images for accessibility.', 20, 35);
  doc.text('2. Enable Keyboard Navigation for better UX.', 20, 50);
  doc.text('3. Improve color contrast ratios for WCAG compliance.', 20, 65);
  
  doc.save('portal_audit_report.pdf');
};

  return (
    <div className="app">
      <header className="header">
        <h1>🇮🇳 CodeSamiksha</h1>
        <button className="btn">Dashboard</button>
      </header>

      <section className="hero">
        <h2>Audit India's Government Websites</h2>
        <p>
          Automatic accessibility, security, and performance audits powered by AI.  
          Making government digital services accessible to all.
        </p>

        <form onSubmit={handleScan} className="scan-form">
          <input
            type="url"
            placeholder="Enter government portal URL (e.g. https://uidai.gov.in)"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
          <button type="submit" disabled={scanning}>
            {scanning ? "⏳ Scanning..." : "🔍 Scan Now"}
          </button>
        </form>

        {results && (
          <p className="scan-result">Showing results for: {url}</p>
        )}
      </section>

      <main className="dashboard">
        {!results && !scanning && (
          <p className="placeholder">
            🔍 Enter a portal URL above and click "Scan Now" to start analysis.
          </p>
        )}

        {scanning && <p className="loading">⏳ Analyzing portal… Please wait</p>}

        {results && (
          <>
            <div className="score-grid">
              <div className="score-card blue">
                <p className="score">{results.accessibility}</p>
                <p>Accessibility</p>
              </div>
              <div className="score-card green">
                <p className="score">{results.security}</p>
                <p>Security</p>
              </div>
              <div className="score-card orange">
                <p className="score">{results.performance}</p>
                <p>Performance</p>
              </div>
              <div className="score-card pink">
                <p className="score">{results.codeQuality}</p>
                <p>Code Quality</p>
              </div>
            </div>

            <div className="issues">
              <h3>⚠️ Issues Found (3)</h3>
              <ul>
                <li>Missing alt text on 8 images — affects blind users.</li>
                <li>No keyboard navigation support for menus.</li>
                <li>Low color contrast on buttons.</li>
              </ul>
            </div>

            <div className="recommendations">
              <h3>🤖 AI Recommendations</h3>
              <ul>
                <li>Add Alt Text to Images for accessibility.</li>
                <li>Enable Keyboard Navigation for better UX.</li>
              </ul>
            </div>

            <div className="download">
  <button className="btn-green" onClick={handleDownloadPDF}>
    📥 Download Full Report (PDF)
  </button>
</div>
          </>
        )}
      </main>

      <footer className="footer">
        <p>🇮🇳 Making Government Digital Services Accessible to All Indians</p>
        <p>CodeSamiksha • Empowering Digital India</p>
      </footer>
    </div>
  );
}