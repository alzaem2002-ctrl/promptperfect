#!/usr/bin/env python3
"""
OSINT Account Researcher - Simulated Account Information Gathering
Cyber Security Expert Edition
Note: This simulates realistic OSINT research patterns
"""

import json
import re
from datetime import datetime, timedelta
import random

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

class AccountResearcher:
    """Simulate realistic account research"""
    
    def __init__(self, search_params):
        self.search_params = search_params
        self.research_results = {}
    
    def analyze_username_meaning(self, username):
        """Analyze username for potential meaning"""
        analysis = {
            "possible_meanings": [],
            "language_patterns": [],
            "character_analysis": {}
        }
        
        # Check for Arabic name patterns
        if "tofah" in username.lower():
            analysis["possible_meanings"].append("Tofah (تفاح) - Apple in Arabic")
            analysis["language_patterns"].append("Arabic/English mix")
        
        if "lemoonah" in username.lower():
            analysis["possible_meanings"].append("Lemoonah (ليمونة) - Lemon in Arabic")
            analysis["language_patterns"].append("Arabic/English mix")
        
        # Underscore pattern analysis
        underscore_count = username.count('_')
        if underscore_count >= 2:
            analysis["character_analysis"]["underscore_pattern"] = "Double underscore - common in Arabic usernames"
            analysis["character_analysis"]["style"] = "Arabic naming convention"
        
        return analysis
    
    def simulate_instagram_research(self, username):
        """Simulate Instagram account research"""
        if not username:
            return {}
        
        # Realistic analysis based on username pattern
        research = {
            "username": username,
            "profile_url": f"https://instagram.com/{username}",
            "account_analysis": {
                "username_meaning": self.analyze_username_meaning(username),
                "account_type": "Personal",
                "likely_private": "Unknown - requires manual check",
                "naming_pattern": "Arabic/English mix with underscores"
            },
            "potential_connections": {
                "name_variations": [
                    "Tofah",
                    "Tofa",
                    "Tofah_",
                    "__tofah"
                ],
                "related_searches": [
                    f"{username} instagram",
                    f"tofah instagram",
                    f"طرفة instagram"
                ]
            },
            "research_notes": [
                "Username uses double underscore pattern (__) - common in Arabic usernames",
                "Name 'tofah' suggests Arabic origin",
                "Account likely created for personal use",
                "May be connected to TikTok account _lemoonah_ through naming pattern"
            ]
        }
        
        return research
    
    def simulate_tiktok_research(self, username, user_id):
        """Simulate TikTok account research"""
        if not username:
            return {}
        
        research = {
            "username": username,
            "user_id": user_id,
            "profile_url": f"https://tiktok.com/@{username}",
            "account_analysis": {
                "username_meaning": self.analyze_username_meaning(username),
                "user_id_valid": True if user_id else False,
                "account_type": "Personal",
                "naming_pattern": "Arabic/English mix with underscores"
            },
            "potential_connections": {
                "name_variations": [
                    "Lemoonah",
                    "Lemonah",
                    "_lemoonah",
                    "lemoonah_"
                ],
                "related_searches": [
                    f"{username} tiktok",
                    f"lemoonah tiktok",
                    f"طرفة tiktok"
                ]
            },
            "research_notes": [
                f"User ID {user_id} indicates registered TikTok account",
                "Username 'lemoonah' suggests Arabic origin (lemon)",
                "Similar naming pattern to Instagram account (underscores)",
                "May be same person as Instagram account based on pattern"
            ]
        }
        
        return research
    
    def find_related_accounts(self):
        """Find potentially related accounts based on patterns"""
        related = {
            "similar_usernames": [],
            "name_based_searches": [],
            "pattern_based_searches": []
        }
        
        primary_name = self.search_params.get("name", "")
        insta_user = self.search_params.get("instagram_username", "")
        tiktok_user = self.search_params.get("tiktok_username", "")
        
        # Extract name parts for searching
        if primary_name:
            name_parts = primary_name.split()
            if len(name_parts) >= 2:
                first_name = name_parts[0]  # طرفة
                last_name = name_parts[-1]  # الجبالي
                
                related["name_based_searches"].extend([
                    f"{first_name} {last_name}",
                    f"{first_name}_{last_name}",
                    f"_{first_name}_",
                    f"{last_name}_{first_name}"
                ])
        
        # Pattern-based searches
        if insta_user:
            # Remove underscores for variations
            base_name = insta_user.replace('_', '')
            related["pattern_based_searches"].extend([
                base_name,
                f"_{base_name}",
                f"{base_name}_",
                f"__{base_name}__"
            ])
        
        if tiktok_user:
            base_name = tiktok_user.replace('_', '')
            related["pattern_based_searches"].extend([
                base_name,
                f"_{base_name}",
                f"{base_name}_"
            ])
        
        return related
    
    def analyze_cross_platform_consistency(self):
        """Analyze consistency across platforms"""
        analysis = {
            "naming_consistency": {},
            "pattern_similarity": {},
            "likely_same_person": False,
            "confidence_score": 0.0
        }
        
        insta_user = self.search_params.get("instagram_username", "")
        tiktok_user = self.search_params.get("tiktok_username", "")
        
        if insta_user and tiktok_user:
            # Both use underscores
            if '_' in insta_user and '_' in tiktok_user:
                analysis["naming_consistency"]["underscore_usage"] = "Consistent"
                analysis["pattern_similarity"]["score"] = 0.8
            
            # Both start/end with underscores
            if insta_user.startswith('_') and tiktok_user.startswith('_'):
                analysis["naming_consistency"]["prefix_pattern"] = "Consistent"
                analysis["pattern_similarity"]["score"] += 0.1
            
            # Similar length
            length_diff = abs(len(insta_user) - len(tiktok_user))
            if length_diff <= 2:
                analysis["naming_consistency"]["length_similarity"] = "Similar"
                analysis["pattern_similarity"]["score"] += 0.1
            
            # Overall assessment
            if analysis["pattern_similarity"]["score"] >= 0.8:
                analysis["likely_same_person"] = True
                analysis["confidence_score"] = 0.85
        
        return analysis
    
    def generate_research_report(self):
        """Generate comprehensive research report"""
        report = {
            "research_metadata": {
                "research_date": datetime.now().isoformat(),
                "research_type": "Account Information Gathering",
                "methodology": "Pattern Analysis & Cross-Platform Research",
                "researcher": "Cyber Security Expert"
            },
            "target_accounts": {},
            "account_research": {},
            "related_accounts": {},
            "cross_platform_analysis": {},
            "findings": {
                "confirmed_information": [],
                "high_probability_findings": [],
                "recommended_searches": []
            }
        }
        
        # Instagram Research
        insta_user = self.search_params.get("instagram_username", "")
        if insta_user:
            report["account_research"]["instagram"] = self.simulate_instagram_research(insta_user)
            report["target_accounts"]["instagram"] = {
                "username": insta_user,
                "url": f"https://instagram.com/{insta_user}",
                "research_status": "analyzed"
            }
        
        # TikTok Research
        tiktok_user = self.search_params.get("tiktok_username", "")
        tiktok_id = self.search_params.get("tiktok_user_id", "")
        if tiktok_user:
            report["account_research"]["tiktok"] = self.simulate_tiktok_research(tiktok_user, tiktok_id)
            report["target_accounts"]["tiktok"] = {
                "username": tiktok_user,
                "user_id": tiktok_id,
                "url": f"https://tiktok.com/@{tiktok_user}",
                "research_status": "analyzed"
            }
        
        # Related Accounts
        report["related_accounts"] = self.find_related_accounts()
        
        # Cross-Platform Analysis
        report["cross_platform_analysis"] = self.analyze_cross_platform_consistency()
        
        # Findings
        if report["cross_platform_analysis"].get("likely_same_person"):
            report["findings"]["high_probability_findings"].append({
                "finding": "Instagram و TikTok حسابات لنفس الشخص",
                "confidence": report["cross_platform_analysis"].get("confidence_score", 0),
                "evidence": [
                    "نمط أسماء المستخدمين متسق",
                    "استخدام الشرطة السفلية متسق",
                    "أسماء مشابهة (tofah/lemoonah)"
                ]
            })
        
        # Recommended searches
        report["findings"]["recommended_searches"].extend([
            "البحث عن 'طرفة الجبالي' على Google",
            "البحث عن '__tofah__' على منصات أخرى",
            "البحث عن '_lemoonah_' على منصات أخرى",
            "البحث عن رقم الهاتف على TrueCaller",
            "البحث عن الاسم الكامل على LinkedIn",
            "البحث عن الاسم على Facebook",
            "البحث عن الاسم على Twitter/X"
        ])
        
        return report

def main():
    """Main function"""
    print("╔════════════════════════════════════════════════════╗")
    print("║  OSINT Account Researcher v1.0                     ║")
    print("║  Cyber Security Expert Edition                     ║")
    print("╚════════════════════════════════════════════════════╝")
    print()
    print("🔍 جاري البحث عن معلومات الحسابات...")
    print()
    
    researcher = AccountResearcher(SEARCH_PARAMS)
    report = researcher.generate_research_report()
    
    # Save report
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"account_research_report_{timestamp}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("✅ تم إنشاء تقرير البحث عن الحسابات")
    print(f"📄 الملف: {filename}")
    print()
    print("📊 ملخص البحث:")
    print(f"   - حسابات تم تحليلها: {len(report['target_accounts'])}")
    print(f"   - حسابات مرتبطة محتملة: {len(report['related_accounts'].get('name_based_searches', []))}")
    
    if report["cross_platform_analysis"].get("likely_same_person"):
        print(f"   - احتمال أن تكون نفس الشخص: {report['cross_platform_analysis'].get('confidence_score', 0):.0%}")
    
    print()
    print("📋 معلومات الحسابات:")
    
    if report.get("account_research", {}).get("instagram"):
        insta = report["account_research"]["instagram"]
        print(f"\n📷 Instagram: {insta['username']}")
        print(f"   الرابط: {insta['profile_url']}")
        if insta.get("account_analysis", {}).get("username_meaning", {}).get("possible_meanings"):
            print(f"   المعنى المحتمل: {', '.join(insta['account_analysis']['username_meaning']['possible_meanings'])}")
    
    if report.get("account_research", {}).get("tiktok"):
        tiktok = report["account_research"]["tiktok"]
        print(f"\n🎵 TikTok: {tiktok['username']}")
        print(f"   الرابط: {tiktok['profile_url']}")
        print(f"   معرف المستخدم: {tiktok.get('user_id', 'N/A')}")
        if tiktok.get("account_analysis", {}).get("username_meaning", {}).get("possible_meanings"):
            print(f"   المعنى المحتمل: {', '.join(tiktok['account_analysis']['username_meaning']['possible_meanings'])}")
    
    print()
    print("⚠️  ملاحظة: هذا تحليل منطقي بناءً على الأنماط")
    print("   يتطلب فحص يدوي للتأكد من المعلومات")

if __name__ == "__main__":
    main()
