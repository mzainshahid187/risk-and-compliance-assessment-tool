# ============================================================
#   Risk and Compliance Assessment Tool
#   Python OOP Project
# ============================================================

# ─────────────────────────────────────────
# CLASS 1: 
# ─────────────────────────────────────────
class Risk:
    """Represents a single risk in the organization."""

    def __init__(self, risk_id, name, probability, impact, owner):
        self.risk_id     = risk_id       # unique ID
        self.name        = name          # name of risk
        self.probability = probability   # chance it happens  (1-5)
        self.impact      = impact        # damage if it does  (1-5)
        self.owner       = owner         # responsible person
        self.mitigation  = "Not defined" # plan to reduce risk

    def calculate_score(self):
        """Risk Score = Probability x Impact"""
        return self.probability * self.impact

    def get_level(self):
        """Return LOW / MEDIUM / HIGH based on score."""
        score = self.calculate_score()
        if score <= 6:
            return "LOW"
        elif score <= 15:
            return "MEDIUM"
        else:
            return "HIGH"

    def display(self):
        """Print risk details to the console."""
        print(f"  Risk ID    : {self.risk_id}")
        print(f"  Name       : {self.name}")
        print(f"  Probability: {self.probability}/5")
        print(f"  Impact     : {self.impact}/5")
        print(f"  Score      : {self.calculate_score()}")
        print(f"  Level      : {self.get_level()}")
        print(f"  Owner      : {self.owner}")
        print(f"  Mitigation : {self.mitigation}")


# ─────────────────────────────────────────
# CLASS 2: ComplianceRequirement
# ─────────────────────────────────────────
class ComplianceRequirement:
    """Represents one compliance rule the organization must follow."""

    def __init__(self, req_id, name, framework):
        self.req_id    = req_id       # unique ID
        self.name      = name         # requirement name
        self.framework = framework    # e.g. GDPR, ISO27001
        self.status    = "Pending"    # Compliant / Non-Compliant / Pending
        self.evidence  = []           # list of proof documents

    def set_status(self, status):
        """Set compliance status."""
        allowed = ["Compliant", "Non-Compliant", "Pending"]
        if status in allowed:
            self.status = status
        else:
            print(f"  Invalid status! Choose from: {allowed}")

    def add_evidence(self, evidence):
        """Add a piece of evidence for this requirement."""
        self.evidence.append(evidence)

    def display(self):
        """Print requirement details to the console."""
        print(f"  Req ID    : {self.req_id}")
        print(f"  Name      : {self.name}")
        print(f"  Framework : {self.framework}")
        print(f"  Status    : {self.status}")
        if self.evidence:
            print(f"  Evidence  : {', '.join(self.evidence)}")
        else:
            print(f"  Evidence  : None provided")


# ─────────────────────────────────────────
# CLASS 3: Assessment
# ─────────────────────────────────────────
class Assessment:
    """Holds all risks and compliance requirements for an assessment."""

    def __init__(self, assessment_id, name):
        self.assessment_id = assessment_id
        self.name          = name
        self.risks         = []           # list of Risk objects
        self.requirements  = []           # list of ComplianceRequirement objects

    def add_risk(self, risk):
        """Add a Risk object to this assessment."""
        self.risks.append(risk)

    def add_requirement(self, requirement):
        """Add a ComplianceRequirement object to this assessment."""
        self.requirements.append(requirement)

    def get_average_risk_score(self):
        """Return the average risk score across all risks."""
        if not self.risks:
            return 0
        total = sum(r.calculate_score() for r in self.risks)
        return total / len(self.risks)

    def get_compliance_percentage(self):
        """Return the percentage of compliant requirements."""
        if not self.requirements:
            return 0
        compliant = sum(1 for r in self.requirements if r.status == "Compliant")
        return (compliant / len(self.requirements)) * 100


# ─────────────────────────────────────────
# CLASS 4: ReportPrinter
# ─────────────────────────────────────────
class ReportPrinter:
    """Prints summary reports for an assessment."""

    def print_risk_report(self, assessment):
        """Print all risks in the assessment."""
        print("\n" + "=" * 50)
        print(f"  RISK REPORT — {assessment.name}")
        print("=" * 50)

        if not assessment.risks:
            print("  No risks added yet.")
            return

        for risk in assessment.risks:
            print()
            risk.display()

        print()
        print(f"  Total Risks         : {len(assessment.risks)}")
        print(f"  Avg Risk Score      : {assessment.get_average_risk_score():.1f}")

        high   = sum(1 for r in assessment.risks if r.get_level() == "HIGH")
        medium = sum(1 for r in assessment.risks if r.get_level() == "MEDIUM")
        low    = sum(1 for r in assessment.risks if r.get_level() == "LOW")

        print(f"  High Level Risks    : {high}")
        print(f"  Medium Level Risks  : {medium}")
        print(f"  Low Level Risks     : {low}")

    def print_compliance_report(self, assessment):
        """Print all compliance requirements in the assessment."""
        print("\n" + "=" * 50)
        print(f"  COMPLIANCE REPORT — {assessment.name}")
        print("=" * 50)

        if not assessment.requirements:
            print("  No requirements added yet.")
            return

        for req in assessment.requirements:
            print()
            req.display()

        print()
        print(f"  Total Requirements  : {len(assessment.requirements)}")
        print(f"  Compliance Rate     : {assessment.get_compliance_percentage():.1f}%")

    def print_summary(self, assessment):
        """Print a short summary of the whole assessment."""
        print("\n" + "=" * 50)
        print(f"  SUMMARY — {assessment.name}")
        print("=" * 50)
        print(f"  Assessment ID       : {assessment.assessment_id}")
        print(f"  Total Risks         : {len(assessment.risks)}")
        print(f"  Avg Risk Score      : {assessment.get_average_risk_score():.1f} / 25")
        print(f"  Total Requirements  : {len(assessment.requirements)}")
        print(f"  Compliance Rate     : {assessment.get_compliance_percentage():.1f}%")


# ─────────────────────────────────────────
# MAIN — Run the program
# ─────────────────────────────────────────
def main():
    print("\n" + "=" * 50)
    print("  RISK & COMPLIANCE ASSESSMENT TOOL")
    print("=" * 50)

    # --- Create Assessment ---
    assessment = Assessment("A001", "IT Security Assessment")

    # --- Create Risks ---
    r1 = Risk("R001", "Data Breach",     probability=4, impact=5, owner="Zain")
    r1.mitigation = "Enable encryption and MFA"

    r2 = Risk("R002", "Server Downtime", probability=3, impact=4, owner="Kaif")
    r2.mitigation = "Set up backup servers"

    r3 = Risk("R003", "Phishing Attack", probability=5, impact=3, owner="Huzaifa")
    r3.mitigation = "Conduct security awareness training"

    r4 = Risk("R004", "Weak Passwords",  probability=2, impact=2, owner="Haris")
    r4.mitigation = "Enforce strong password policy"

    # --- Add Risks to Assessment ---
    assessment.add_risk(r1)
    assessment.add_risk(r2)
    assessment.add_risk(r3)
    assessment.add_risk(r4)

    # --- Create Compliance Requirements ---
    c1 = ComplianceRequirement("C001", "Data Encryption",      framework="GDPR")
    c1.set_status("Compliant")
    c1.add_evidence("Encryption audit report - Jan 2024")

    c2 = ComplianceRequirement("C002", "Access Control Policy", framework="ISO27001")
    c2.set_status("Non-Compliant")

    c3 = ComplianceRequirement("C003", "Security Training",     framework="ISO27001")
    c3.set_status("Compliant")
    c3.add_evidence("Training records for all staff")

    c4 = ComplianceRequirement("C004", "Incident Response Plan",framework="NIST")
    c4.set_status("Pending")

    # --- Add Requirements to Assessment ---
    assessment.add_requirement(c1)
    assessment.add_requirement(c2)
    assessment.add_requirement(c3)
    assessment.add_requirement(c4)

    # --- Print Reports ---
    printer = ReportPrinter()
    printer.print_risk_report(assessment)
    printer.print_compliance_report(assessment)
    printer.print_summary(assessment)

    print("\n  Program finished.\n")


if __name__ == "__main__":
    main()
