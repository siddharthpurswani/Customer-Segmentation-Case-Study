# 🛍️ Customer Segmentation Case Study

## 📌 Overview
This project applies unsupervised machine learning on **550,000+ real-world transactional records** to segment customers into distinct behavioral groups using **RFM Analysis** and **K-Means Clustering**. The goal is to help businesses move away from one-size-fits-all marketing and instead execute **precision-targeted strategies** per customer segment.

---

## 🎯 Problem Statement
Businesses often struggle to understand *who* their customers are and *how* to engage them effectively. This project addresses that by leveraging transactional data to identify distinct customer personas — enabling smarter retention, upselling, and re-activation strategies.

---

## 📂 Dataset
- **Size:** 550,000+ transactional records
- **Key Features:** Customer ID, Invoice Date, Quantity, Unit Price, Country
- **Engineered Features:** Recency, Frequency, Monetary Value, Purchase Month, Day of Week, Transaction Aggregates

---

## 🔧 Methodology

**1. Data Cleaning & Preprocessing**
- Handled missing values, removed duplicates, and filtered anomalous transactions
- Standardized features for clustering compatibility

**2. Feature Engineering**
- Extracted date-time attributes (month, day-of-week, hour)
- Aggregated transactional data to customer-level RFM metrics

**3. Exploratory Data Analysis (EDA)**
- 10+ visualizations including distribution plots, correlation heatmaps, box plots, and scatter plots
- Identified outliers and behavioral trends across the customer base

**4. K-Means Clustering**
- Determined optimal K=3 using the **Elbow Method** and **Silhouette Scoring**
- Segmented 550,000+ customers into 3 distinct personas

---

## 👥 Customer Segments

| Segment | Recency | Frequency | Monetary | Business Action |
|---|---|---|---|---|
| 🟢 Loyal Customers | Low (recent) | High | High | Retain & Reward |
| 🟡 Potential Customers | Moderate | Moderate | Moderate | Upsell & Nurture |
| 🔴 At-Risk Customers | High (lapsed) | Low | Low | Re-activate & Win Back |

---

## 📊 Key Findings
- **Loyal customers** drive the highest revenue despite being a smaller segment — top priority for retention programs
- **Potential customers** show growing engagement patterns — ideal targets for cross-selling campaigns
- **At-risk customers** have lapsed significantly — require win-back offers and re-engagement strategies
- Feature engineering on date-time variables revealed strong **seasonality patterns** in purchase behavior

---

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core programming language |
| Pandas & NumPy | Data manipulation & feature engineering |
| Scikit-learn | K-Means clustering, preprocessing |
| Matplotlib & Seaborn | Data visualization & EDA |
| Jupyter Notebook | Development environment |

---

## 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/siddharthpurswani/Customer-Segmentation-Case-Study.git

# Navigate to the project directory
cd Customer-Segmentation-Case-Study

# Install dependencies
pip install -r requirements.txt

# Launch the notebook
jupyter notebook Customer_Segmentation_Case_Study.ipynb
```

---

## 📈 Results
- Successfully segmented **550,000+ customers** into **3 actionable clusters** with clear business interpretability
- Enabled marketing teams to shift from broad outreach to **targeted, segment-specific campaigns**
- Surfaced seasonality and behavioral trends through EDA to support **data-driven decision making**

---

## 🙋 Author
**Siddharth Purswani**  
[GitHub](https://github.com/siddharthpurswani) • [LinkedIn](#)
