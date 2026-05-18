class PerformanceEvaluationExpertSystem:
    def __init__(self):
        print("--- Employee Performance Matrix Expert System Initialized ---")

    def evaluate_employee(self, kpi_score, leadership_rating, project_count):
        # Inference Logic
        if kpi_score >= 90 and leadership_rating >= 4 and project_count >= 5:
            return "Rating: Exceptional (Exceeds All Expectations). Action: Eligible for Immediate Promotion & Fast-Track Leadership Circle."
        elif kpi_score >= 80 and leadership_rating >= 3 and project_count >= 3:
            return "Rating: Strong Performer (Meets Expectations). Action: Standard Annual Merit Salary Increment Appraised."
        elif kpi_score >= 70 or project_count >= 2:
            return "Rating: Developing Performer. Action: Keep in current role, schedule specialized skill up-training modules."
        else:
            return "Rating: Unsatisfactory Performance. Action: Initiate Performance Improvement Plan (PIP) workflow immediately."

# Interactive Interface
try:
    kpi = float(input("Enter raw quantifiable KPI Metrics score (0-100): "))
    lead = int(input("Enter subjective Leadership Core evaluation rating (1-5): "))
    proj = int(input("Enter number of fully deployed production projects completed this cycle: "))

    recommendation = PerformanceEvaluationExpertSystem().evaluate_employee(kpi, lead, proj)
    print(f"\n[HR Performance Decision]\n{recommendation}")
except ValueError:
    print("Invalid numeric data input. Terminating execution.")
