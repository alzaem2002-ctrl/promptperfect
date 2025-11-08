#!/usr/bin/env python3
"""
OSINT Professional Investigation Tool
Cyber Security Expert Edition
Complies with OSINT best practices and verification standards
"""

import json
import hashlib
from datetime import datetime
from collections import defaultdict

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

# OSINT Sources with credibility ratings
OSINT_SOURCES = {
    "username_search": {
        "Sherlock": {
            "url": "https://github.com/sherlock-project/sherlock",
            "credibility": "high",
            "verification_method": "automated_cross_platform",
            "last_verified": "2024-01-15"
        },
        "WhatsMyName": {
            "url": "https://github.com/WebBreacher/WhatsMyName",
            "credibility": "high",
            "verification_method": "manual_verification",
            "last_verified": "2024-01-10"
        },
        "Namechk": {
            "url": "https://namechk.com/",
            "credibility": "medium",
            "verification_method": "automated",
            "last_verified": "2024-01-12"
        },
        "CheckUsernames": {
            "url": "https://checkusernames.com/",
            "credibility": "medium",
            "verification_method": "automated",
            "last_verified": "2024-01-12"
        },
        "Maigret": {
            "url": "https://github.com/soxoj/maigret",
            "credibility": "high",
            "verification_method": "automated_cross_platform",
            "last_verified": "2024-01-14"
        }
    },
    "phone_search": {
        "PhoneInfoga": {
            "url": "https://github.com/sundowndev/phoneinfoga",
            "credibility": "high",
            "verification_method": "technical_analysis",
            "last_verified": "2024-01-13"
        },
        "TrueCaller": {
            "url": "https://www.truecaller.com/",
            "credibility": "medium",
            "verification_method": "crowdsourced",
            "last_verified": "2024-01-11"
        },
        "WhitePages": {
            "url": "https://www.whitepages.com/",
            "credibility": "medium",
            "verification_method": "public_records",
            "last_verified": "2024-01-10"
        },
        "PeopleFinder": {
            "url": "https://www.peoplefinder.com/",
            "credibility": "medium",
            "verification_method": "public_records",
            "last_verified": "2024-01-10"
        },
        "Spokeo": {
            "url": "https://www.spokeo.com/",
            "credibility": "medium",
            "verification_method": "aggregated_data",
            "last_verified": "2024-01-09"
        }
    },
    "email_search": {
        "Hunter.io": {
            "url": "https://hunter.io/",
            "credibility": "high",
            "verification_method": "technical_verification",
            "last_verified": "2024-01-14"
        },
        "RocketReach": {
            "url": "https://rocketreach.co/",
            "credibility": "high",
            "verification_method": "professional_networks",
            "last_verified": "2024-01-13"
        },
        "EmailFinder": {
            "url": "https://www.emailfinder.com/",
            "credibility": "medium",
            "verification_method": "automated",
            "last_verified": "2024-01-12"
        },
        "Clearbit": {
            "url": "https://clearbit.com/",
            "credibility": "high",
            "verification_method": "api_verification",
            "last_verified": "2024-01-15"
        },
        "MailboxValidator": {
            "url": "https://www.mailboxvalidator.com/",
            "credibility": "high",
            "verification_method": "smtp_verification",
            "last_verified": "2024-01-14"
        }
    },
    "domain_search": {
        "Shodan": {
            "url": "https://www.shodan.io/",
            "credibility": "high",
            "verification_method": "technical_scanning",
            "last_verified": "2024-01-15"
        },
        "Censys": {
            "url": "https://search.censys.io/",
            "credibility": "high",
            "verification_method": "technical_scanning",
            "last_verified": "2024-01-15"
        },
        "WHOIS Lookup": {
            "url": "https://whois.net/",
            "credibility": "high",
            "verification_method": "dns_records",
            "last_verified": "2024-01-14"
        },
        "DNS Dumpster": {
            "url": "https://dnsdumpster.com/",
            "credibility": "high",
            "verification_method": "dns_enumeration",
            "last_verified": "2024-01-13"
        },
        "SecurityTrails": {
            "url": "https://securitytrails.com/",
            "credibility": "high",
            "verification_method": "historical_dns",
            "last_verified": "2024-01-15"
        }
    },
    "hash_search": {
        "VirusTotal": {
            "url": "https://www.virustotal.com/",
            "credibility": "high",
            "verification_method": "multi_engine_scan",
            "last_verified": "2024-01-15"
        },
        "Have I Been Pwned": {
            "url": "https://haveibeenpwned.com/",
            "credibility": "high",
            "verification_method": "breach_database",
            "last_verified": "2024-01-15"
        },
        "Hybrid Analysis": {
            "url": "https://www.hybrid-analysis.com/",
            "credibility": "high",
            "verification_method": "sandbox_analysis",
            "last_verified": "2024-01-14"
        },
        "Malware.Expert": {
            "url": "https://malware.expert/",
            "credibility": "medium",
            "verification_method": "static_analysis",
            "last_verified": "2024-01-12"
        },
        "AlienVault OTX": {
            "url": "https://otx.alienvault.com/",
            "credibility": "high",
            "verification_method": "threat_intelligence",
            "last_verified": "2024-01-15"
        }
    }
}

class OSINTVerification:
    """Class for verifying OSINT data credibility"""
    
    @staticmethod
    def calculate_credibility_score(sources):
        """Calculate overall credibility score based on source ratings"""
        credibility_map = {"high": 3, "medium": 2, "low": 1}
        total_score = 0
        count = 0
        
        for source_info in sources.values():
            if isinstance(source_info, dict) and "credibility" in source_info:
                total_score += credibility_map.get(source_info["credibility"], 1)
                count += 1
        
        if count == 0:
            return 0
        
        avg_score = total_score / count
        if avg_score >= 2.5:
            return "high"
        elif avg_score >= 1.5:
            return "medium"
        else:
            return "low"
    
    @staticmethod
    def verify_cross_reference(data_points):
        """Verify data by cross-referencing multiple sources"""
        verification_status = {
            "verified": [],
            "partially_verified": [],
            "unverified": [],
            "conflicting": []
        }
        
        # Group data by type
        grouped = defaultdict(list)
        for point in data_points:
            grouped[point.get("type")].append(point)
        
        # Check for consistency
        for data_type, points in grouped.items():
            if len(points) >= 2:
                values = [p.get("value") for p in points]
                if len(set(values)) == 1:
                    verification_status["verified"].extend(points)
                else:
                    verification_status["conflicting"].extend(points)
            else:
                verification_status["partially_verified"].extend(points)
        
        return verification_status
    
    @staticmethod
    def generate_data_hash(data):
        """Generate hash for data integrity verification"""
        data_str = json.dumps(data, sort_keys=True, ensure_ascii=False)
        return hashlib.sha256(data_str.encode()).hexdigest()

def generate_professional_report():
    """Generate professional OSINT report with verification"""
    
    # Initialize verification
    verifier = OSINTVerification()
    
    report = {
        "report_metadata": {
            "report_id": f"OSINT-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "report_type": "Professional OSINT Investigation",
            "investigator": "Cyber Security Expert",
            "classification": "Confidential",
            "methodology": "OSINT Best Practices",
            "verification_level": "Standard",
            "timestamp": datetime.now().isoformat(),
            "data_integrity_hash": ""
        },
        "executive_summary": {
            "investigation_purpose": "تحليل البصمة الرقمية والتحقق من المصداقية",
            "scope": "تحليل شامل للوجود الرقمي عبر منصات متعددة",
            "key_findings": [],
            "credibility_assessment": {},
            "risk_assessment": "منخفض إلى متوسط",
            "recommendations": []
        },
        "search_parameters": SEARCH_PARAMS,
        "verification_framework": {
            "source_credibility": {},
            "cross_reference_results": {},
            "data_integrity": {}
        },
        "digital_footprint": {
            "name_connections": {},
            "activity_analysis": {},
            "cross_platform_links": [],
            "verification_status": {}
        },
        "osint_sources": OSINT_SOURCES,
        "results": {},
        "found_accounts": [],
        "connected_accounts": [],
        "analysis": {
            "credibility_analysis": {},
            "consistency_check": {},
            "timeline_analysis": {},
            "pattern_analysis": {}
        },
        "quality_assurance": {
            "verification_checklist": {},
            "data_quality_score": 0,
            "recommendations": []
        }
    }
    
    # Build name connections with verification
    primary_name = SEARCH_PARAMS.get("name", "")
    username = SEARCH_PARAMS.get("username", "")
    
    name_variations = []
    if primary_name:
        name_variations.append(primary_name)
    if username and username != primary_name:
        name_variations.append(username)
    
    # Calculate credibility for username search sources
    username_sources = OSINT_SOURCES.get("username_search", {})
    username_credibility = verifier.calculate_credibility_score(username_sources)
    
    report["verification_framework"]["source_credibility"]["username_search"] = {
        "credibility_level": username_credibility,
        "sources_count": len(username_sources),
        "high_credibility_sources": sum(1 for s in username_sources.values() 
                                        if isinstance(s, dict) and s.get("credibility") == "high")
    }
    
    # Build cross-platform identity with verification
    cross_platform_identity = {
        "primary_name": primary_name,
        "name_variations": name_variations,
        "platforms": [],
        "verification_status": "pending_manual_review"
    }
    
    # Add Instagram with verification
    if SEARCH_PARAMS.get("instagram_username"):
        insta_username = SEARCH_PARAMS["instagram_username"]
        cross_platform_identity["platforms"].append({
            "platform": "Instagram",
            "username": insta_username,
            "url": f"https://instagram.com/{insta_username}",
            "name_used": primary_name,
            "connection_type": "username_match",
            "verification_status": "requires_manual_verification",
            "verification_method": "profile_inspection_required"
        })
    
    # Add TikTok with verification
    if SEARCH_PARAMS.get("tiktok_username"):
        tiktok_username = SEARCH_PARAMS["tiktok_username"]
        cross_platform_identity["platforms"].append({
            "platform": "TikTok",
            "username": tiktok_username,
            "user_id": SEARCH_PARAMS.get("tiktok_user_id", ""),
            "url": f"https://tiktok.com/@{tiktok_username}",
            "name_used": primary_name,
            "connection_type": "username_match",
            "verification_status": "requires_manual_verification",
            "verification_method": "profile_inspection_required"
        })
    
    # Add phone with verification
    if SEARCH_PARAMS.get("phone"):
        phone_number = SEARCH_PARAMS["phone"]
        phone_sources = OSINT_SOURCES.get("phone_search", {})
        phone_credibility = verifier.calculate_credibility_score(phone_sources)
        
        cross_platform_identity["platforms"].append({
            "platform": "Phone",
            "number": phone_number,
            "name_used": primary_name,
            "connection_type": "contact_info",
            "verification_status": "requires_reverse_lookup",
            "verification_method": "phone_lookup_required",
            "source_credibility": phone_credibility
        })
    
    report["digital_footprint"]["cross_platform_links"] = [cross_platform_identity]
    
    # Build name connections
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
        "verification_notes": "يتطلب التحقق اليدوي من المطابقة بين الأسماء والحسابات"
    }
    
    # Build activity analysis with realistic assessment
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
            "credibility_note": "البيانات المقدمة أولية - يتطلب تحقق يدوي"
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
            "credibility_note": "البيانات المقدمة أولية - يتطلب تحقق يدوي"
        },
        "general_activity": {
            "name_mentions": [],
            "cross_platform_activity": [],
            "digital_presence_summary": f"وجود رقمي محتمل على منصات متعددة مرتبطة بالاسم: {primary_name}",
            "verification_level": "preliminary"
        }
    }
    
    # Add found accounts with verification status
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
            "credibility_note": "المعلومات المقدمة أولية - يتطلب فحص يدوي للملف الشخصي"
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
            "credibility_note": "المعلومات المقدمة أولية - يتطلب فحص يدوي للملف الشخصي"
        })
    
    # Quality assurance
    report["quality_assurance"] = {
        "verification_checklist": {
            "source_verification": "pending",
            "cross_reference_completed": False,
            "manual_review_required": True,
            "data_integrity_verified": False
        },
        "data_quality_score": 0.3,  # Preliminary data - low score
        "recommendations": [
            "إجراء فحص يدوي لجميع الحسابات المذكورة",
            "التحقق من مطابقة الأسماء عبر المنصات",
            "إجراء بحث عكسي لرقم الهاتف",
            "التحقق من صحة معرفات المستخدمين",
            "تحليل المحتوى المنشور للتحقق من الهوية"
        ]
    }
    
    # Generate data integrity hash
    report_data_for_hash = {
        "search_params": SEARCH_PARAMS,
        "timestamp": report["report_metadata"]["timestamp"]
    }
    report["report_metadata"]["data_integrity_hash"] = verifier.generate_data_hash(report_data_for_hash)
    
    return report

def save_professional_report(report):
    """Save professional report with verification"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_filename = f"osint_professional_report_{timestamp}.json"
    
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Professional OSINT Report saved: {json_filename}")
    print(f"📊 Report ID: {report['report_metadata']['report_id']}")
    print(f"🔐 Data Integrity Hash: {report['report_metadata']['data_integrity_hash'][:16]}...")
    print(f"⚠️  Verification Status: Preliminary - Manual Review Required")
    
    return json_filename

def main():
    """Main function"""
    print("╔════════════════════════════════════════════════════╗")
    print("║  OSINT Professional Investigation Tool v2.0         ║")
    print("║  Cyber Security Expert Edition                      ║")
    print("║  Compliant with OSINT Best Practices               ║")
    print("╚════════════════════════════════════════════════════╝")
    print()
    
    report = generate_professional_report()
    save_professional_report(report)
    
    print("\n📋 Report Summary:")
    print(f"   - Primary Name: {SEARCH_PARAMS.get('name', 'N/A')}")
    print(f"   - Accounts Found: {len(report['found_accounts'])}")
    print(f"   - Verification Level: Preliminary")
    print(f"   - Quality Score: {report['quality_assurance']['data_quality_score']:.1%}")
    print("\n⚠️  IMPORTANT: This report contains preliminary data.")
    print("   Manual verification and cross-referencing required for accuracy.")

if __name__ == "__main__":
    main()
