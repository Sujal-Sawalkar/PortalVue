# PortalVue - Government Portal Quality Auditor

AI-powered accessibility, security, and performance audits for Indian government websites with actionable AI-generated recommendations.

## Problem Statement

India has 500+ government portals serving 130 crore citizens. Yet:
- **1.5 crore disabled Indians cannot access government services** due to accessibility failures
- **Security vulnerabilities** put citizen data at risk
- **Poor performance** locks out rural users with slow internet
- **No systematic auditing** means issues persist unfixed

**This is a civil rights issue.**

## Our Solution

PortalVue is an intelligent auditing platform that scans government websites on 4 critical dimensions:

- **♿ Accessibility** - WCAG 2.1 compliance, alt text, keyboard navigation, semantic HTML
- **🔐 Security** - HTTPS verification, security headers, vulnerability detection
- **⚡ Performance** - Load time analysis, Google PageSpeed integration, Core Web Vitals
- **🧹 Code Quality** - Deprecated patterns, best practices, maintainability

**The differentiator:** Our AI doesn't just find problems. It generates specific, actionable fixes with code snippets, explanations, and citizen impact metrics.

## Why PortalVue?

Unlike generic code analysis tools:
- **Government-Focused** - Pre-loaded with 500+ Indian government portals
- **4-in-1 Dashboard** - All metrics integrated in one place
- **AI Recommendations** - Ready-to-implement solutions with code
- **Public Accountability** - Transparent portal rankings create pressure for improvement
- **Automated at Scale** - Scan all portals systematically

## Key Features

✅ **Integrated 4-in-1 Analysis** - Accessibility + Security + Performance + Code Quality
✅ **AI-Powered Fixes** - Ready-to-copy code solutions with explanations
✅ **Government Portal Database** - 500+ Indian government websites pre-loaded
✅ **Async Scanning** - Background processing, non-blocking user experience
✅ **PDF Reports** - Professional reports for government submission
✅ **Public Dashboard** - Transparent rankings driving accountability
✅ **Progress Tracking** - Monitor improvements over time
✅ **Impact Metrics** - Show how fixes help millions of citizens

## Tech Stack

**Frontend:**
- React.js with Vite
- Axios for API integration
- jsPDF for report generation
- Responsive CSS styling

**Backend:**
- Django 4.2 REST Framework
- Python 3.13
- PostgreSQL database
- Beautiful Soup 4 for HTML parsing
- Threading for async operations

**AI & Analytics:**
- Deepseek API for intelligent recommendations
- Google PageSpeed Insights API for performance metrics
- WCAG 2.1 standards for accessibility
- OWASP principles for security analysis

**Infrastructure:**
- Docker containerization ready
- GitHub version control
- Cloud deployment compatible (Render, Railway)

## Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 16+
- PostgreSQL
- Git

### Backend Setup
```bash
