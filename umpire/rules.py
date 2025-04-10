ATTACK_CHAIN_RULES = {
    "Brute Force Attack": ["Compromised Account"],
    "Compromised Account": ["Business Email Compromise", "Internal Phishing Attack", "Lateral Movement"],
    "Business Email Compromise": ["Payment Diversion Fraud"],
    "Internal Phishing Attack": ["Credential Theft", "Malware"],
    "Malware": ["Compromised PC", "Remote Access Trojan"],
    "Compromised PC": ["Lateral Movement", "Data Exfiltration (PC)"],
    "Compromised Server": ["Lateral Movement", "Data Exfiltration (Database)", "Data Exfiltration (Server)"],
    "Lateral Movement": ["Privilege Escalation", "Compromised PC", "Compromised Server"],
    "Privilege Escalation": ["Domain Dominance"],
    "Intruder (HQ)": ["Zero Day Attack"],
    "Intruder (Production)": ["Zero Day Attack", "IoT Vulnerability"],
    "IoT Vulnerability": ["IoT Disruption"],
    "IoT Disruption": ["IoT Destruction"],
    "Email Reconnaissance": ["Spear Phishing"],
    "Spear Phishing": ["Compromised Account"],
    "Infected USB": ["Malware"],
    "Phishing Attack": ["Malware"],
    "Port Scanning": ["Database Vulnerability"],
    "Database Vulnerability": ["Lateral Movement"],
    "Simple Web Server Hack": ["Defaced Web Site"],
    "Defaced Web Site": ["Reputational Damage"],
    "Targeted Scanning": ["IoT Vulnerability"],
    "Unsecured Wireless Network": ["Compromised PC"],
    "Remote Access Trojan": ["Lateral Movement"],
    "Privilege Escalation": ["Domain Dominance"],
    "Zero Day Attack": ["Lateral Movement"],
    # Add any remaining transitions...
}

DEFENSE_EFFECTIVENESS = {
    "Brute Force Attack": {
        "blocked_by": ["Complex Passwords"],
        "detected_by": ["Multi-factor Authentication", "Threat Analytics"],
        "symptom": None
    },
    "Business Email Compromise": {
        "blocked_by": ["Advanced Security Training"],
        "detected_by": [],
        "symptom": None
    },
    "Compromised Account": {
        "blocked_by": ["Identity Protection"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Compromised PC": {
        "blocked_by": ["Data Loss Prevention"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Compromised Server": {
        "blocked_by": [],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Credential Theft": {
        "blocked_by": ["Multi-factor Authentication"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Database Vulnerability": {
        "blocked_by": ["Database Software Patching"],
        "detected_by": ["Penetration Test"],
        "symptom": None
    },
    "DDOS Attack": {
        "blocked_by": ["Firewall (HQ)", "Firewall (Production)"],
        "detected_by": [],
        "symptom": "Services run slowly; users can't access the website"
    },
    "Defaced Web Site": {
        "blocked_by": [],
        "detected_by": [],
        "symptom": "Adverse publicity due to defamatory content"
    },
    "Email Reconnaissance": {
        "blocked_by": [],
        "detected_by": ["Advanced Security Training"],
        "symptom": None
    },
    "Infected USB": {
        "blocked_by": ["Security Awareness Training"],
        "detected_by": [],
        "symptom": None
    },
    "Internal Phishing Attack": {
        "blocked_by": ["Advanced Security Training"],
        "detected_by": ["Security Awareness Training"],
        "symptom": "Users may report (not 100%)"
    },
    "Intruder (HQ)": {
        "blocked_by": [],
        "detected_by": ["CCTV (HQ)"],
        "symptom": None
    },
    "Intruder (Production)": {
        "blocked_by": [],
        "detected_by": ["CCTV (Production)"],
        "symptom": None
    },
    "IoT Disruption": {
        "blocked_by": ["IoT Controller Upgrade"],
        "detected_by": [],
        "symptom": "Performance downgrade"
    },
    "IoT Vulnerability": {
        "blocked_by": [],
        "detected_by": ["Penetration Test"],
        "symptom": None
    },
    "Lateral Movement": {
        "blocked_by": [],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Lost or Stolen PC": {
        "blocked_by": ["Hard Drive Encryption"],
        "detected_by": [],
        "symptom": "User reports"
    },
    "Malware": {
        "blocked_by": ["Anti-virus"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Phishing Attack": {
        "blocked_by": ["Security Awareness Training"],
        "detected_by": [],
        "symptom": None
    },
    "Port Scanning": {
        "blocked_by": ["Firewall (HQ)"],
        "detected_by": [],
        "symptom": None
    },
    "Privilege Escalation": {
        "blocked_by": ["Role-Based Access Control"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Remote Access Trojan": {
        "blocked_by": ["Anti-malware"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Simple Web Server Hack": {
        "blocked_by": ["Server Operating System Patching"],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Spamming Attack": {
        "blocked_by": ["Spam Filters"],
        "detected_by": [],
        "symptom": "Inboxes full of spam"
    },
    "Spear Phishing": {
        "blocked_by": ["Phishing Simulation"],
        "detected_by": [],
        "symptom": None
    },
    "Targeted Scanning": {
        "blocked_by": ["Firewall (Production)"],
        "detected_by": [],
        "symptom": "Firewall logs show scanning activity"
    },
    "Unsecured Wireless Network": {
        "blocked_by": ["Penetration Test"],
        "detected_by": ["Penetration Test"],
        "symptom": None
    },
    "Zero Day Attack": {
        "blocked_by": [],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "Data Exfiltration (Database)": {
        "blocked_by": ["Database Software Patching"],
        "detected_by": ["Network Monitoring"],
        "symptom": None
    },
    "Data Exfiltration (PC)": {
        "blocked_by": [],
        "detected_by": ["Network Monitoring"],
        "symptom": None
    },
    "Data Exfiltration (Server)": {
        "blocked_by": [],
        "detected_by": ["Network Monitoring"],
        "symptom": None
    },
    "Domain Dominance": {
        "blocked_by": [],
        "detected_by": ["Threat Analytics"],
        "symptom": None
    },
    "IoT Destruction": {
        "blocked_by": [],
        "detected_by": [],
        "symptom": "IoT network destroyed"
    },
    "Payment Diversion Fraud": {
        "blocked_by": ["Advanced Security Training"],
        "detected_by": [],
        "symptom": "Monthly cash reconciliation detects a loss"
    },
    "Reputational Damage": {
        "blocked_by": [],
        "detected_by": [],
        "symptom": "Drop in sales, falling share prices"
    },
}
