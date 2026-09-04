# Step 2 — Data Cleaning Summary
# - No missing values found
# - No duplicate rows found
# - Data types are appropriate
# - No invalid values found in important columns
# - Possible outliers found in absences
import pandas as pd
df = pd.read_csv("../data/student-mat.csv", sep=";")
#print(df["age"].describe())
print(df["age"].value_counts())
