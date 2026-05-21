## Plantilla de README

1) Objective
   
- Data analysis and visualization of a dataset containing information about reviews published on Booking.com. The dataset includes 515,000 reviews and customer scores from 1,493 luxury hotels across Europe.
- The objective of this study is to analyze how the customer's nationality influences their perception of hotel service, evaluating both numerical scores and complaint patterns across different seasons of the year.

2) Dataset
  - Source: A CSV file titled "515K Hotel Reviews Data in Europe", uploaded to Kaggle by the user Jiashen Liu.
- No. of rows/columns: The file contains 17 columns and 515,738 rows.
- Key variables: Numerical and categorical columns generated for analysis, which include:
    Review_Date (categorical): The date when the customer wrote the review.
    Reviewer_Nationality (categorical): The nationality of the customer writing the review.
    Review_Total_Negative_Word_Counts (numerical): The total number of words in a negative review.
    Reviewer_Score (numerical): The final score awarded to the hotel by the customer.
    Month (numerical/temporal): A feature generated from Review_Date to group data on a monthly basis.
    Negative_Review_Clean (text): Standardized negative review in lowercase and filtered to remove noise.

3) Questions
- Q1: How is the data distributed after cleaning?

    The data distribution undergoes a significant change that improves the quality of the analysis, given that the original dataset suffers from a major bias due to automated responses—specifically, the text "No          Negative". These records have been removed to focus exclusively on actual complaints.

- Q2: What new features can be derived?

    The temporal feature Month has been created, allowing data grouping and seasonality studies.

    Negative_Review_Clean has also been generated, capturing standardized negative reviews free of text noise.

- Q3: What insights are obtained from the visualizations?

    - 1st insight: Frustration levels can be measured through complaint volume (Scatterplot). It has been demonstrated that the more dissatisfied a customer is with their hotel experience, the higher the word count of the review. Dissatisfied customers want to detail every issue they encountered.

    - 2nd insight: Negative hotel reviews spike during the summer (Line chart). This could be due to operational saturation, as hotels are more crowded, driving up customer dissatisfaction. Key terms isolated in this insight include small rooms, breakfast, and check (the most repeated words in negative reviews).

    - 3rd insight: Cultural shock and seasonality intersect (Heatmap). The heatmap reveals that dissatisfaction has strongly defined geographical and temporal components. Middle Eastern customers (UAE and Saudi Arabia) are the strictest, recording their lowest average scores in July and October (hitting a minimum of 7.69), which contrasts sharply with the American profile, which maintains optimal scores (close to 8.80) year-round.

4) Data issues & fixes
- Missing values ➔ Cleaning and imputation in src/cleaning.py

  The 'Negative_Review' column contained thousands of records where the user had no actual complaint, which were automatically filled by the platform with the text 'No Negative', creating a massive bias in the analysis.

  The solution was to apply a filter to ignore these rows when analyzing review keywords, ensuring we only work with complaints that hold real semantic value.

- Inconsistent data ➔ Normalization and correction

  The review text presented common typographical inconsistencies (mixed casing, whitespaces, and meaningless filler words).

  This was normalized by converting all text strings to lowercase and stripping whitespaces. Additionally, a regular expression filter using re.findall was paired with a custom stopword list to isolate only             operationally meaningful keywords.

- Incorrect formats ➔ Data type conversion

  The Review_Date variable was parsed by default as a generic data type, making chronological operations or temporal groupings impossible.

  An explicit conversion of the column to a datetime format was performed. Following this adjustment, the Month variable was created, enabling the generation of the time-series charts.

5) Pipeline
[ Original Dataset: Hotel_Reviews.csv ] (data/raw)
                  │
                  ▼
         1. CLEANING PHASE 
          (src/cleaning.py)
                  │
                  ▼
      2. ANALYSIS & SCRIPT PHASE
             (main.py)
                  │
                  ▼
        3. OUTPUT GENERATION PHASE 
            
6) Findings
Through Exploratory Data Analysis (EDA) and the applied text mining techniques, the following three main findings have been consolidated:

- Insight 1: Complaint volume betrays the frustration level

    Evidence: Scatterplot of Complaint Length vs. Score.

    Conclusion: There is a clear asymmetry in consumer behavior. While short reviews (under 100 words) are spread across the entire scoring spectrum, extremely long reviews (200 to 400 words) concentrate almost exclusively on scores below 6. This proves that the text volume of a complaint is a direct indicator of customer frustration: the worse the experience, the greater the need to vent.

- Insight 2: Seasonality hides operational stress spikes

    Evidence: Line Chart (Temporal Trend) of monthly review volume.

    Conclusion: Review volume is not constant; it shows two massive spikes: the first one in May and the highest in August (exceeding 50,000 reviews). However, the most interesting finding is the rebound in October (nearly 44,000 reviews)—a month theoretically considered "low season" that, by oversaturating hotels that have already reduced staff for autumn, triggers operational bottlenecks.

- Insight 3: Cultural shock and business vulnerability in summer

    Evidence: Heatmap by Nationality/Month and Summer Bar Chart.

    Conclusion: Visualizations reveal that dissatisfaction is highly segmented. Middle Eastern tourists (UAE and Saudi Arabia) are the strictest in the dataset, registering their lowest scores in July and October (minima of 7.69), contrasting with the American profile, which consistently scores high (close to 8.80). Cross-referencing this with the July/August bar chart, we discover that the root cause of summer dissatisfaction is not the hotel itself, but overcrowding: the main complaints center on room size (small), breakfast queues (breakfast), and wait times at check-in (check).

7) Project structure
The project is modularly structured following software engineering and data science best practices. Files are organized as follows:



```
project/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt

```
