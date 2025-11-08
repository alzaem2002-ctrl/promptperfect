#!/usr/bin/env python3
"""
Convert professional OSINT JSON report to HTML
"""

import json
from datetime import datetime

def load_report(filename):
    """Load JSON report"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_html(report_data):
    """Generate professional HTML report"""
    
    report = report_data.get('osint_report', {})
    metadata = report.get('metadata', {})
    summary = report.get('executive_summary', {})
    target_info = report.get('target_information', {})
    findings = report.get('findings', {})
    
    html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{metadata.get('report_title', 'OSINT Report')}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            padding: 40px;
        }}
        .header {{
            text-align: center;
            border-bottom: 4px solid #667eea;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .header h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header .metadata {{
            color: #666;
            font-size: 0.9em;
        }}
        .classification {{
            background: #dc3545;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            margin: 10px 0;
            font-weight: bold;
        }}
        .section {{
            margin: 30px 0;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            border-right: 4px solid #764ba2;
        }}
        .section h2 {{
            color: #764ba2;
            font-size: 1.8em;
            margin-bottom: 15px;
            border-bottom: 2px solid #764ba2;
            padding-bottom: 10px;
        }}
        .section h3 {{
            color: #667eea;
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
            padding: 15px;
            border-radius: 5px;
            border-right: 3px solid #667eea;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .info-card strong {{
            color: #667eea;
            display: block;
            margin-bottom: 5px;
        }}
        .account-card {{
            background: #e8f4f8;
            padding: 20px;
            margin: 15px 0;
            border-radius: 8px;
            border-right: 4px solid #17a2b8;
        }}
        .account-card h4 {{
            color: #17a2b8;
            font-size: 1.3em;
            margin-bottom: 10px;
        }}
        .account-card a {{
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }}
        .account-card a:hover {{
            text-decoration: underline;
        }}
        .list-item {{
            background: white;
            padding: 10px;
            margin: 8px 0;
            border-radius: 5px;
            border-right: 3px solid #764ba2;
        }}
        .badge {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.85em;
            font-weight: bold;
            margin: 5px;
        }}
        .badge-success {{
            background: #28a745;
            color: white;
        }}
        .badge-warning {{
            background: #ffc107;
            color: #333;
        }}
        .badge-danger {{
            background: #dc3545;
            color: white;
        }}
        .badge-info {{
            background: #17a2b8;
            color: white;
        }}
        ul {{
            list-style: none;
            padding: 0;
        }}
        ul li {{
            padding: 8px 0;
            border-bottom: 1px solid #eee;
        }}
        ul li:before {{
            content: "▸ ";
            color: #667eea;
            font-weight: bold;
            margin-left: 10px;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 2px solid #eee;
            text-align: center;
            color: #666;
            font-size: 0.9em;
        }}
        .highlight {{
            background: #fff3cd;
            padding: 15px;
            border-radius: 5px;
            border-right: 4px solid #ffc107;
            margin: 15px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        table th, table td {{
            padding: 12px;
            text-align: right;
            border-bottom: 1px solid #ddd;
        }}
        table th {{
            background: #667eea;
            color: white;
        }}
        table tr:hover {{
            background: #f5f5f5;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="classification">{metadata.get('classification_level', 'سري')}</div>
            <h1>{metadata.get('report_title', 'تقرير OSINT')}</h1>
            <div class="metadata">
                <p><strong>معرف التقرير:</strong> {metadata.get('report_id', 'N/A')}</p>
                <p><strong>تاريخ الإنشاء:</strong> {metadata.get('date_created', 'N/A')}</p>
                <p><strong>المحلل:</strong> {metadata.get('investigator_name', 'N/A')}</p>
                <p><strong>الإصدار:</strong> {metadata.get('report_version', '1.0')}</p>
            </div>
        </div>

        <div class="section">
            <h2>📋 الملخص التنفيذي</h2>
            <div class="highlight">
                <h3>الغرض من التحقيق</h3>
                <p>{summary.get('investigation_purpose', 'N/A')}</p>
            </div>
            <h3>النتائج الرئيسية</h3>
            <ul>
"""
    
    for finding in summary.get('key_findings', []):
        html += f"<li>{finding}</li>\n"
    
    html += f"""
            </ul>
            <h3>تقييم المخاطر</h3>
            <p><span class="badge badge-warning">{summary.get('risk_assessment', 'N/A')}</span></p>
            <h3>التوصيات</h3>
            <ul>
"""
    
    for rec in summary.get('recommendations', []):
        html += f"<li>{rec}</li>\n"
    
    html += """
            </ul>
        </div>

        <div class="section">
            <h2>🎯 معلومات الهدف</h2>
"""
    
    for target in target_info.get('primary_targets', []):
        html += f"""
            <div class="info-card">
                <strong>معرف الهدف:</strong> {target.get('target_id', 'N/A')}<br>
                <strong>النوع:</strong> {target.get('target_type', 'N/A')}<br>
                <strong>الاسم:</strong> {target.get('target_name', 'N/A')}<br>
                <strong>الأولوية:</strong> <span class="badge badge-danger">{target.get('priority_level', 'N/A')}</span><br>
                <strong>المعرفات المرتبطة:</strong>
                <ul>
"""
        for identifier in target.get('associated_identifiers', []):
            html += f"<li>{identifier}</li>\n"
        
        html += """
                </ul>
            </div>
"""
    
    html += """
        </div>

        <div class="section">
            <h2>📱 الحسابات الرقمية</h2>
"""
    
    digital_footprint = findings.get('digital_footprint', {})
    for account in digital_footprint.get('active_accounts', []):
        html += f"""
            <div class="account-card">
                <h4>{account.get('platform', 'N/A')} - {account.get('username', 'N/A')}</h4>
                <p><strong>الرابط:</strong> <a href="{account.get('profile_url', '#')}" target="_blank">{account.get('profile_url', 'N/A')}</a></p>
                <div class="info-grid">
                    <div class="info-card">
                        <strong>آخر نشاط:</strong> {account.get('last_activity', 'مطلوب تحقق')}
                    </div>
                    <div class="info-card">
                        <strong>تاريخ الإنشاء:</strong> {account.get('account_creation_date', 'مطلوب تحقق')}
                    </div>
                    <div class="info-card">
                        <strong>حالة التحقق:</strong> <span class="badge badge-info">{account.get('verification_status', 'غير محقق')}</span>
                    </div>
                    <div class="info-card">
                        <strong>المتابعون:</strong> {account.get('follower_count', 'مطلوب تحقق')}
                    </div>
                    <div class="info-card">
                        <strong>المتابَعون:</strong> {account.get('following_count', 'مطلوب تحقق')}
                    </div>
"""
        if account.get('user_id'):
            html += f"""
                    <div class="info-card">
                        <strong>معرف المستخدم:</strong> {account.get('user_id')}
                    </div>
"""
        html += """
                </div>
            </div>
"""
    
    html += """
        </div>

        <div class="section">
            <h2>📞 معلومات الاتصال</h2>
"""
    
    personal_info = findings.get('personal_information', {})
    contact_info = personal_info.get('contact_information', {})
    
    html += f"""
            <div class="info-grid">
                <div class="info-card">
                    <strong>الاسم الكامل:</strong> {personal_info.get('biographical_data', {}).get('full_name', 'N/A')}
                </div>
                <div class="info-card">
                    <strong>الاسم بالإنجليزية:</strong> {personal_info.get('biographical_data', {}).get('full_name_english', 'N/A')}
                </div>
                <div class="info-card">
                    <strong>الموقع الحالي:</strong> {personal_info.get('biographical_data', {}).get('current_residence', 'N/A')}
                </div>
            </div>
            <h3>أرقام الهواتف</h3>
"""
    
    for phone in contact_info.get('phone_numbers', []):
        html += f"""
            <div class="info-card">
                <strong>الرقم:</strong> {phone.get('number', 'N/A')}<br>
                <strong>البلد:</strong> {phone.get('country', 'N/A')}<br>
                <strong>المشغل:</strong> {phone.get('operator', 'مطلوب تحديد')}<br>
                <strong>حالة التحقق:</strong> <span class="badge badge-success">{phone.get('verification_status', 'N/A')}</span>
            </div>
"""
    
    html += """
        </div>

        <div class="section">
            <h2>🔒 مخاوف الأمان</h2>
"""
    
    security = findings.get('security_concerns', {})
    html += f"""
            <h3>المعلومات المكشوفة</h3>
            <ul>
"""
    for info in security.get('exposed_information', []):
        html += f"<li>{info}</li>\n"
    
    html += f"""
            </ul>
            <h3>نقاط الضعف المحتملة</h3>
            <ul>
"""
    for vuln in security.get('potential_vulnerabilities', []):
        html += f"<li>{vuln}</li>\n"
    
    html += """
            </ul>
        </div>

        <div class="section">
            <h2>📊 التحليل والتقييم</h2>
"""
    
    analysis = report.get('analysis_and_assessment', {})
    threat = analysis.get('threat_level_evaluation', {})
    
    html += f"""
            <h3>مستوى التهديد الحالي</h3>
            <p><span class="badge badge-warning">{threat.get('current_threat_level', 'N/A')}</span></p>
            <h3>عوامل المخاطر</h3>
            <ul>
"""
    for factor in threat.get('risk_factors', []):
        html += f"<li>{factor}</li>\n"
    
    html += """
            </ul>
            <h3>توصيات التخفيف</h3>
            <ul>
"""
    for rec in threat.get('mitigation_recommendations', []):
        html += f"<li>{rec}</li>\n"
    
    html += """
            </ul>
        </div>

        <div class="footer">
            <p><strong>تصنيف:</strong> {metadata.get('classification_level', 'سري')}</p>
            <p>هذا التقرير سري ومخصص للمخولين فقط</p>
            <p>تاريخ التوزيع: {metadata.get('date_created', 'N/A')}</p>
            <p style="margin-top: 20px; font-size: 0.8em; color: #999;">
                تم إنشاء هذا التقرير باستخدام أدوات OSINT - للأغراض القانونية والأخلاقية فقط
            </p>
        </div>
    </div>
</body>
</html>
"""
    
    return html

def main():
    """Main function"""
    filename = "osint_professional_report_2025-11-07.json"
    report_data = load_report(filename)
    html = generate_html(report_data)
    
    output_filename = "osint_professional_report_2025-11-07.html"
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ تم إنشاء التقرير HTML: {output_filename}")

if __name__ == "__main__":
    main()
