from sklearn.model_selection import train_test_split
import pandas as pd
btc=pd.read_csv('cleaned_dataset.csv')
features = ['Open', 'High', 'Low', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']
label = 'Close'
#dividing dataset in 70%test,15%train and 15% vlidation
X_train, X_test, Y_train, Y_test = train_test_split(
    btc[features],
    btc[label],
    test_size = 0.15
)
X_train, X_val, Y_train, Y_val = train_test_split(
    btc[features],
    btc[label],
    test_size = 0.15
)

print(X_train.size)
print(X_test.size)
print(X_val.size)