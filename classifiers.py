from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LinearRegression

btc=pd.read_csv('cleaned_dataset.csv')
features = ['Open', 'High', 'Low', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price']
label = 'Close'
#dividing dataset in 60%test,20%train and 20% vlidation
X_train, X_test, Y_train, Y_test = train_test_split(
    btc[features],
    btc[label],
    test_size = 0.40
)
X_test, X_val, Y_test, Y_val = train_test_split(
    btc[features],
    btc[label],
    test_size = 0.50
)

print(X_train.size)
print(X_test.size)
print(X_val.size)

#applying linear Regression
lr = LinearRegression()
lr.fit(X_train, Y_train)
print(lr.score(X_test, Y_test))

#Bayesian Ridge regression
from sklearn.linear_model import BayesianRidge
gnb = BayesianRidge()
gnb.fit(X_train, Y_train)
print(gnb.score(X_test,Y_test))
