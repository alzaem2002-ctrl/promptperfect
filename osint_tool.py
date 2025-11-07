#!/usr/bin/env python3
"""
OSINT Multi-Source Search Tool
Educational Purpose Only
"""

import json
from datetime import datetime

# Search parameters
SEARCH_PARAMS = {
    "name": "طرفة عبدالعزيز الجبالي",
    "username": "طرفة عبدالعزيز الجبالي",
    "phone": "+966558899680",
    "instagram_username": "__tofah__",
    "tiktok_username": "_lemoonah_",
    "tiktok_user_id": "7243145311366988805",
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
        "results": {},
        "found_accounts": [],
        "connected_accounts": [],
        "messages": [],
        "available_images": []
    }
    
    for key, value in SEARCH_PARAMS.items():
        if value:
            category_key = None
            if "name" in key.lower() or "username" in key.lower() or "instagram" in key.lower() or "tiktok" in key.lower():
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
    
    # Add found accounts based on search parameters
    if SEARCH_PARAMS.get("instagram_username"):
        report["found_accounts"].append({
            "platform": "Instagram",
            "username": SEARCH_PARAMS["instagram_username"],
            "url": f"https://instagram.com/{SEARCH_PARAMS['instagram_username']}",
            "status": "found",
            "profile_info": {
                "display_name": "",
                "bio": "",
                "followers": "",
                "following": "",
                "posts": ""
            }
        })
    
    if SEARCH_PARAMS.get("tiktok_username"):
        report["found_accounts"].append({
            "platform": "TikTok",
            "username": SEARCH_PARAMS["tiktok_username"],
            "url": f"https://tiktok.com/@{SEARCH_PARAMS['tiktok_username']}",
            "status": "found",
            "profile_info": {
                "display_name": "",
                "bio": "",
                "followers": "",
                "following": "",
                "likes": "",
                "user_id": SEARCH_PARAMS.get("tiktok_user_id", "")
            }
        })
    
    # Add connected/related accounts section (to be filled with discovered accounts)
    # This section will contain accounts found through mutual connections, 
    # similar usernames, phone number lookups, etc.
    
    return report

def save_report(report):
    """Save report to file"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_filename = f"osint_report_{timestamp}.json"
    html_filename = f"osint_report_{timestamp}.html"
    
    # Save JSON
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\n✅ JSON Report saved to: {json_filename}")
    
    # Save HTML
    html_content = generate_html_report(report)
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML Report saved to: {html_filename}")

def generate_html_report(report):
    """Generate HTML version of the report"""
    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSINT Report - {report['timestamp']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 30px;
        }}
        h1 {{
            color: #667eea;
            text-align: center;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #764ba2;
            margin-top: 30px;
            border-right: 4px solid #764ba2;
            padding-right: 10px;
        }}
        .search-param {{
            background: #f8f9fa;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-right: 4px solid #667eea;
        }}
        .search-param strong {{
            color: #667eea;
        }}
        .source-list {{
            list-style: none;
            padding: 0;
        }}
        .source-item {{
            background: #f8f9fa;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            border-right: 3px solid #764ba2;
        }}
        .source-item a {{
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }}
        .source-item a:hover {{
            color: #764ba2;
            text-decoration: underline;
        }}
        .status {{
            display: inline-block;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }}
        .status.ready {{
            background: #28a745;
            color: white;
        }}
        .status.pending {{
            background: #ffc107;
            color: #333;
        }}
        .timestamp {{
            text-align: center;
            color: #666;
            font-style: italic;
            margin-bottom: 20px;
        }}
        .empty {{
            color: #999;
            font-style: italic;
        }}
        .account-card {{
            background: #e8f4f8;
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            border-right: 4px solid #17a2b8;
        }}
        .message-item {{
            background: #fff3cd;
            padding: 12px;
            margin: 8px 0;
            border-radius: 5px;
            border-right: 3px solid #ffc107;
        }}
        .image-gallery {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }}
        .image-item {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }}
        .image-item img {{
            max-width: 100%;
            height: auto;
            border-radius: 5px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 OSINT Multi-Source Search Report</h1>
        <p class="timestamp">Generated: {report['timestamp']}</p>
        
        <h2>📋 Search Parameters</h2>
"""
    
    for key, value in report['search_parameters'].items():
        if value:
            html += f"""
        <div class="search-param">
            <strong>{key.replace('_', ' ').title()}:</strong> {value}
        </div>
"""
        else:
            html += f"""
        <div class="search-param empty">
            <strong>{key.replace('_', ' ').title()}:</strong> (Empty)
        </div>
"""
    
    html += """
        <h2>🔗 OSINT Sources & Links</h2>
"""
    
    for category, sources in report['osint_sources'].items():
        html += f"""
        <h3>{category.replace('_', ' ').title()}</h3>
        <ul class="source-list">
"""
        for source, url in sources.items():
            html += f"""
            <li class="source-item">
                <strong>{source}:</strong> <a href="{url}" target="_blank">{url}</a>
            </li>
"""
        html += """
        </ul>
"""
    
    html += """
        <h2>📊 Search Results</h2>
"""
    
    if report['results']:
        for key, result in report['results'].items():
            html += f"""
        <div class="search-param">
            <strong>Search Term:</strong> {result['search_term']}<br>
            <strong>Status:</strong> <span class="status {result['status']}">{result['status']}</span><br>
            <strong>Available Sources:</strong>
            <ul class="source-list">
"""
            for source, url in result['sources'].items():
                html += f"""
                <li class="source-item">
                    <a href="{url}" target="_blank">{source}</a>
                </li>
"""
            html += """
            </ul>
        </div>
"""
    else:
        html += """
        <p class="empty">No search results yet. Fill in search parameters and run the tool.</p>
"""
    
    # Add Found Accounts Section
    html += """
        <h2>👤 Found Accounts</h2>
"""
    if report.get('found_accounts'):
        for account in report['found_accounts']:
            html += f"""
        <div class="account-card">
            <strong>Platform:</strong> {account['platform']}<br>
            <strong>Username:</strong> {account['username']}<br>
            <strong>URL:</strong> <a href="{account['url']}" target="_blank">{account['url']}</a><br>
            <strong>Status:</strong> <span class="status {account['status']}">{account['status']}</span><br>
"""
            if account.get('profile_info'):
                html += "<strong>Profile Info:</strong><ul>"
                for key, value in account['profile_info'].items():
                    if value:
                        html += f"<li>{key.replace('_', ' ').title()}: {value}</li>"
                html += "</ul>"
            html += """
        </div>
"""
    else:
        html += """
        <p class="empty">No accounts found yet.</p>
"""
    
    # Add Connected/Related Accounts Section
    html += """
        <h2>🔗 Connected/Related Accounts</h2>
        <p style="color: #666; font-style: italic;">Accounts discovered through mutual connections, similar usernames, phone lookups, or other OSINT methods</p>
"""
    if report.get('connected_accounts'):
        for account in report['connected_accounts']:
            html += f"""
        <div class="account-card" style="background: #f0f8ff;">
            <strong>Platform:</strong> {account.get('platform', 'N/A')}<br>
            <strong>Username:</strong> {account.get('username', 'N/A')}<br>
            <strong>URL:</strong> <a href="{account.get('url', '#')}" target="_blank">{account.get('url', 'N/A')}</a><br>
            <strong>Connection Type:</strong> {account.get('connection_type', 'Unknown')}<br>
            <strong>Status:</strong> <span class="status {account.get('status', 'unknown')}">{account.get('status', 'unknown')}</span><br>
"""
            if account.get('profile_info'):
                html += "<strong>Profile Info:</strong><ul>"
                for key, value in account['profile_info'].items():
                    if value:
                        html += f"<li>{key.replace('_', ' ').title()}: {value}</li>"
                html += "</ul>"
            if account.get('notes'):
                html += f"<strong>Notes:</strong> {account['notes']}<br>"
            html += """
        </div>
"""
    else:
        html += """
        <p class="empty">No connected accounts found yet. Use OSINT tools to discover related accounts through:
        <ul style="text-align: right; margin-top: 10px;">
            <li>Mutual followers/following on social media</li>
            <li>Phone number reverse lookup</li>
            <li>Similar username searches</li>
            <li>Email address associations</li>
            <li>Cross-platform username matching</li>
        </ul>
        </p>
"""
    
    # Add Messages Section
    html += """
        <h2>💬 Messages</h2>
"""
    if report.get('messages'):
        for msg in report['messages']:
            html += f"""
        <div class="message-item">
            <strong>Date:</strong> {msg.get('date', 'N/A')}<br>
            <strong>Platform:</strong> {msg.get('platform', 'N/A')}<br>
            <strong>Content:</strong> {msg.get('content', '')}<br>
            <strong>Sender:</strong> {msg.get('sender', 'N/A')}<br>
"""
            if msg.get('attachments'):
                html += f"<strong>Attachments:</strong> {', '.join(msg['attachments'])}<br>"
            html += """
        </div>
"""
    else:
        html += """
        <p class="empty">No messages found yet.</p>
"""
    
    # Add Available Images Section
    html += """
        <h2>🖼️ Available Images</h2>
"""
    if report.get('available_images'):
        html += '<div class="image-gallery">'
        for img in report['available_images']:
            html += f"""
        <div class="image-item">
            <img src="{img.get('url', '')}" alt="{img.get('description', 'Image')}" onerror="this.style.display='none'">
            <p><strong>{img.get('description', 'Image')}</strong></p>
            <p><a href="{img.get('url', '')}" target="_blank">View Full Size</a></p>
            <p><small>Source: {img.get('source', 'N/A')}</small></p>
        </div>
"""
        html += '</div>'
    else:
        html += """
        <p class="empty">No images found yet.</p>
"""
    
    html += f"""
        <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #eee; text-align: center; color: #666;">
            <p>Total Sources: {report['total_sources']} | Status: <span class="status {report['status']}">{report['status']}</span></p>
            <p style="font-size: 12px;">Educational Purpose Only - Respect Privacy</p>
        </div>
    </div>
</body>
</html>
"""
    return html

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
