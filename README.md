# Adas-crash-analysis
Analysis and data-quality validation of real-world Level 2 ADAS crash reports (NHTSA)

# Real-World ADAS Crash Data: Analysis & Data Quality

**Status: in progress**

## Question
What can real-world crash reports tell us about Level 2 driver-assistance systems (e.g., adaptive cruise control with lane centering), and how far can this data be trusted?

1. Under what conditions do reported crashes happen (road type, speed, lighting, weather, crash partner)?
2. How has crash reporting changed over time, including after the 2025 rule change?
3. How reliable is the data? A data-quality scorecard per reporting manufacturer.

## Data
NHTSA Standing General Order 2021-01 incident reports for Level 2 ADAS (current and 2021–2025 archive files), publicly available at nhtsa.gov/SGOcrashReporting.

## Approach
- Load and explore the data (pandas)
- Clean: latest report versions, duplicates, merging archive and current files
- Automated data validation (pytest, pandera) running in GitHub Actions
- Reconcile results with NHTSA's published figures
- SQL analysis (DuckDB) and statistical tests (SciPy)
- Logistic regression on crash severity (scikit-learn)
- Tableau dashboard

## Limitations
- No exposure data (miles driven with ADAS engaged), so manufacturers cannot be ranked by safety
- Only crashes above the reporting thresholds are included
- Self-reported, unverified data with redacted fields and possible duplicates
- US data only