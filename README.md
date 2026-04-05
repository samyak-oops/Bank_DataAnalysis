# 🏦 Bank Customer Churn Prediction

A machine learning-powered web application that predicts whether a bank customer is likely to churn based on their demographic and financial data.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://bankdataanalysis.streamlit.app/)

---

## 🚀 Live Demo

**Try it out:** [https://bankdataanalysis.streamlit.app/](https://bankdataanalysis.streamlit.app/)

---

## 📋 Overview

This application uses a trained machine learning model to analyze customer data and predict the probability of customer churn. It provides an intuitive interface for entering customer details and instantly receiving churn predictions.

### Features

- 🔮 **Churn Probability Prediction** - Get instant predictions on customer churn likelihood
- 📊 **Interactive Input Form** - Easy-to-use sliders and dropdowns for data entry
- 🎯 **Clear Results Display** - Visual indication of churn risk with probability score
- ⚡ **Real-time Processing** - Fast predictions powered by machine learning

---

## 🛠️ Input Parameters

The model uses the following customer features to make predictions:

| Parameter | Description |
|-----------|-------------|
| **Credit Score** | Customer's credit score (300-850) |
| **Geography** | Customer's country (France, Spain, Germany) |
| **Gender** | Customer's gender (Male/Female) |
| **Age** | Customer's age |
| **Tenure** | Number of years as a bank customer |
| **Balance** | Account balance |
| **Number of Products** | Number of bank products held |
| **Has Credit Card** | Whether customer has a credit card (Yes/No) |
| **Is Active Member** | Whether customer is an active member (Yes/No) |
| **Estimated Salary** | Customer's estimated annual salary |

---

## 💻 Tech Stack

- **Python** - Core programming language
- **Streamlit** - Web application framework
- **Scikit-learn / TensorFlow / PyTorch** - Machine learning model
- **Pandas** - Data manipulation
- **NumPy** - Numerical computations

---

## 🏃 Getting Started

### Prerequisites

- Python 3.7+
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/samyak-oops/bank-dl.git
cd bank-dl
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application locally:
```bash
streamlit run app.py
```

4. Open your browser and navigate to `http://localhost:8501`

---

## 📁 Project Structure

```
bank-dl/
├── app.py                 # Main Streamlit application
├── model/                 # Trained ML model files
│   └── churn_model.pkl
├── data/                  # Dataset files
│   └── bank_churn.csv
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

---

## 📊 Model Performance

The churn prediction model is trained on historical bank customer data and achieves high accuracy in identifying customers at risk of leaving the bank.

---

## 🎯 Use Cases

- **Customer Retention** - Identify at-risk customers and take proactive measures
- **Marketing Strategy** - Target customers with personalized retention offers
- **Risk Assessment** - Evaluate portfolio health and churn risk
- **Business Intelligence** - Gain insights into factors driving customer churn

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Samyak** - [@samyak-oops](https://github.com/samyak-oops)

---

## 🙏 Acknowledgments

- Dataset source: [Bank Customer Churn Dataset](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)
- Built with [Streamlit](https://streamlit.io/)

---

## 📧 Contact

For questions or feedback, please reach out via GitHub issues.

---

<p align="center">Made with ❤️ using Streamlit</p>
