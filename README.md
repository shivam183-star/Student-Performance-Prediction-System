# Student Performance Prediction System

A Machine Learning--based application that predicts a student's
**performance score** using academic and lifestyle factors.\
The project uses **Linear Regression**, includes proper **training and
evaluation pipelines**, and is deployed as an interactive **Streamlit
web app**.

------------------------------------------------------------------------

## Project Objective

The goal of this project is to predict student performance based on
measurable features such as: - Hours studied - Previous academic
scores - Extracurricular participation - Sleep duration - Practice
through sample question papers

------------------------------------------------------------------------

## Machine Learning Overview

-   **Algorithm:** Linear Regression\
-   **Learning Type:** Supervised Learning (Regression)
-   **Target Variable:** Performance Scores

------------------------------------------------------------------------

## Project Structure

student-performance-predictor/ 
├── app.py\
├── requirements.txt\
├── README.md\
├── .gitignore\
├── data/\
│ ├── Student.csv\
│ ├── Xtest.csv\
│ └── Ytest.csv\
├── model/\
│ └── model.pkl\
├── src/\
│ ├── train.py\
│ └── evaluate.py\
└── plots/\
└── actual_vs_predicted.png

------------------------------------------------------------------------

## How to Run

### Clone the repository
```bash
git clone https://github.com/shivam183-star/Student-Performance-Prediction-System.git
cd Student-Performance-Prediction-System
```

### Install dependencies
```bash
pip install -r requirements.txt
```
### Train Model
```bash
python src/train.py
```
### Evaluate Model
```bash
python src/evaluate.py
```
### Run Streamlit App
```bash
python -m streamlit run app.py
```

------------------------------------------------------------------------

## Evaluation Graph

The following graph compares actual and predicted performance values:

(Predictions_vs_Actual_Values.png)

------------------------------------------------------------------------

## Author
**Shivam**
- Student | Python Learner
- @shivam183-star

------------------------------------------------------------------------

## Support
If you find this project useful, consider giving it a star on GitHub!

------------------------------------------------------------------------

## License

For educational and academic use.
