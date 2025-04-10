from django.core.management.base import BaseCommand
from umpire.models import Card

class Command(BaseCommand):
    help = "Loads all standard game cards into the database"

    def handle(self, *args, **kwargs):
        cards = [
            # Yellow (Initial Attacks)
            ("Brute Force Attack", "red", "yellow", 0, False, 1),
            ("DDOS Attack", "red", "yellow", 0, False, 1),
            ("Email Reconnaissance", "red", "yellow", 0, False, 1),
            ("Infected USB", "red", "yellow", 0, False, 1),
            ("Intruder (HQ)", "red", "yellow", 0, False, 1),
            ("Intruder (Production)", "red", "yellow", 0, False, 1),
            ("Lost or Stolen PC", "red", "yellow", 0, False, 1),
            ("Phishing Attack", "red", "yellow", 0, False, 1),
            ("Port Scanning", "red", "yellow", 0, False, 1),
            ("Simple Web Server Hack", "red", "yellow", 0, False, 1),
            ("Spamming Attack", "red", "yellow", 0, False, 1),
            ("Targeted Scanning", "red", "yellow", 0, False, 1),
            ("Unsecured Wireless Network", "red", "yellow", 0, False, 1),

            # Red (Intermediate Attacks)
            ("Business Email Compromise", "red", "red", 0, False, 1),
            ("Compromised Account", "red", "red", 0, False, 2),
            ("Compromised PC", "red", "red", 0, False, 3),
            ("Compromised Server", "red", "red", 0, False, 2),
            ("Database Vulnerability", "red", "red", 0, False, 1),
            ("Defaced Web Site", "red", "red", 0, False, 1),
            ("Internal Phishing Attack", "red", "red", 0, False, 1),
            ("IoT Disruption", "red", "red", 0, False, 1),
            ("IoT Vulnerability", "red", "red", 0, False, 1),
            ("Lateral Movement", "red", "red", 0, False, 5),
            ("Malware", "red", "red", 0, False, 3),
            ("Privilege Escalation", "red", "red", 0, False, 1),
            ("Remote Access Trojan", "red", "red", 0, False, 1),
            ("Spear Phishing", "red", "red", 0, False, 1),
            ("Zero Day Attack", "red", "red", 0, False, 2),

            # Black (Final Attacks)
            ("Credential Theft", "red", "black", 0, False, 1),
            ("Data Exfiltration (Database)", "red", "black", 0, False, 1),
            ("Data Exfiltration (PC)", "red", "black", 0, False, 1),
            ("Data Exfiltration (Server)", "red", "black", 0, False, 1),
            ("Domain Dominance", "red", "black", 0, False, 1),
            ("IoT Destruction", "red", "black", 0, False, 1),
            ("Payment Diversion Fraud", "red", "black", 0, False, 1),
            ("Reputational Damage", "red", "black", 0, False, 1),

            # Blue Team Defenses
            ("Advanced Security Training", "blue", "defense", 30, False, 1),
            ("Anti-malware", "blue", "defense", 30, False, 1),
            ("Antivirus", "blue", "defense", 25, False, 1),
            ("CCTV (HQ)", "blue", "defense", 40, False, 1),
            ("CCTV (Production)", "blue", "defense", 40, False, 1),
            ("Complex Passwords", "blue", "defense", 10, False, 1),
            ("Data Loss Prevention", "blue", "defense", 20, True, 1),
            ("Database Software Patching", "blue", "defense", 50, False, 1),
            ("Firewall (HQ)", "blue", "defense", 25, False, 1),
            ("Firewall (Production)", "blue", "defense", 25, False, 1),
            ("Hard Drive Encryption", "blue", "defense", 25, False, 1),
            ("Identity Protection", "blue", "defense", 30, True, 1),
            ("IoT Controller Upgrade", "blue", "defense", 25, False, 1),
            ("Multi-factor Authentication", "blue", "defense", 20, True, 1),
            ("Network Monitoring", "blue", "defense", 40, False, 1),
            ("PC Operating System Patching", "blue", "defense", 25, False, 1),
            ("Penetration Test", "blue", "defense", 30, False, 1),
            ("Phishing Simulation", "blue", "defense", 30, False, 1),
            ("Role-Based Access Control", "blue", "defense", 20, True, 1),
            ("Security Awareness Training", "blue", "defense", 25, False, 1),
            ("Security Platform", "blue", "defense", 50, False, 1),
            ("Server Operating System Patching", "blue", "defense", 25, False, 1),
            ("Spam Filters", "blue", "defense", 10, False, 1),
            ("Threat Analytics", "blue", "defense", 50, True, 1),
        ]

        created = 0
        for entry in cards:
            # Support 5 or 6 fields depending on if quantity is specified
            if len(entry) == 5:
                name, team, ctype, cost, sp_required = entry
                quantity = 1
            else:
                name, team, ctype, cost, sp_required, quantity = entry

            obj, created_flag = Card.objects.get_or_create(
                name=name,
                defaults={
                    "team": team,
                    "card_type": ctype,
                    "cost": cost,
                    "sp_required": sp_required,
                    "quantity": quantity,
                }
            )
            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"{created} cards created."))
