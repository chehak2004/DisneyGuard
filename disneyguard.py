import requests
from bs4 import BeautifulSoup

def scrape_piracy_websites():
    """Scans websites for piracy-related content."""
    piracy_sites = [
        "https://examplepiracy.com",
        "https://anotherpiratesite.com"
    ]
    violations = []
    
    for site in piracy_sites:
        try:
            response = requests.get(site, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()
                
                if "Disney" in text or "Marvel" in text:
                    violations.append({"site": site, "status": "Potential Disney content found"})
        except Exception as e:
            violations.append({"site": site, "status": f"Error: {str(e)}"})
    
    return violations
