class HelpDeskExpertSystem:
    def __init__(self):
        print("--- IT Help Desk Troubleshooting Expert System Initialized ---")

    def diagnose_issue(self, domain, system_powers_on, ping_successful, credentials_valid):
        # Knowledge Base Rules lookup
        if domain == "network":
            if ping_successful == 'no':
                return "Diagnosis: Local Gateway Isolation or Hardware Unplugged. Action: Restart router, check physical Ethernet connections."
            else:
                return "Diagnosis: DNS Failure or ISP Outage. Action: Flush local DNS cache, verify external nameservers."
        elif domain == "hardware":
            if system_powers_on == 'no':
                return "Diagnosis: PSU Failure or Dead Battery. Action: Replace power brick, swap electrical outlets."
            else:
                return "Diagnosis: POST Failure / RAM unseated. Action: Reseat Memory modules, check motherboard indicator LEDs."
        elif domain == "software":
            if credentials_valid == 'no':
                return "Diagnosis: Active Directory Lockout. Action: Trigger automated self-service password reset token."
            else:
                return "Diagnosis: Corrupt Local Application Registry profiles. Action: Clear local AppData caches and reinstall."
        else:
            return "Diagnosis: Unknown System Variant. Action: Escalating ticket to Tier-2 Engineering specialists."

# Interactive Interface
dom = input("Select Issue Domain (network / hardware / software): ").strip().lower()
pow_on = input("Does the physical asset power on? (yes/no/na): ").strip().lower()
ping = input("Can the asset successfully ping 8.8.8.8? (yes/no/na): ").strip().lower()
cred = input("Are the user credentials valid globally? (yes/no/na): ").strip().lower()

resolution = HelpDeskExpertSystem().diagnose_issue(dom, pow_on, ping, cred)
print(f"\n[System Diagnostic Result]\n{resolution}")
