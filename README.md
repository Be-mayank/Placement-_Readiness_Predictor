# Placement Readiness Predictor — GDG-USAR AIML Task 1

## Objective
Build a binary classifier that predicts whether a student is **Placed** or **Not Placed** using the supplied placement-readiness dataset.

## Task Requirements Covered
- Data cleaning and duplicate handling
- Missing-value handling
- Categorical encoding
- Useful feature selection
- Binary classification
- Comparison of two simple classifiers
- Precision, Recall and F1-score
- Example prediction with explanation
- Meaningful decisions documented in `DECISIONS.md`
- Decision Tree feature importance / interpretability
- Optional Streamlit input interface

## Models
1. **Logistic Regression** — simple linear baseline.
2. **Decision Tree** — interpretable nonlinear classifier.

## Important preprocessing decisions
- Remove duplicate rows **before** train/test split.
- Exclude `name` and `email` because they are identifiers.
- Exclude `other_course` because it is a redundant companion field.
- Exclude `opinion` because it is free text and would require an NLP pipeline.
- Exclude `placement` from input features because it is the target.

## Feature engineering
`languages` is converted into:
- `language_count`
- `has_python`
- `has_java`
- `has_cplusplus`
- `has_c`
- `has_javascript`

`certifications` is converted into:
- `certification_count`
- `cert_ai_ml`
- `cert_data_analytics`
- `cert_cloud_computing`
- `cert_cyber_security`

## Preprocessing
Numerical columns:
- Median imputation
- Standard scaling

Categorical columns:
- Most-frequent imputation
- One-hot encoding

All preprocessing is inside the scikit-learn pipeline to avoid leakage.

## Evaluation
The notebook reports:
- Accuracy
- Precision
- Recall
- F1-score
- Classification report
- Confusion matrix

The required metrics are Precision, Recall and F1-score. The final model is selected using the highest test-set F1-score.

## Example prediction
The notebook predicts one held-out test student and reports:
- actual placement
- predicted placement
- probability of `Placed`
- whether the prediction was correct

It also demonstrates a custom student input.

## Project structure
```text
Placement_Readiness_Predictor_GDG_USAR/
├── README.md
├── DECISIONS.md
├── requirements.txt
├── .gitignore
├── app.py
├── Placement_Readiness_Predictor.ipynb
└── data/
    └── README.md
```

The supplied CSV is not redistributed in this repository. Upload it in Colab or place it in `data/` locally.

## Run in Google Colab
1. Open `Placement_Readiness_Predictor.ipynb`.
2. Run cells from top to bottom.
3. Upload the supplied CSV when prompted.
4. The notebook trains, compares, evaluates and saves the best model.

## Local setup
```bash
pip install -r requirements.txt
jupyter notebook Placement_Readiness_Predictor.ipynb
```

## Optional Streamlit interface
After running the notebook:
```bash
streamlit run app.py
```

The notebook saves the trained model as `placement_readiness_model.joblib`.

## Technologies
Python, Pandas, NumPy, scikit-learn, Matplotlib, Seaborn, Joblib, Streamlit.

## Submission checklist
- [x] Cleaning
- [x] Missing values
- [x] Duplicate removal
- [x] Categorical encoding
- [x] Feature selection
- [x] Binary classification
- [x] Two models
- [x] Precision
- [x] Recall
- [x] F1-score
- [x] Example prediction
- [x] Explanation
- [x] Interpretability
- [x] `DECISIONS.md`
- [x] Optional input interface
