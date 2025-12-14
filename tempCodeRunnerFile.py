# app.py - Simple Flask app for Provider Data Validation
from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from process import process_dataframe
from generate_report import generate_pdf

app = Flask(__name__)
UPLOAD_FOLDER = 'datasets'
CLEANED_PATH = os.path.join(UPLOAD_FOLDER, 'cleaned_output.csv')
GRAPH_PATH = os.path.join('static', 'score_bar.png')

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f = request.files.get('file')
        if not f:
            return 'No file uploaded', 400
        filename = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(filename)
        try:
            df = pd.read_csv(filename)
        except Exception as e:
            return f'Error reading CSV: {e}', 400
        df_processed = process_dataframe(df)
        df_processed.to_csv(CLEANED_PATH, index=False)
        # generate bar graph for Confidence_Score distribution
        plt.figure(figsize=(6,3))
        df_processed['Confidence_Score'].value_counts().sort_index().plot(kind='bar')
        plt.xlabel('Confidence Score')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig(GRAPH_PATH)
        plt.close()
        # generate pdf report
        report_file = generate_pdf(df_processed, path=os.path.join('reports','summary_report.pdf'))
        return render_template('results.html', tables=[df_processed.head(50).to_html(classes='table table-striped', index=False)], graph_url=GRAPH_PATH, report_path=report_file)
    return render_template('upload.html')

@app.route('/download-clean')
def download_clean():
    if os.path.exists(CLEANED_PATH):
        return send_file(CLEANED_PATH, as_attachment=True)
    return 'No cleaned file found', 404

@app.route('/download-report')
def download_report():
    rp = os.path.join('reports','summary_report.pdf')
    if os.path.exists(rp):
        return send_file(rp, as_attachment=True)
    return 'No report found', 404

if __name__ == '__main__':
    # create folders if missing
    os.makedirs('static', exist_ok=True)
    os.makedirs('datasets', exist_ok=True)
    os.makedirs('reports', exist_ok=True)
    app.run(debug=True, port=5001)
