# Basic Risk and Compliance Assessment Tool

A lightweight, standalone Python command-line utility built to evaluate system infrastructures against defined asset risk matrices and compliance rules.

## ⚙️ Features
* **Risk Score Matrix:** Evaluates threat probability against asset criticality to calculate overall risk levels (Low, Medium, High, Critical).
* **Compliance Checks:** Cross-references machine environment baselines against key security configuration policies.
* **Remediation Output:** Prints clear actionable summaries identifying vulnerabilities and recommended patching updates.

## 🛠️ Technical Stack & Architecture
* **Language:** Python 3.x
* **Deployment:** Standalone Single-File execution (`risk_tool.py`)
* **Libraries Used:** System native modules (e.g., `sys`, `os`, `json`)

## 🚀 Installation & Quickstart

1. Download the `risk_tool.py` file directly from this repository.
2. Open your terminal or command prompt in that directory.
3. Run the assessment tool instantly (No external dependencies required):
   ```bash
   python risk_tool.py
