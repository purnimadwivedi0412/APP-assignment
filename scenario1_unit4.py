
import numpy as np
import pandas as pd

bills = np.array([1500, 2500, 3500, 4200, 2800])

print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

data = {
    'Consumer': ['Aarav', 'Bhavna', 'Chetan', 'Diya', 'Esha'],
    'Bill Amount': bills
}

df = pd.DataFrame(data)

print("\nElectricity Bill Details:")
print(df)


print("\nConsumers with bills above Rs. 3000:")
print(df[df['Bill Amount'] > 3000])

OUTPT
Mean Bill: 2900.0
Median Bill: 2800.0
Maximum Bill: 4200
Minimum Bill: 1500

Electricity Bill Details:
  Consumer  Bill Amount
0    Aarav         1500
1   Bhavna         2500
2   Chetan         3500
3      Diya         4200
4      Esha         2800

Consumers with bills above Rs. 3000:
  Consumer  Bill Amount
2   Chetan         3500
3      Diya         4200