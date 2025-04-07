from django.db import migrations

def seed_cards(apps, schema_editor):
    AttackCard = apps.get_model('game', 'AttackCard')
    DefenseCard = apps.get_model('game', 'DefenseCard')

    attack_cards = [
        # (name, description, type)
        ("Brute Force Attack", "Password cracking to access an account", "YELLOW"),
        ("Email Reconnaissance", "Probing emails for valid addresses", "YELLOW"),
        ("Phishing Attack", "Tricks users into giving credentials", "YELLOW"),
        ("Infected USB", "Malware-laden USB dropped in parking lot", "YELLOW"),
        ("Intruder (HQ)", "Physical access to HQ network", "YELLOW"),
        ("Intruder (Production)", "Access to production IoT devices", "YELLOW"),
        ("Lost or Stolen PC", "Physical loss of a laptop or PC", "YELLOW"),
        ("Port Scanning", "Scanning for open/vulnerable services", "YELLOW"),
        ("Simple Web Server Hack", "Exploits a known server vuln", "YELLOW"),
        ("Spamming Attack", "Flooding email system", "YELLOW"),
        ("Targeted Scanning", "Scans that identify specific targets", "YELLOW"),
        ("Unsecured Wireless Network", "Open Wi-Fi used for entry", "YELLOW"),

        ("Compromised Account", "Gained control of a user account", "RED"),
        ("Compromised PC", "Remote control of a PC", "RED"),
        ("Compromised Server", "Server takeover", "RED"),
        ("Business Email Compromise", "Fake CEO email for fraudulent payments", "RED"),
        ("Internal Phishing Attack", "Spearphishing from inside network", "RED"),
        ("Malware", "Email malware delivery", "RED"),
        ("IoT Vulnerability", "Exploit to gain IoT access", "RED"),
        ("IoT Disruption", "IoT firmware update causes issues", "RED"),
        ("Zero Day Attack", "Exploits an unknown vuln", "RED"),
        ("Privilege Escalation", "Gains admin access from user access", "RED"),
        ("Lateral Movement", "Moves from one machine to others", "RED"),
        ("Remote Access Trojan", "Hidden backdoor to remote access", "RED"),
        ("Spear Phishing", "Highly targeted phishing", "RED"),
        ("Database Vulnerability", "Exploit DB system to gain access", "RED"),

        ("Credential Theft", "Tricked user gives up password", "BLACK"),
        ("Data Exfiltration (Database)", "Database data stolen", "BLACK"),
        ("Data Exfiltration (PC)", "PC data stolen", "BLACK"),
        ("Data Exfiltration (Server)", "Server data stolen", "BLACK"),
        ("IoT Destruction", "Permanent damage to IoT systems", "BLACK"),
        ("Payment Diversion Fraud", "Tricks staff into sending money", "BLACK"),
        ("Domain Dominance (Persistence)", "Maintains long-term control", "BLACK"),
        ("Reputational Damage", "Site defaced; public embarrassment", "BLACK"),
    ]

    for name, desc, ctype in attack_cards:
        AttackCard.objects.create(name=name, description=desc, card_type=ctype)

    defense_cards = [
        # (name, description, cost, requires_sp)
        ("Advanced Security Training", "Trains staff in spotting threats", 30, False),
        ("Anti-malware", "Detects and removes malware", 30, False),
        ("Antivirus", "Detects and removes viruses", 25, False),
        ("CCTV (HQ)", "Surveillance at HQ", 40, False),
        ("CCTV (Production)", "Surveillance at production site", 40, False),
        ("Complex Passwords", "Enforce strong passwords", 10, False),
        ("Data Loss Prevention", "Controls outbound info flow", 20, True),
        ("Database Software Patching", "Keeps DBMS up to date", 50, False),
        ("Firewall (HQ)", "Blocks unauthorized network access", 25, False),
        ("Firewall (Production)", "Same for production site", 25, False),
        ("Hard Drive Encryption", "Protects sensitive data", 25, False),
        ("Identity Protection", "Detects leaked credentials", 30, True),
        ("IoT Controller Upgrade", "Secure firmware updates", 25, False),
        ("Multi-factor Authentication", "Requires code/token to log in", 20, True),
        ("Network Monitoring", "Tracks activity across network", 40, False),
        ("PC OS Patching", "Keeps PCs up to date", 25, False),
        ("Penetration Test", "Red team assessment", 30, False),
        ("Phishing Simulation", "Trains users on phishing", 30, False),
        ("Role-Based Access Control", "Limits access by job role", 20, True),
        ("Security Awareness Training", "Basic security training", 25, False),
        ("Security Platform", "Required for SP cards", 50, False),
        ("Server OS Patching", "Keeps servers up to date", 25, False),
        ("Spam Filters", "Blocks junk email", 10, False),
        ("Threat Analytics", "Behavior-based alerts", 50, True),
    ]

    for name, desc, cost, sp in defense_cards:
        DefenseCard.objects.create(name=name, description=desc, cost=cost, requires_sp=sp)

def unseed_cards(apps, schema_editor):
    AttackCard = apps.get_model('game', 'AttackCard')
    DefenseCard = apps.get_model('game', 'DefenseCard')
    AttackCard.objects.all().delete()
    DefenseCard.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ("game", "0001_initial"),  # Replace with the latest migration filename
    ]

    operations = [
        migrations.RunPython(seed_cards, unseed_cards),
    ]
