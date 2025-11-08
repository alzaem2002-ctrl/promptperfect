#!/usr/bin/env python3
"""
Generate Professional HTML OSINT Report
Cyber Security Expert Edition
"""

import json
from datetime import datetime

def load_report(filename):
    """Load JSON report"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_professional_html(report):
    """Generate professional HTML report with verification indicators"""
    
    metadata = report.get('report_metadata', {})
    footprint = report.get('digital_footprint', {})
    verification = report.get('verification_framework', {})
    quality = report.get('quality_assurance', {})
    
    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('report_id', 'OSINT Report')} - Professional Investigation</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3a8a 0%, #7c3aed 100%);
            padding: 20px;
            color: #1f2937;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #1e40af 0%, #7e22ce 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .classification-badge {{
            display: inline-block;
            background: #dc2626;
            color: white;
            padding: 8px 20px;
            border-radius: 20px;
            font-weight: bold;
            margin: 10px 0;
            font-size: 0.9em;
        }}
        .content {{
            padding: 40px;
        }}
        .section {{
            margin: 30px 0;
            padding: 25px;
            background: #f9fafb;
            border-radius: 10px;
            border-right: 5px solid #3b82f6;
        }}
        .section h2 {{
            color: #1e40af;
            font-size: 1.8em;
            margin-bottom: 20px;
            border-bottom: 2px solid #3b82f6;
            padding-bottom: 10px;
        }}
        .section h3 {{
            color: #7c3aed;
            font-size: 1.4em;
            margin: 20px 0 10px 0;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 15px;
            margin: 15px 0;
        }}
        .info-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            border-right: 4px solid #3b82f6;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        .info-card strong {{
            color: #1e40af;
            display: block;
            margin-bottom: 8px;
        }}
        .credibility-badge {{
            display: inline-block;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin: 5px;
        }}
        .credibility-high {{
            background: #10b981;
            color: white;
        }}
        .credibility-medium {{
            background: #f59e0b;
            color: white;
        }}
        .credibility-low {{
            background: #ef4444;
            color: white;
        }}
        .verification-status {{
            background: #fef3c7;
            border-right: 4px solid #f59e0b;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
        }}
        .verification-status.warning {{
            background: #fee2e2;
            border-right-color: #ef4444;
        }}
        .verification-status.success {{
            background: #d1fae5;
            border-right-color: #10b981;
        }}
        .account-card {{
            background: #e0e7ff;
            padding: 20px;
            margin: 15px 0;
            border-radius: 10px;
            border-right: 5px solid #6366f1;
        }}
        .account-card h4 {{
            color: #4f46e5;
            margin-bottom: 15px;
        }}
        .account-card a {{
            color: #4338ca;
            text-decoration: none;
            font-weight: bold;
        }}
        .account-card a:hover {{
            text-decoration: underline;
        }}
        .quality-score {{
            font-size: 2em;
            font-weight: bold;
            color: #1e40af;
            text-align: center;
            padding: 20px;
            background: #eff6ff;
            border-radius: 10px;
            margin: 20px 0;
        }}
        .recommendations {{
            background: #fef3c7;
            padding: 20px;
            border-radius: 10px;
            border-right: 5px solid #f59e0b;
            margin: 20px 0;
        }}
        .recommendations ul {{
            list-style: none;
            padding: 0;
        }}
        .recommendations li {{
            padding: 10px 0;
            border-bottom: 1px solid #fde68a;
            padding-right: 30px;
            position: relative;
        }}
        .recommendations li:before {{
            content: "⚠️";
            position: absolute;
            right: 0;
        }}
        .footer {{
            background: #1f2937;
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .hash-display {{
            font-family: monospace;
            background: #1f2937;
            color: #10b981;
            padding: 10px;
            border-radius: 5px;
            font-size: 0.9em;
            word-break: break-all;
            margin: 10px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        table th, table td {{
            padding: 12px;
            text-align: right;
            border-bottom: 1px solid #e5e7eb;
        }}
        table th {{
            background: #3b82f6;
            color: white;
        }}
        table tr:hover {{
            background: #f3f4f6;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="classification-badge">{metadata.get('classification', 'CONFIDENTIAL')}</div>
            <h1>🔍 تقرير OSINT محترف</h1>
            <p style="margin-top: 10px; opacity: 0.9;">Professional OSINT Investigation Report</p>
            <div style="margin-top: 20px; font-size: 0.9em;">
                <p><strong>Report ID:</strong> {metadata.get('report_id', 'N/A')}</p>
                <p><strong>Investigator:</strong> {metadata.get('investigator', 'N/A')}</p>
                <p><strong>Date:</strong> {metadata.get('timestamp', 'N/A')[:10]}</p>
            </div>
        </div>
        
        <div class="content">
            <!-- Verification Status -->
            <div class="verification-status warning">
                <h3>⚠️ حالة التحقق</h3>
                <p><strong>المستوى الحالي:</strong> أولي (Preliminary)</p>
                <p><strong>ملاحظة مهمة:</strong> جميع البيانات المقدمة أولية وتتطلب التحقق اليدوي والمراجعة المتقاطعة للتأكد من المصداقية.</p>
            </div>
            
            <!-- Quality Score -->
            <div class="quality-score">
                <div>نقاط جودة البيانات</div>
                <div style="font-size: 3em; color: #f59e0b;">{int(quality.get('data_quality_score', 0) * 100)}%</div>
                <div style="font-size: 0.6em; color: #6b7280; margin-top: 10px;">Preliminary Data - Manual Verification Required</div>
            </div>
            
            <!-- Digital Footprint -->
            <div class="section">
                <h2>👣 البصمة الرقمية والتحقق</h2>
"""
    
    # Name Connections
    if footprint.get('name_connections'):
        name_conn = footprint['name_connections']
        html += f"""
                <div class="account-card">
                    <h3>🔗 ربط الأسماء والتحقق</h3>
                    <div class="info-grid">
                        <div class="info-card">
                            <strong>الاسم الأساسي:</strong> {name_conn.get('primary_name', 'N/A')}
                        </div>
                        <div class="info-card">
                            <strong>الأسماء المستعارة:</strong> {', '.join(name_conn.get('aliases', []))}
                        </div>
                    </div>
                    <div class="verification-status warning">
                        <strong>ملاحظة التحقق:</strong> {name_conn.get('verification_notes', 'يتطلب التحقق اليدوي')}
                    </div>
                </div>
"""
    
    # Cross-Platform Links
    if footprint.get('cross_platform_links'):
        html += """
                <div class="account-card" style="background: #fef3c7;">
                    <h3>🌐 الروابط عبر المنصات</h3>
"""
        for link in footprint['cross_platform_links']:
            html += f"""
                    <p><strong>الاسم الأساسي:</strong> {link.get('primary_name', 'N/A')}</p>
                    <p><strong>حالة التحقق:</strong> <span class="credibility-badge credibility-medium">{link.get('verification_status', 'pending')}</span></p>
                    <h4>المنصات المرتبطة:</h4>
                    <div class="info-grid">
"""
            for platform in link.get('platforms', []):
                platform_name = platform.get('platform', 'N/A')
                username = platform.get('username', platform.get('number', 'N/A'))
                verification_status = platform.get('verification_status', 'pending')
                
                html += f"""
                        <div class="info-card">
                            <strong>{platform_name}</strong><br>
                            <span>{username}</span><br>
                            <small>حالة التحقق: <span class="credibility-badge credibility-medium">{verification_status}</span></small>
"""
                if platform.get('user_id'):
                    html += f"<br><small>معرف المستخدم: {platform['user_id']}</small>"
                html += "</div>\n"
            
            html += """
                    </div>
                </div>
"""
    
    # Activity Analysis
    if footprint.get('activity_analysis'):
        activity = footprint['activity_analysis']
        html += """
                <div class="account-card" style="background: #f3e5f5;">
                    <h3>📊 تحليل النشاط والمشاركات</h3>
"""
        
        # Instagram
        if activity.get('instagram_activity'):
            insta = activity['instagram_activity']
            html += f"""
                    <h4>📷 نشاط Instagram</h4>
                    <div class="info-grid">
                        <div class="info-card">
                            <strong>اسم المستخدم:</strong> {insta.get('username', 'N/A')}
                        </div>
                        <div class="info-card">
                            <strong>الرابط:</strong> <a href="{insta.get('profile_url', '#')}" target="_blank">{insta.get('profile_url', 'N/A')}</a>
                        </div>
                        <div class="info-card">
                            <strong>حالة التحقق:</strong> <span class="credibility-badge credibility-medium">{insta.get('verification_status', 'pending')}</span>
                        </div>
                    </div>
                    <div class="verification-status warning">
                        <strong>ملاحظة المصداقية:</strong> {insta.get('credibility_note', 'يتطلب التحقق')}
                    </div>
"""
        
        # TikTok
        if activity.get('tiktok_activity'):
            tiktok = activity['tiktok_activity']
            html += f"""
                    <h4>🎵 نشاط TikTok</h4>
                    <div class="info-grid">
                        <div class="info-card">
                            <strong>اسم المستخدم:</strong> {tiktok.get('username', 'N/A')}
                        </div>
                        <div class="info-card">
                            <strong>معرف المستخدم:</strong> {tiktok.get('user_id', 'N/A')}
                        </div>
                        <div class="info-card">
                            <strong>الرابط:</strong> <a href="{tiktok.get('profile_url', '#')}" target="_blank">{tiktok.get('profile_url', 'N/A')}</a>
                        </div>
                        <div class="info-card">
                            <strong>حالة التحقق:</strong> <span class="credibility-badge credibility-medium">{tiktok.get('verification_status', 'pending')}</span>
                        </div>
                    </div>
                    <div class="verification-status warning">
                        <strong>ملاحظة المصداقية:</strong> {tiktok.get('credibility_note', 'يتطلب التحقق')}
                    </div>
"""
        
        html += """
                </div>
"""
    
    # Source Credibility
    if verification.get('source_credibility'):
        html += """
            <div class="section">
                <h2>📊 مصداقية المصادر</h2>
"""
        for source_type, cred_info in verification['source_credibility'].items():
            cred_level = cred_info.get('credibility_level', 'unknown')
            cred_class = f"credibility-{cred_level}" if cred_level != 'unknown' else "credibility-medium"
            
            html += f"""
                <div class="info-card">
                    <h4>{source_type.replace('_', ' ').title()}</h4>
                    <p><strong>مستوى المصداقية:</strong> <span class="credibility-badge {cred_class}">{cred_level}</span></p>
                    <p><strong>عدد المصادر:</strong> {cred_info.get('sources_count', 0)}</p>
                    <p><strong>مصادر عالية المصداقية:</strong> {cred_info.get('high_credibility_sources', 0)}</p>
                </div>
"""
        html += """
            </div>
"""
    
    # Recommendations
    if quality.get('recommendations'):
        html += f"""
            <div class="recommendations">
                <h2>💡 التوصيات والخطوات التالية</h2>
                <ul>
"""
        for rec in quality['recommendations']:
            html += f"<li>{rec}</li>\n"
        
        html += """
                </ul>
            </div>
"""
    
    # Data Integrity
    html += f"""
            <div class="section">
                <h2>🔐 سلامة البيانات</h2>
                <div class="info-card">
                    <strong>Data Integrity Hash:</strong>
                    <div class="hash-display">{metadata.get('data_integrity_hash', 'N/A')}</div>
                    <p style="margin-top: 10px; font-size: 0.9em; color: #6b7280;">
                        هذا الـ Hash يضمن سلامة البيانات وعدم التلاعب بها
                    </p>
                </div>
            </div>
"""
    
    html += """
        </div>
        
        <div class="footer">
            <p><strong>Professional OSINT Investigation Report</strong></p>
            <p style="margin-top: 10px; font-size: 0.9em; opacity: 0.8;">
                هذا التقرير يحتوي على بيانات أولية - يتطلب التحقق اليدوي والمراجعة المتقاطعة
            </p>
            <p style="margin-top: 10px; font-size: 0.8em; opacity: 0.7;">
                Report Generated: {metadata.get('timestamp', 'N/A')}
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    """Main function"""
    filename = "osint_professional_report_20251108_170708.json"
    report = load_report(filename)
    html = generate_professional_html(report)
    
    output_filename = "osint_professional_report_20251108_170708.html"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Professional HTML Report generated: {output_filename}")

if __name__ == "__main__":
    main()
