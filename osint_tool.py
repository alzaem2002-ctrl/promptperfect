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
    """Generate OSINT report with digital footprint analysis and verification"""
    report = {
        "timestamp": datetime.now().isoformat(),
        "report_metadata": {
            "report_type": "Professional OSINT Investigation",
            "methodology": "OSINT Best Practices",
            "verification_level": "Preliminary - Manual Review Required",
            "credibility_note": "جميع البيانات أولية وتتطلب التحقق اليدوي"
        },
        "search_parameters": SEARCH_PARAMS,
        "sources_configured": len(OSINT_SOURCES),
        "total_sources": sum(len(v) for v in OSINT_SOURCES.values()),
        "status": "ready",
        "osint_sources": OSINT_SOURCES,
        "results": {},
        "found_accounts": [],
        "connected_accounts": [],
        "messages": [],
        "available_images": [],
        "digital_footprint": {
            "name_connections": {},
            "activity_analysis": {},
            "cross_platform_links": [],
            "verification_status": "pending_manual_review"
        },
        "quality_assurance": {
            "data_quality_score": 0.3,
            "verification_required": True,
            "recommendations": [
                "إجراء فحص يدوي لجميع الحسابات المذكورة",
                "التحقق من مطابقة الأسماء عبر المنصات",
                "إجراء بحث عكسي لرقم الهاتف",
                "التحقق من صحة معرفات المستخدمين",
                "تحليل المحتوى المنشور للتحقق من الهوية"
            ]
        }
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
    
    # Add found accounts based on search parameters with verification status
    if SEARCH_PARAMS.get("instagram_username"):
        report["found_accounts"].append({
            "platform": "Instagram",
            "username": SEARCH_PARAMS["instagram_username"],
            "url": f"https://instagram.com/{SEARCH_PARAMS['instagram_username']}",
            "status": "requires_verification",
            "verification_status": "pending",
            "profile_info": {
                "display_name": "يتطلب التحقق",
                "bio": "يتطلب التحقق",
                "followers": "يتطلب التحقق",
                "following": "يتطلب التحقق",
                "posts": "يتطلب التحقق"
            },
            "credibility_note": "المعلومات المقدمة أولية - يتطلب فحص يدوي للملف الشخصي للتأكد من المطابقة"
        })
    
    if SEARCH_PARAMS.get("tiktok_username"):
        report["found_accounts"].append({
            "platform": "TikTok",
            "username": SEARCH_PARAMS["tiktok_username"],
            "url": f"https://tiktok.com/@{SEARCH_PARAMS['tiktok_username']}",
            "status": "requires_verification",
            "verification_status": "pending",
            "profile_info": {
                "display_name": "يتطلب التحقق",
                "bio": "يتطلب التحقق",
                "followers": "يتطلب التحقق",
                "following": "يتطلب التحقق",
                "likes": "يتطلب التحقق",
                "user_id": SEARCH_PARAMS.get("tiktok_user_id", "")
            },
            "credibility_note": "المعلومات المقدمة أولية - يتطلب فحص يدوي للملف الشخصي للتأكد من المطابقة"
        })
    
    # Build name connections and digital footprint
    primary_name = SEARCH_PARAMS.get("name", "")
    username = SEARCH_PARAMS.get("username", "")
    
    # Create name connections mapping
    name_variations = []
    if primary_name:
        name_variations.append(primary_name)
    if username and username != primary_name:
        name_variations.append(username)
    
    # Build cross-platform identity links
    cross_platform_identity = {
        "primary_name": primary_name,
        "name_variations": name_variations,
        "platforms": []
    }
    
    # Add Instagram connection
    if SEARCH_PARAMS.get("instagram_username"):
        cross_platform_identity["platforms"].append({
            "platform": "Instagram",
            "username": SEARCH_PARAMS["instagram_username"],
            "name_used": primary_name,
            "connection_type": "username_match"
        })
    
    # Add TikTok connection
    if SEARCH_PARAMS.get("tiktok_username"):
        cross_platform_identity["platforms"].append({
            "platform": "TikTok",
            "username": SEARCH_PARAMS["tiktok_username"],
            "user_id": SEARCH_PARAMS.get("tiktok_user_id", ""),
            "name_used": primary_name,
            "connection_type": "username_match"
        })
    
    # Add phone connection
    if SEARCH_PARAMS.get("phone"):
        cross_platform_identity["platforms"].append({
            "platform": "Phone",
            "number": SEARCH_PARAMS["phone"],
            "name_used": primary_name,
            "connection_type": "contact_info"
        })
    
    report["digital_footprint"]["cross_platform_links"] = [cross_platform_identity]
    
    # Build name connections dictionary with verification notes
    report["digital_footprint"]["name_connections"] = {
        "primary_name": primary_name,
        "aliases": name_variations,
        "platform_usernames": {
            "Instagram": SEARCH_PARAMS.get("instagram_username", ""),
            "TikTok": SEARCH_PARAMS.get("tiktok_username", ""),
            "General": SEARCH_PARAMS.get("username", "")
        },
        "contact_info": {
            "phone": SEARCH_PARAMS.get("phone", ""),
            "email": SEARCH_PARAMS.get("email", "")
        },
        "verification_notes": "يتطلب التحقق اليدوي من المطابقة بين الأسماء والحسابات - البيانات أولية"
    }
    
    # Build activity analysis structure with credibility notes
    report["digital_footprint"]["activity_analysis"] = {
        "instagram_activity": {
            "username": SEARCH_PARAMS.get("instagram_username", ""),
            "profile_url": f"https://instagram.com/{SEARCH_PARAMS.get('instagram_username', '')}" if SEARCH_PARAMS.get("instagram_username") else "",
            "verification_status": "pending",
            "posts_analysis": "يتطلب الوصول المباشر للملف الشخصي للتحقق",
            "hashtags_used": [],
            "locations_tagged": [],
            "people_tagged": [],
            "activity_timeline": [],
            "credibility_note": "البيانات المقدمة أولية - يتطلب تحقق يدوي من الملف الشخصي"
        },
        "tiktok_activity": {
            "username": SEARCH_PARAMS.get("tiktok_username", ""),
            "user_id": SEARCH_PARAMS.get("tiktok_user_id", ""),
            "profile_url": f"https://tiktok.com/@{SEARCH_PARAMS.get('tiktok_username', '')}" if SEARCH_PARAMS.get("tiktok_username") else "",
            "verification_status": "pending",
            "videos_analysis": "يتطلب الوصول المباشر للملف الشخصي للتحقق",
            "sounds_used": [],
            "hashtags_used": [],
            "activity_timeline": [],
            "credibility_note": "البيانات المقدمة أولية - يتطلب تحقق يدوي من الملف الشخصي"
        },
        "general_activity": {
            "name_mentions": [],
            "cross_platform_activity": [],
            "digital_presence_summary": f"وجود رقمي محتمل على منصات متعددة مرتبطة بالاسم: {primary_name}",
            "verification_level": "preliminary"
        }
    }
    
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
    
    # Add Digital Footprint Section
    if report.get('digital_footprint'):
        footprint = report['digital_footprint']
        
        html += """
        <h2>👣 البصمة الرقمية وربط الأسماء</h2>
"""
        
        # Name Connections
        if footprint.get('name_connections'):
            name_conn = footprint['name_connections']
            html += f"""
        <div class="account-card" style="background: #e8f5e9;">
            <h3>🔗 ربط الأسماء</h3>
            <p><strong>الاسم الأساسي:</strong> {name_conn.get('primary_name', 'N/A')}</p>
            <p><strong>الأسماء المستعارة:</strong> {', '.join(name_conn.get('aliases', []))}</p>
            <h4>أسماء المستخدمين عبر المنصات:</h4>
            <ul class="source-list">
"""
            for platform, username in name_conn.get('platform_usernames', {}).items():
                if username:
                    html += f"<li><strong>{platform}:</strong> {username}</li>\n"
            html += """
            </ul>
            <h4>معلومات الاتصال:</h4>
            <ul class="source-list">
"""
            contact = name_conn.get('contact_info', {})
            if contact.get('phone'):
                html += f"<li><strong>الهاتف:</strong> {contact['phone']}</li>\n"
            if contact.get('email'):
                html += f"<li><strong>البريد:</strong> {contact['email']}</li>\n"
            html += """
            </ul>
        </div>
"""
        
        # Cross-Platform Links
        if footprint.get('cross_platform_links'):
            html += """
        <div class="account-card" style="background: #fff3e0;">
            <h3>🌐 الروابط عبر المنصات</h3>
"""
            for link in footprint['cross_platform_links']:
                html += f"""
            <p><strong>الاسم الأساسي:</strong> {link.get('primary_name', 'N/A')}</p>
            <p><strong>الأسماء المستخدمة:</strong> {', '.join(link.get('name_variations', []))}</p>
            <h4>المنصات المرتبطة:</h4>
            <ul class="source-list">
"""
                for platform in link.get('platforms', []):
                    platform_name = platform.get('platform', 'N/A')
                    username = platform.get('username', platform.get('number', 'N/A'))
                    connection_type = platform.get('connection_type', 'N/A')
                    html += f"""
                <li>
                    <strong>{platform_name}:</strong> {username}<br>
                    <small>نوع الربط: {connection_type}</small>
"""
                    if platform.get('user_id'):
                        html += f"<br><small>معرف المستخدم: {platform['user_id']}</small>"
                    html += "</li>\n"
                html += """
            </ul>
        </div>
"""
        
        # Activity Analysis
        if footprint.get('activity_analysis'):
            activity = footprint['activity_analysis']
            html += """
        <div class="account-card" style="background: #f3e5f5;">
            <h3>📊 تحليل النشاط والمشاركات</h3>
"""
            
            # Instagram Activity
            if activity.get('instagram_activity'):
                insta = activity['instagram_activity']
                if insta.get('username'):
                    html += f"""
            <h4>📷 نشاط Instagram</h4>
            <p><strong>اسم المستخدم:</strong> {insta.get('username', 'N/A')}</p>
            <p><strong>الرابط:</strong> <a href="{insta.get('profile_url', '#')}" target="_blank">{insta.get('profile_url', 'N/A')}</a></p>
            <p><strong>تحليل المنشورات:</strong> {insta.get('posts_analysis', 'N/A')}</p>
            <p><strong>الهاشتاقات المستخدمة:</strong> {', '.join(insta.get('hashtags_used', [])) if insta.get('hashtags_used') else 'لم يتم تحديدها بعد'}</p>
            <p><strong>المواقع المحددة:</strong> {', '.join(insta.get('locations_tagged', [])) if insta.get('locations_tagged') else 'لم يتم تحديدها بعد'}</p>
            <p><strong>الأشخاص المحددين:</strong> {', '.join(insta.get('people_tagged', [])) if insta.get('people_tagged') else 'لم يتم تحديدهم بعد'}</p>
"""
            
            # TikTok Activity
            if activity.get('tiktok_activity'):
                tiktok = activity['tiktok_activity']
                if tiktok.get('username'):
                    html += f"""
            <h4>🎵 نشاط TikTok</h4>
            <p><strong>اسم المستخدم:</strong> {tiktok.get('username', 'N/A')}</p>
            <p><strong>معرف المستخدم:</strong> {tiktok.get('user_id', 'N/A')}</p>
            <p><strong>الرابط:</strong> <a href="{tiktok.get('profile_url', '#')}" target="_blank">{tiktok.get('profile_url', 'N/A')}</a></p>
            <p><strong>تحليل الفيديوهات:</strong> {tiktok.get('videos_analysis', 'N/A')}</p>
            <p><strong>الأصوات المستخدمة:</strong> {', '.join(tiktok.get('sounds_used', [])) if tiktok.get('sounds_used') else 'لم يتم تحديدها بعد'}</p>
            <p><strong>الهاشتاقات المستخدمة:</strong> {', '.join(tiktok.get('hashtags_used', [])) if tiktok.get('hashtags_used') else 'لم يتم تحديدها بعد'}</p>
"""
            
            # General Activity
            if activity.get('general_activity'):
                general = activity['general_activity']
                html += f"""
            <h4>🌍 النشاط العام</h4>
            <p><strong>ملخص البصمة الرقمية:</strong> {general.get('digital_presence_summary', 'N/A')}</p>
            <p><strong>الإشارات للاسم:</strong> {', '.join(general.get('name_mentions', [])) if general.get('name_mentions') else 'لم يتم العثور عليها بعد'}</p>
"""
            
            html += """
        </div>
"""
    
    # Add Quality Assurance Section
    if report.get('quality_assurance'):
        quality = report['quality_assurance']
        html += """
        <h2>✅ ضمان الجودة والتحقق</h2>
        <div class="account-card" style="background: #fef3c7; border-right-color: #f59e0b;">
            <h3>📊 تقييم جودة البيانات</h3>
            <p><strong>نقاط الجودة:</strong> <span style="font-size: 1.5em; color: #f59e0b; font-weight: bold;">{:.0%}</span></p>
            <p><strong>حالة التحقق:</strong> <span class="status pending">يتطلب مراجعة يدوية</span></p>
""".format(quality.get('data_quality_score', 0))
        
        if quality.get('recommendations'):
            html += """
            <h4>💡 التوصيات:</h4>
            <ul class="source-list">
"""
            for rec in quality['recommendations']:
                html += f"<li>{rec}</li>\n"
            html += """
            </ul>
"""
        html += """
        </div>
"""
    
    # Add Report Metadata
    if report.get('report_metadata'):
        metadata = report['report_metadata']
        html += f"""
        <h2>📋 معلومات التقرير</h2>
        <div class="account-card" style="background: #e0e7ff;">
            <p><strong>نوع التقرير:</strong> {metadata.get('report_type', 'N/A')}</p>
            <p><strong>المنهجية:</strong> {metadata.get('methodology', 'N/A')}</p>
            <p><strong>مستوى التحقق:</strong> {metadata.get('verification_level', 'N/A')}</p>
            <div class="verification-status warning" style="margin-top: 15px;">
                <strong>⚠️ ملاحظة مهمة:</strong> {metadata.get('credibility_note', 'البيانات أولية وتتطلب التحقق')}
            </div>
        </div>
"""
    
    html += f"""
        <div style="margin-top: 30px; padding-top: 20px; border-top: 2px solid #eee; text-align: center; color: #666;">
            <p>Total Sources: {report['total_sources']} | Status: <span class="status {report['status']}">{report['status']}</span></p>
            <p style="font-size: 12px; margin-top: 10px;">
                <strong>⚠️ Professional OSINT Report - Preliminary Data</strong><br>
                Manual verification and cross-referencing required for accuracy<br>
                Educational Purpose Only - Respect Privacy
            </p>
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
