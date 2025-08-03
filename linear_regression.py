import csv
import numpy as np
# Open the CSV file
with open('Salary_Data.csv', mode='r', newline='') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Read the header row (optional)
    header = next(csv_reader)
    print(f"Header: {header}")
    X=[]
    Y=[]
    # Iterate over the remaining rows
    for row in csv_reader:
        X.append(float(row[0]))
        Y.append(float(row[1]))

X=np.array(X)
Y=np.array(Y)

X_m=np.mean(X)
Y_m=np.mean(Y)

X_d=X-X_m
Y_d=Y-Y_m


P=X_d*Y_d   
# print(P)
S=sum(P)

# print(X_d,"\n")
# print(Y_d,"\n")

S_X=np.square(X_d)
S_X=sum(S_X)

m=S/S_X

b=Y_m-(m*X_m)

Y=m*13+b
print(Y)
