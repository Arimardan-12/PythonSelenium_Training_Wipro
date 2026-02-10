import numpy as np
import pandas as pd
arr=np.array([10,20,30,40,50])

print("array",arr)
print("sum",np.sum(arr))
print("mean",np.mean(arr))
print("max",np.max(arr))


data={
    "Name":["Kiran","Anita","Ravi"],
    "Age":[21,27,29],
    "City":["Banglore","Chennai","Hyderabad"]
}
df=pd.DataFrame(data)
print(df)

print(df["Name"])
print(df[df["Age"]>24])