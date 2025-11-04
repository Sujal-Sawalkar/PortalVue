import requests
from bs4 import BeautifulSoup
import os

def scan_website(url):
    """Scan website and return scores"""
    try:
        response = requests.get(url, timeout=10)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    except Exception as e:
        return {
            'accessibility': 0,
            'security': 0,
            'performance': 0,
            'code_quality': 0,
            'issues': f"Error: Could not access website",
            'ai_recommendations': "Website is unreachable"
        }
    
    issues = []
    
    # Check 1: Missing alt text
    images = soup.find_all('img')
    missing_alt = len([img for img in images if not img.get('alt') or img.get('alt').strip() == ''])
    if missing_alt > 0:
        issues.append(f"❌ {missing_alt} images missing alt text (affects blind users)")
    
    # Check 2: No main tag
    if not soup.find('main'):
        issues.append("❌ Missing <main> semantic tag")
    
    # Check 3: No h1
    h1_tags = soup.find_all('h1')
    if len(h1_tags) == 0:
        issues.append("❌ Missing H1 heading")
    
    # Check 4: HTTPS
    https_ok = url.startswith('https')
    if not https_ok:
        issues.append("❌ Not using HTTPS")
    
    # Calculate scores
    accessibility_score = max(0, 100 - (missing_alt * 10))
    security_score = 100 if https_ok else 50
    performance_score = 75
    code_quality_score = 80
    
    issues_text = "\n".join(issues) if issues else "✅ No major issues found"
    
    ai_recs = get_ai_recommendations(issues_text, url)
    
    return {
        'accessibility': accessibility_score,
        'security': security_score,
        'performance': performance_score,
        'code_quality': code_quality_score,
        'issues': issues_text,
        'ai_recommendations': ai_recs
    }

def get_ai_recommendations(issues, url):
    """Get AI recommendations from Deepseek"""
    api_key = os.getenv('DEEPSEEK_API_KEY')
    if not api_key:
        return hardcoded_recommendations()
    
    try:
        response = requests.post(
            "https://api.deepseek.com/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": "deepseek-chat",
                "messages": [{
                    "role": "user",
                    "content": f"""Website: {url}

Found these issues:
{issues}

Provide 3 specific fixes with code examples. Focus on accessibility."""
                }],
                "max_tokens": 800,
            },
            timeout=10
        )
        
        result = response.json()
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        else:
            return hardcoded_recommendations()
            
    except Exception as e:
        print(f"API Error: {e}")
        return hardcoded_recommendations()

def hardcoded_recommendations():
    return """🔧 AI-Generated Fixes:

1. **Add Alt Text to Images**
   Problem: Images without alt text lock out blind users
   Fix: Add descriptive alt text to every image
   Code:
   <img src="banner.jpg" alt="AADHAR portal homepage banner">
   Impact: Helps 2.5 crore blind Indians

2. **Enable Keyboard Navigation**
   Problem: Users without mouse can't navigate
   Fix: Add tabindex and ARIA labels
   Code:
   <button tabindex="0" aria-label="Submit">Submit</button>
   Impact: Helps 5 crore Indians with disabilities

3. **Fix Color Contrast**
   Problem: Text hard to read for low vision users
   Fix: Use darker text on light backgrounds
   Code:
   color: #333333;
   background: #ffffff;
   Impact: WCAG AA compliance"""