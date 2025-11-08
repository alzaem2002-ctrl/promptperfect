#!/usr/bin/env python3
"""
Helper script to add accounts, messages, and images to OSINT report
"""

import json
import sys
from datetime import datetime

def load_latest_report():
    """Load the latest OSINT report"""
    import glob
    reports = glob.glob("osint_report_*.json")
    if not reports:
        print("❌ No report files found!")
        return None
    
    latest = max(reports)
    print(f"📄 Loading: {latest}")
    with open(latest, 'r', encoding='utf-8') as f:
        return json.load(f), latest

def add_account(report, platform, username, url, profile_info=None):
    """Add a found account to the report"""
    account = {
        "platform": platform,
        "username": username,
        "url": url,
        "status": "found",
        "profile_info": profile_info or {}
    }
    report["found_accounts"].append(account)
    print(f"✅ Added account: {platform} - {username}")

def add_message(report, date, platform, content, sender, attachments=None):
    """Add a message to the report"""
    message = {
        "date": date,
        "platform": platform,
        "content": content,
        "sender": sender,
        "attachments": attachments or []
    }
    report["messages"].append(message)
    print(f"✅ Added message from {sender} on {platform}")

def add_connected_account(report, platform, username, url, connection_type, profile_info=None, notes=None):
    """Add a connected/related account to the report"""
    account = {
        "platform": platform,
        "username": username,
        "url": url,
        "connection_type": connection_type,
        "status": "found",
        "profile_info": profile_info or {},
        "notes": notes or ""
    }
    report["connected_accounts"].append(account)
    print(f"✅ Added connected account: {platform} - {username} ({connection_type})")

def add_image(report, url, description, source):
    """Add an image to the report"""
    image = {
        "url": url,
        "description": description,
        "source": source
    }
    report["available_images"].append(image)
    print(f"✅ Added image: {description} from {source}")

def save_report(report, filename):
    """Save updated report"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"💾 Report saved: {filename}")

def main():
    """Example usage"""
    report, filename = load_latest_report()
    if not report:
        return
    
    print("\n📝 Adding sample data...\n")
    
    # Example: Add Instagram account details
    instagram_account = next((acc for acc in report["found_accounts"] if acc["platform"] == "Instagram"), None)
    if instagram_account:
        instagram_account["profile_info"] = {
            "display_name": "Tofah",
            "bio": "Example bio text",
            "followers": "1,234",
            "following": "567",
            "posts": "89"
        }
        print("✅ Updated Instagram account info")
    
    # Example: Add TikTok account details
    tiktok_account = next((acc for acc in report["found_accounts"] if acc["platform"] == "TikTok"), None)
    if tiktok_account:
        tiktok_account["profile_info"] = {
            "display_name": "Lemoonah",
            "bio": "Example TikTok bio",
            "followers": "5,678",
            "following": "123",
            "likes": "12.3K"
        }
        print("✅ Updated TikTok account info")
    
    # Example: Add a message
    add_message(
        report,
        date=datetime.now().strftime("%Y-%m-%d"),
        platform="Instagram",
        content="Example message content",
        sender="__tofah__"
    )
    
    # Example: Add a connected account (mutual follower, similar username, etc.)
    add_connected_account(
        report,
        platform="Twitter",
        username="example_user",
        url="https://twitter.com/example_user",
        connection_type="Mutual Follower",
        profile_info={"display_name": "Example User", "followers": "1K"},
        notes="Found through mutual followers analysis on Instagram"
    )
    
    # Example: Add an image
    add_image(
        report,
        url="https://example.com/image.jpg",
        description="Profile Picture",
        source="Instagram"
    )
    
    # Save updated report
    save_report(report, filename)
    
    print("\n✅ Done! Run osint_tool.py to regenerate HTML report with new data.")

if __name__ == "__main__":
    main()
