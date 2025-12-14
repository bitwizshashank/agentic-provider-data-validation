# Agentic AI Provider Data Validation System

## Problem

Healthcare payers maintain large provider directories that frequently contain incorrect or outdated information.
Industry studies report **40–80% data inaccuracy**, leading to compliance risks, operational cost, and poor member experience.
Manual verification is slow, repetitive, and not scalable.

## Solution Overview

This project implements an **Agentic AI–inspired automated provider data validation system**.

The system:

- Validates provider contact and address data
- Enriches and scores records using rule-based agents
- Flags low-confidence entries for manual review
- Stores clean data in MySQL-compatible format
- Generates PDF summary reports
- Provides a lightweight Flask web dashboard

## Architecture

- **Master Agent**: Orchestrates validation workflow
- **Validation Agent**: Phone, email, address checks
- **Scoring Agent**: Assigns data quality score
- **Reporting Agent**: Generates PDF summary
- **UI Layer**: Flask dashboard for upload and results

## Tech Stack

- Python
- Pandas
- Flask
- ReportLab (PDF generation)
- HTML/CSS (Jinja templates)
- MySQL-ready output

## Project Structure

```
.
├── app.py                 # Flask application
├── process.py             # Validation & scoring logic
├── generate_report.py     # PDF report generator
├── datasets/
│   └── input.csv
├── templates/
│   ├── upload.html
│   └── results.html
├── static/
├── reports/
├── requirements.txt
└── run.sh
```

## How It Works

1. Upload provider CSV file
2. Master agent triggers validation and scoring
3. Data quality score is computed per record
4. Clean data is stored and low-score entries flagged
5. PDF summary is generated
6. Results displayed on dashboard

## Setup & Run

```bash
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open browser at:

```
http://127.0.0.1:5000
```

## Limitations (Honest)

- Rule-based validation (no live external APIs)
- No real-time license verification
- Agentic logic is simulated

## Future Improvements

- Integrate NPI registry & license APIs
- Replace rule-based agents with LLM agents
- Add scheduling and periodic re-validation
- MySQL persistence instead of CSV

## Author

**Shashank Shukla**  
Email: [shashankshukla0105@gmail.com](mailto:shashankshukla0105@gmail.com)  
LinkedIn: [linkedin.com/in/your-linkedin-username](https://www.linkedin.com/in/shashankshukla0806)
