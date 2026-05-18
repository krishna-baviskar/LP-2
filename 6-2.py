class MedicalTriageExpertSystem:
    def __init__(self):
        print("--- Hospital Triage & Medical Expert System Initialized ---")

    def infer_condition(self, chest_pain, fever, cough, breathing_difficulty):
        # Inference Engine
        if chest_pain == 'yes' or breathing_difficulty == 'yes':
            return "RED ALERT: High Probability of Cardiac or Severe Respiratory Distress. Route immediately to ER."
        elif fever == 'yes' and cough == 'yes':
            return "YELLOW ALERT: Suspected Lower Respiratory Infection (e.g., Pneumonia/Bronchitis). Route to Urgent Care."
        elif fever == 'yes' and cough == 'no':
            return "GREEN ALERT: Isolated Febrile Illness. Route to General Outpatient Clinic for testing."
        elif fever == 'no' and cough == 'yes':
            return "GREEN ALERT: Mild Upper Respiratory Allergy/Cold symptoms. Advise over-the-counter care or OPD."
        else:
            return "GREEN ALERT: Non-Urgent. Routine health check-up routing."

# Interactive Interface
print("Please answer the triage queries with 'yes' or 'no':")
cp = input("Is the patient experiencing active chest pain? ").strip().lower()
fv = input("Does the patient have a fever (> 100.4°F)? ").strip().lower()
cg = input("Is the patient presenting a persistent cough? ").strip().lower()
bd = input("Is the patient experiencing shortness of breath? ").strip().lower()

diagnosis = MedicalTriageExpertSystem().infer_condition(cp, fv, cg, bd)
print(f"\n[Expert Evaluation]\nRecommended Action: {diagnosis}")
