#!/usr/bin/env python3
"""
OSINT Multi-Source Search Tool
Educational Purpose Only
"""

import json
from datetime import datetime

# Search parameters
SEARCH_PARAMS = {
    "username": "طرفة عبدالعزيز الجبالي",
    "phone": "+966558899680",
    "instagram_username": "__tofah__",
    "tiktok_username": "_lemoonah_",
    "email": "",
    "domain": "",
    "hash_value": "",
}

# Define all OSINT sources with URLs
OSINT_SOURCES = {
    "username_search": {
        "Sherlock": "https://github.com/sherlock-project/sherlock",
        "WhatsMyName": "https://github.com/WebBreacher/WhatsMyName",
        "Namechk": "https://namechk.com/",
        "CheckUsernames": "https://checkusernames.com/",
        "Maigret": "https://github.com/soxoj/maigret"
    },
    "phone_search": {
        "PhoneInfoga": "https://github.com/sundowndev/phoneinfoga",
        "TrueCaller": "https://www.truecaller.com/",
        "WhitePages": "https://www.whitepages.com/",
        "PeopleFinder": "https://www.peoplefinder.com/",
        "Spokeo": "https://www.spokeo.com/"
    },
    "email_search": {
        "Hunter.io": "https://hunter.io/",
        "RocketReach": "https://rocketreach.co/",
        "EmailFinder": "https://www.emailfinder.com/",
        "Clearbit": "https://clearbit.com/",
        "MailboxValidator": "https://www.mailboxvalidator.com/"
    },
    "domain_search": {
        "Shodan": "https://www.shodan.io/",
        "Censys": "https://search.censys.io/",
        "WHOIS Lookup": "https://whois.net/",
        "DNS Dumpster": "https://dnsdumpster.com/",
        "SecurityTrails": "https://securitytrails.com/"
    },
    "hash_search": {
        "VirusTotal": "https://www.virustotal.com/",
        "Have I Been Pwned": "https://haveibeenpwned.com/",
        "Hybrid Analysis": "https://www.hybrid-analysis.com/",
        "Malware.Expert": "https://malware.expert/",
        "AlienVault OTX": "https://otx.alienvault.com/"
    }
}

def display_intro():
    """Display introduction"""
    print("╔════════════════════════════════════════════════════╗")
    print("║     OSINT Multi-Source Search Tool v1.0            ║")
    print("║     Educational Purpose Only - Respect Privacy     ║")
    print("╚════════════════════════════════════════════════════╝")
    print()

def display_sources():
    """Display available OSINT sources"""
    print("📊 AVAILABLE OSINT SOURCES:")
    print("=" * 50)
    for category, sources in OSINT_SOURCES.items():
        print(f"\n🔍 {category.replace('_', ' ').upper()}:")
        for i, (source, url) in enumerate(sources.items(), 1):
            print(f"   {i}. {source}")
            print(f"      🔗 {url}")

def display_parameters():
    """Display search parameters"""
    print("\n\n📋 SEARCH PARAMETERS:")
    print("=" * 50)
    for key, value in SEARCH_PARAMS.items():
        status = "✓ SET" if value else "⚠️  EMPTY"
        print(f"{key.upper():<20} : {status}")

def display_instructions():
    """Display usage instructions"""
    print("\n\n📖 INSTRUCTIONS:")
    print("=" * 50)
    print("""
To use this tool:

1. Edit the SEARCH_PARAMS dictionary with your 
   - username: For social media searches
   - phone_number: For phone reverse lookup
   - email: For email finder
   - domain: For domain/infrastructure search
   - hash_value: For malware/breach search

2. Run the tool:
   python3 osint_tool.py

3. Results will be saved to results.json

4. Respect privacy and use legally!
    """)

def generate_report():
    """Generate OSINT report"""
    report = {
        "timestamp": datetime.now().isoformat(),
        "search_parameters": SEARCH_PARAMS,
        "sources_configured": len(OSINT_SOURCES),
        "total_sources": sum(len(v) for v in OSINT_SOURCES.values()),
        "status": "ready",
        "osint_sources": OSINT_SOURCES,
        "results": {}
    }
    
    for key, value in SEARCH_PARAMS.items():
        if value:
            category_key = None
            if "username" in key.lower() or "instagram" in key.lower() or "tiktok" in key.lower():
                category_key = "username_search"
            elif "phone" in key.lower() or "+" in key:
                category_key = "phone_search"
            elif "email" in key.lower():
                category_key = "email_search"
            elif "domain" in key.lower():
                category_key = "domain_search"
            elif "hash" in key.lower():
                category_key = "hash_search"
            
            if category_key:
                report["results"][key] = {
                    "search_term": value,
                    "sources": OSINT_SOURCES.get(category_key, {}),
                    "status": "pending"
                }
    
    return report

def save_report(report):
    """Save report to file"""
    filename = f"osint_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"\n✅ Report saved to: {filename}")

def main():
    """Main function"""
    display_intro()
    display_sources()
    display_parameters()
    display_instructions()
    
    report = generate_report()
    save_report(report)
    
    print("\n✅ OSINT Tool is ready!")
    print("   Fill in SEARCH_PARAMS and run again for actual searches")

if __name__ == "__main__":
    main()
