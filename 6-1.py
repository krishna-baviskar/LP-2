class InfoManagementExpertSystem:
    def __init__(self):
        print("--- Information Management Expert System Initialized ---")

    def evaluate_asset(self, contains_pii, business_critical, operational_use):
        # Knowledge Base & Inference Engine
        if contains_pii == 'yes' and business_critical == 'yes':
            tier = "Tier 1 (Highly Restricted)"
            storage = "Encrypted On-Premise Core Servers"
            retention = "7 Years (Regulatory Mandate)"
        elif contains_pii == 'yes' and business_critical == 'no':
            tier = "Tier 2 (Confidential/Internal)"
            storage = "Secure Cloud Bucket with IAM Roles"
            retention = "3 Years"
        elif contains_pii == 'no' and business_critical == 'yes':
            tier = "Tier 2 (Business Operational Assets)"
            storage = "Redundant Hybrid Cloud Storage"
            retention = "Indefinite / Continuous Review"
        else:
            tier = "Tier 3 (Public / Low Sensitivity)"
            storage = "Standard Shared Cloud Drives"
            retention = "1 Year / Purge when obsolete"
            
        return tier, storage, retention

# Interactive Interface
es = InfoManagementExpertSystem()
pii = input("Does the data asset contain PII / financial records? (yes/no): ").strip().lower()
critical = input("Is this asset mission-critical for daily business operations? (yes/no): ").strip().lower()
op = input("Is the asset used primarily for short-term operational tasks? (yes/no): ").strip().lower()

tier, storage, retention = es.evaluate_asset(pii, critical, op)
print(f"\n[Decision Output]\nClassification: {tier}\nStorage Target: {storage}\nRetention Policy: {retention}")
