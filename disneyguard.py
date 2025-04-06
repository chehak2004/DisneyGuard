import requests
from bs4 import BeautifulSoup
import json

# Replace this with your actual Gemini API key
API_KEY = "AIzaSyAcfjylzbRh3YOSwi_-vekKQW1VJKk4Epw"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def generate_gemini_response(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(GEMINI_API_URL, headers=headers, data=json.dumps(body))
    if response.status_code == 200:
        result = response.json()
        try:
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "No valid response from Gemini"
    else:
        return f"❌ Error: {response.status_code} {response.text}"

def scrape_piracy_websites():
    piracy_sites = [
        "http://localhost:5000/testsite.html",
        "https://www.wikipedia.org",
        "https://www.imdb.com"
    ]

    violations = []

    for site in piracy_sites:
        try:
            response = requests.get(site, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                text = soup.get_text()[:3000]

                prompt = (
                    "Does the following website content indicate potential piracy "
                    "of Disney or Marvel content? Reply 'Yes' or 'No'.\n\n"
                    f"{text}"
                )

                ai_response = generate_gemini_response(prompt)
                if "yes" in ai_response.lower():
                    violations.append({"site": site, "status": "🚨 Potential Disney piracy detected"})
            else:
                violations.append({"site": site, "status": f"⚠️ HTTP error {response.status_code}"})

        except Exception as e:
            violations.append({"site": site, "status": f"❌ Error: {str(e)}"})

    return violations

if __name__ == "__main__":
    results = scrape_piracy_websites()
    for r in results:
        print(f"{r['site']}: {r['status']}")
