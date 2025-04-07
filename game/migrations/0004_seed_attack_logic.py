from django.db import migrations

def seed_attack_logic(apps, schema_editor):
    AttackCard = apps.get_model('game', 'AttackCard')
    DefenseCard = apps.get_model('game', 'DefenseCard')
    Matchup = apps.get_model('game', 'AttackDefenseMatchup')

    # Chain Logic: map attack card -> list of cards that can follow it
    chains = {
        "Brute Force Attack": ["Compromised Account"],
        "Compromised Account": [
            "Business Email Compromise", "Internal Phishing Attack", "Lateral Movement"
        ],
        "Compromised PC": [
            "Lateral Movement", "Data Exfiltration (PC)"
        ],
        "Compromised Server": [
            "Lateral Movement", "Data Exfiltration (Database)", "Data Exfiltration (Server)"
        ],
        "Database Vulnerability": [
            "Lateral Movement"
        ],
        "DDOS Attack": ["Reputational Damage"],
        "Email Reconnaissance": ["Spear Phishing"],
        "Infected USB": ["Malware"],
        "Internal Phishing Attack": ["Credential Theft", "Malware"],
        "Intruder (HQ)": ["Zero Day Attack"],
        "Intruder (Production)": ["Zero Day Attack", "IoT Vulnerability"],
        "IoT Disruption": ["IoT Destruction"],
        "IoT Vulnerability": ["IoT Disruption"],
        "Lateral Movement": ["Privilege Escalation", "Compromised PC", "Compromised Server"],
        "Lost or Stolen PC": ["Compromised PC"],
        "Malware": ["Compromised PC"],
        "Phishing Attack": ["Malware"],
        "Port Scanning": ["Database Vulnerability"],
        "Privilege Escalation": ["Domain Dominance (Persistence)"],
        "Remote Access Trojan": ["Lateral Movement"],
        "Simple Web Server Hack": ["Reputational Damage"],
        "Spear Phishing": ["Compromised Account"],
        "Targeted Scanning": ["IoT Vulnerability"],
        "Unsecured Wireless Network": ["Compromised PC"],
        "Zero Day Attack": ["Lateral Movement"]
    }

    for source_name, target_names in chains.items():
        try:
            source = AttackCard.objects.get(name=source_name)
            for target_name in target_names:
                target = AttackCard.objects.get(name=target_name)
                source.follows.add(target)
        except AttackCard.DoesNotExist:
            continue

    # Defense Matchups: which defense counters which attacks
    counters = {
        "Antivirus": ["Malware"],
        "Anti-malware": ["Malware", "Remote Access Trojan"],
        "Spam Filters": ["Phishing Attack", "Spear Phishing", "Spamming Attack"],
        "Complex Passwords": ["Brute Force Attack"],
        "Firewall (HQ)": ["Port Scanning", "Simple Web Server Hack"],
        "Firewall (Production)": ["IoT Vulnerability"],
        "Hard Drive Encryption": ["Lost or Stolen PC"],
        "Multi-factor Authentication": ["Credential Theft"],
        "Security Awareness Training": ["Phishing Attack", "Spear Phishing"],
        "Advanced Security Training": ["Business Email Compromise", "Internal Phishing Attack"],
        "CCTV (HQ)": ["Intruder (HQ)"],
        "CCTV (Production)": ["Intruder (Production)"],
        "IoT Controller Upgrade": ["IoT Vulnerability"],
        "PC OS Patching": ["Zero Day Attack"],
        "Server OS Patching": ["Zero Day Attack"],
        "Database Software Patching": ["Database Vulnerability"],
        "Penetration Test": ["Unsecured Wireless Network", "Simple Web Server Hack"],
        "Network Monitoring": ["Lateral Movement", "Privilege Escalation"],
        "Role-Based Access Control": ["Privilege Escalation"],
        "Threat Analytics": ["Domain Dominance (Persistence)"],
        "Identity Protection": ["Credential Theft"],
        "Data Loss Prevention": ["Data Exfiltration (Database)", "Data Exfiltration (PC)", "Data Exfiltration (Server)"],
    }

    for defense_name, attack_names in counters.items():
        try:
            defense = DefenseCard.objects.get(name=defense_name)
            for attack_name in attack_names:
                try:
                    attack = AttackCard.objects.get(name=attack_name)
                    Matchup.objects.create(defense=defense, attack=attack)
                except AttackCard.DoesNotExist:
                    continue
        except DefenseCard.DoesNotExist:
            continue

class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_attackdefensematchup')  # Replace with the last actual migration file
    ]

    operations = [
        migrations.RunPython(seed_attack_logic),
    ]
