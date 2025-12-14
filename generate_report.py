# generate_report.py
# Simple PDF report generation using reportlab
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(df, path='reports/summary_report.pdf'):
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont('Helvetica-Bold', 14)
    c.drawString(40, 760, 'Provider Data Validation Report')
    c.setFont('Helvetica', 10)
    total = len(df)
    valid = int((df['Confidence_Score'] >= 60).sum())
    flagged = int((df['Confidence_Score'] < 60).sum())
    c.drawString(40, 740, f'Total records: {total}')
    c.drawString(40, 726, f'Valid (>=60): {valid}')
    c.drawString(40, 712, f'Flagged (<60): {flagged}')
    y = 690
    c.drawString(40, y, 'Top records (id, name, score, needs_review):')
    y -= 16
    for i, row in df.head(20).iterrows():
        line = f"{i+1}. {row.get('Name','')} | Score: {row.get('Confidence_Score')} | Review: {row.get('Needs_Manual_Review')}"
        c.drawString(40, y, line[:90])
        y -= 14
        if y < 80:
            c.showPage()
            y = 750
    c.save()
    return path

if __name__ == '__main__':
    # simple smoke test
    import pandas as pd
    df = pd.read_csv('datasets/input.csv')
    from process import process_dataframe
    df2 = process_dataframe(df)
    generate_pdf(df2, path='reports/summary_report.pdf')
    print('Report generated at reports/summary_report.pdf')
