# process.py
# Simple validation and scoring logic

import pandas as pd
import re

PHONE_RE = re.compile(r'^\d{10}$')
EMAIL_RE = re.compile(r'[^@]+@[^@]+\.[^@]+')
PIN_RE = re.compile(r'^\d{6}$')

def validate_phone(p):
    try:
        return bool(PHONE_RE.fullmatch(str(p).strip()))
    except:
        return False

def validate_email(e):
    try:
        return bool(EMAIL_RE.fullmatch(str(e).strip()))
    except:
        return False

def validate_pincode(pin):
    try:
        return bool(PIN_RE.fullmatch(str(pin).strip()))
    except:
        return False

def validate_address(a):
    return bool(a and str(a).strip())

def calculate_score(row):
    score = 0
    if row.get('Phone_Valid'): score += 30
    if row.get('Email_Valid'): score += 30
    if row.get('Address_Valid'): score += 20
    if row.get('Name') and str(row.get('Name')).strip(): score += 20
    return score

def process_dataframe(df):
    df = df.copy()
    # Ensure columns exist
    for c in ['Name','Phone','Email','Address','Pincode']:
        if c not in df.columns:
            df[c] = ''

    df['Phone_Valid'] = df['Phone'].apply(validate_phone)
    df['Email_Valid'] = df['Email'].apply(validate_email)
    df['Address_Valid'] = df['Address'].apply(validate_address)
    df['Pincode_Valid'] = df['Pincode'].apply(validate_pincode)
    df['Confidence_Score'] = df.apply(calculate_score, axis=1)
    df['Needs_Manual_Review'] = df['Confidence_Score'] < 60
    return df
