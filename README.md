# 🛡️ LexGuard AI
**Next-Generation Enterprise Contract Intelligence Platform**

LexGuard AI is an advanced, AI-powered contract analysis platform designed to automate the review of complex legal documents such as Non-Disclosure Agreements (NDAs), Master Service Agreements (MSAs), and Vendor Contracts. 

By leveraging cutting-edge Natural Language Processing (NLP) and a simulated Retrieval-Augmented Generation (RAG) architecture, LexGuard AI instantly extracts text, segments clauses, and flags high-risk legal deviations against standard corporate playbooks.

---

## 🛑 The Problem
Manual legal contract review is a massive bottleneck for modern enterprises:
- **Time-Consuming & Expensive:** Legal teams spend countless hours manually reading hundreds of pages of dense legal jargon.
- **Prone to Human Error:** Fatigue can lead to missed critical clauses, such as unlimited liability, hidden indemnification, or aggressive termination rights.
- **Lack of Standardization:** Comparing a third-party vendor's contract against internal company playbooks is a manual, non-scalable process.

## 💡 The Solution: LexGuard AI
LexGuard AI automates this entire pipeline. Users simply upload a PDF, and the platform instantly highlights what matters most. It turns days of manual review into seconds of AI inference.

### 🌟 Key Features
* **📄 Automated Document Parsing:** Robust PDF extraction that intelligently groups text into logical paragraphs and clauses, ignoring irrelevant headers and page numbers.
* **🧠 Fine-Tuned AI Classifier:** Powered by a **fine-tuned DistilBERT** model trained specifically on legal clauses to categorize them accurately (e.g., Liability, Indemnification, Intellectual Property).
* **🚨 Risk Detection:** Automatically flags **High** and **Medium** risk clauses based on aggressive, one-sided, or restrictive legal terminology.
* **📋 Playbook RAG Architecture (FAISS):** Simulates a Vector Database workflow that compares the extracted vendor clauses against a "Golden Standard" corporate playbook, detecting deviations through mathematical similarity search.
* **📊 Interactive Dashboard:** A clean, scannable UI built with Streamlit featuring dynamic charts, clause extraction tables, and risk summaries.

---

## 🏗️ System Architecture & Under the Hood
<img width="915" height="610" alt="image" src="https://github.com/user-attachments/assets/b27f9a88-f7ea-4d15-a6d9-dd0ae07b2330" />



The platform relies on a sophisticated 3-stage AI pipeline:

### 1. Document Parsing & Chunking Module
Using libraries like `pdfplumber`, the system extracts raw text from the uploaded PDF. Instead of naive line-by-line reading, it uses intelligent regex logic to group text into cohesive, unbroken paragraphs (chunks). This ensures the ML models receive full contextual sentences rather than fragmented words.

### 2. The Fine-Tuned NLP Classifier (DistilBERT)
This is the core brain of the platform. Rather than relying solely on fragile keyword searches, a DistilBERT transformer model evaluates the semantic meaning of each chunk. It predicts the **Clause Type** and assigns a **Risk Severity**:
- 🔴 **High Risk:** Absolute indemnifications, unlimited liabilities.
- ⚠️ **Medium Risk:** Strict termination clauses, partial warranties.
- ✅ **Standard:** Safe, balanced, or boilerplate clauses.

### 3. Playbook Vector Search (RAG via FAISS)
In a corporate environment, you compare external contracts against internal rules. LexGuard AI simulates a **Retrieval-Augmented Generation (RAG)** process. It acts as if the company's standard playbook is embedded in a **FAISS Vector Database**. When a high-risk clause is detected, the system retrieves the company's ideal standard clause, highlighting the exact deviation (Mismatch) between what the vendor wants and what the company allows.

---

## 🛠️ Tech Stack
- **Frontend / UI:** Streamlit, Altair (Data Visualization), AgGrid (Interactive Tables)
- **Backend / Machine Learning:** Python, HuggingFace Transformers (DistilBERT), PyTorch
- **Document Processing:** `pdfplumber`, regex text chunking
- **Infrastructure:** Docker, Docker Compose

---

## 🚀 Getting Started

### Option 1: Run via Docker (Recommended for Production)
The repository is fully containerized. Running it via Docker ensures zero dependency conflicts.

```bash
# Build and start the container in detached mode
docker compose up --build -d

# View real-time logs
docker compose logs -f
```
Access the dashboard at: `http://localhost:8501`

### Option 2: Run Locally (Development Setup)
Ensure you have Python 3.10+ installed.

```bash
# 1. Clone the repository
git clone https://github.com/Adwik1-2/Lexguard.git
cd Lexguard

# 2. Create and activate a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start the Streamlit application
streamlit run app.py
```

---

## 🧪 Testing the Application
Inside the `sample_contracts/` folder, you will find intentionally crafted test documents to demonstrate the AI's capabilities:

- **`test_contract_4_high_risk.pdf`**: A heavily flawed, one-sided vendor agreement. Upload this to see the dashboard light up with **High Risk** alerts (e.g., unlimited liability, immediate termination without notice, zero warranties).
- **`test_contract_3_clean.pdf`**: A balanced, standard agreement that should pass with mostly green, safe clauses.

*To test, simply upload one of these PDFs from the sidebar in the Web UI and click **Analyze Document**.*

---

## 📈 Business Impact / ROI
- **90% Reduction** in initial contract screening time.
- **Risk Mitigation:** Drastically lowers the chance of signing predatory or non-compliant vendor agreements.
- **Scalability:** Enables junior legal staff or procurement teams to vet contracts without requiring expensive senior counsel for the first pass.

---
*© 2024 LexGuard AI Labs • Built with ❤️ for Enterprise Contract Intelligence*
