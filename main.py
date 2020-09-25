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

#print(X_train.size)
#print(X_test.size)
#print(X_val.size)

#feature scaling by MinMaxScaler

from sklearn.preprocessing import MinMaxScaler
sc_x = MinMaxScaler()
x_train = sc_x.fit_transform(X_train)
x_test = sc_x.fit_transform(X_test)
x_val = sc_x.fit_transform(X_val)

#column(below code is for plotting of 'Weighted price') plots before and after feature scaling
import matplotlib.pyplot as plt
x=X_train['Weighted_Price'].head(100).tolist()
y=[]
for j in range(100):
    y.append(x_train[j][5])
plt.title('plot for Weighted_Price')
plt.plot(x,'r')
plt.show()
plt.title('plot for Weighted_Price')
plt.plot(y,'b')
plt.show()


#applying linear Regression
lr = LinearRegression()
lr.fit(x_train, Y_train)
print(lr.score(x_test, Y_test))

#Bayesian Ridge regression
from sklearn.linear_model import BayesianRidge
gnb = BayesianRidge()
gnb.fit(x_train, Y_train)
print(gnb.score(x_test,Y_test))
