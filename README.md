# Drug Interaction Safety Assistant

An AI-powered Drug Interaction Safety Assistant using Retrieval-Augmented Generation (RAG) to detect potential drug interactions, assess risk severity, and provide easy-to-understand safety recommendations.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Overview

Drug interactions are one of the leading causes of preventable adverse drug events. Patients often take multiple medications simultaneously, increasing the risk of harmful interactions.

The "Drug Interaction Safety Assistant" is an intelligent healthcare application that analyzes two or more medications, detects possible interactions, estimates their severity, and explains the associated risks in simple language.

Unlike traditional drug checkers, this system combines "Retrieval-Augmented Generation (RAG)" with a structured medical dataset to provide fast, reliable, and user-friendly recommendations.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Problem Statement

Patients frequently consume multiple medicines prescribed by different healthcare providers. Existing drug interaction tools usually:

- Only indicate whether an interaction exists.
- Do not explain the interaction in simple language.
- Lack severity prioritization.
- Provide limited guidance for patients.

This project addresses these issues by building an AI-powered assistant capable of retrieving medical knowledge, assessing interaction severity, and generating understandable safety recommendations.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Features

 Drug Interaction Detection

Checks whether selected medicines interact with each other using the medical dataset.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Risk Severity Assessment

Each interaction is assigned a severity score and categorized into risk levels.

| Score   | Risk Level |
|-------- |------------|
| 0 – 20  |  Safe      |
| 21 – 50 |  Moderate  |
| 51 – 80 |  High      |
| 81 – 100| Critical   |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Patient-Friendly Explanation

Converts complex medical terminology into simple explanations.

Example:

Medical Description

Concurrent administration increases anticoagulant activity.

Patient Explanation

Taking these medicines together may increase the risk of bleeding.
Consult your doctor before using them together.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Emergency Alerts

Critical interactions automatically trigger emergency warnings.

Example

🚨 High Risk Interaction Detected

Immediate medical consultation is recommended.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Retrieval-Augmented Generation (RAG)

Instead of relying solely on an AI model, the application retrieves relevant information from its own medical knowledge base before generating responses.

Benefits:

- More accurate responses
- Reduced hallucinations
- Faster retrieval
- Evidence-based recommendations

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Semantic Drug Search

Uses vector similarity search to retrieve relevant drug information even when exact drug names are unavailable.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  System Architecture


                    User

                      │
                      ▼

               Gradio Interface

                      │
                      ▼

            Drug Interaction Engine

         ┌────────────┬─────────────┐
         ▼                          ▼

  Drug Information          Interaction Search

         │                          │
         └────────────┬─────────────┘
                      ▼

               TF-IDF Vectorizer

                      ▼

              FAISS Vector Store

                      ▼

        Drug Interaction Dataset

                      ▼

         Safety Recommendation Engine

                      ▼

              Final Response
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Technologies Used

| Technology       | Purpose                    |
|------------------|----------------------------|
| Python           | Core Programming           |
| Pandas           | Dataset Processing         |
| NumPy            | Numerical Operations       |
| Gradio           | Web User Interface         |
| FAISS            | Vector Similarity Search   |
| TF-IDF           | Text Embedding Generation  |
| Scikit-Learn     | Machine Learning Utilities |
| Jupyter Notebook | Development Environment    |

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dataset

The project uses a healthcare dataset containing patient and medication information.

 Dataset Includes

- Patient ID
- Patient Name
- Gender
- Age
- State
- City
- Primary Drug
- Secondary Drug
- Drug Interaction
- Interaction Severity
- Risk Score

The dataset enables the assistant to identify known interactions and estimate the associated risk.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Structure

Drug-Interaction-Safety-Assistant/

│
├── RAGWar.ipynb
├── indian_drug_interaction_dataset.csv
├── requirements.txt
├── README.md
│
├── vector_store/
│      faiss_index
│
├── models/
│
└── assets/

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Installation

# Clone Repository

bash
git clone https://github.com/devwithanurag/Drug-Interaction-Safety-Assistant.git

cd Drug-Interaction-Safety-Assistant

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Install Dependencies

bash
pip install -r requirements.txt


or

bash
pip install pandas numpy scikit-learn faiss-cpu gradio

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Running the Application

Launch the notebook

bash
jupyter notebook


Open


RAGWar.ipynb


Run all cells.

If converted into a Python application:

bash
python app.py

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🔄 Workflow

User enters two drug names
            │
            ▼
Input Validation
            │
            ▼
TF-IDF Embedding Generation
            │
            ▼
FAISS Similarity Search
            │
            ▼
Retrieve Relevant Drug Information
            │
            ▼
Interaction Detection
            │
            ▼
Risk Severity Calculation
            │
            ▼
Generate Safety Recommendation
            │
            ▼
Display Results

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Example

 Input

Drug 1 : Warfarin
Drug 2 : Aspirin

 Output

Interaction Found

Severity : Critical

Risk Score : 92

Explanation

Taking these medicines together can significantly
increase the risk of bleeding.

Recommendation

Avoid using both medicines together without medical supervision.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Advantages

- Fast interaction detection
- AI-assisted recommendations
- Patient-friendly explanations
- Vector-based semantic search
- Accurate retrieval using FAISS
- Easy-to-use interface
- Scalable architecture
- Reduces medication errors

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Applications

- Hospitals
- Pharmacies
- Telemedicine Platforms
- Clinical Decision Support Systems
- Medical Colleges
- Healthcare Research
- Personal Medication Safety

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Future Enhancements

- Multi-drug interaction analysis
- Food-drug interaction detection
- Drug allergy prediction
- Prescription OCR
- Voice assistant support
- Electronic Health Record (EHR) integration
- Mobile application
- Multilingual support
- Large Language Model (LLM) integration
- Real-time medical database synchronization

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Performance Highlights

- Efficient vector retrieval using FAISS
- Semantic drug search with TF-IDF embeddings
- Fast response generation
- Lightweight deployment
- User-friendly interface

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 👥 Contributors

Team Name RAGWar

  Topic - Drug Interaction Safety Assistant

Members

- Member 1 Anurag Tiwari(Team Leader)
- Member 2 Jyoti Kumari

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# License

This project is developed for educational, research, and hackathon purposes.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Acknowledgements

Special thanks to

- Open Source Community
- Python
- FAISS
- Scikit-Learn
- Gradio
- Healthcare Research Community

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Why This Project?

This project demonstrates how Artificial Intelligence and Retrieval-Augmented Generation (RAG) can improve medication safety by providing intelligent, explainable, and patient-friendly drug interaction analysis. It bridges the gap between traditional drug databases and modern AI-powered clinical decision support systems.
