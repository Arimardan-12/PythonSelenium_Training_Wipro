import pandas as pd
import numpy as np
students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78},
    {"name": "David", "score": 90},
    {"name": "Eva", "score": 88}
]

df = pd.DataFrame(students)
print(df)
mean_score = np.mean(df['score'])
median_score = np.median(df['score'])
std_score = np.std(df['score'], ddof=0) 

print("Mean:", mean_score)
print("Median:", median_score)
print("Standard Deviation:", std_score)

df['above_average'] = df['score'] > mean_score
print(df)
