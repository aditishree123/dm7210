# dm7210
We are updating the Readme file as the project goes on.
In a nutshell, we perform bitcoin price prediction using Bitcoin historical dataset through multiple techniques. Finally, we shall do a comparitive analysis of their performance.

#About the dataset

The dataset that we have used contains information about bitcoin prices from 1/Jan/2012 to 14/Sept/2020. It contains historical bitcoin market data at 1-min intervals for select bitcoin exchanges where trading takes place.The dataset size is 280 MB. The attributes present are:
1. Timestamp: Start time of time window (60s window), in Unix time
2. Open: Open price at start time window
3. High: High price within time window
4. Low: Low price within time window
5. Close: Closing price within time window
6. Volume_(BTC): Volume of BTC transacted in this window
7. Volume_(Currency): Volume of corresponding currency transacted in this window
8. Weighted_price: VWAP- Volume Weighted Average Price

Dataset License: https://creativecommons.org/licenses/by-sa/4.0/

#Steps
1. Download the dataset
2. Import pandas if not already installed, using
    "pip install pandas"
    on certain code editors, if the connection speed is slow, this might give a timeout errror since pandas is a large package. In that case, use
    "pip --default-timeout=1000 install pandas"
3. The data_cleaning.py file will clean the original dataset by removing NaN values and including DataTime in a readable format. It will generate a cleaned_dataset.csv file. Make sure to correctly specify the relative path of the downloaded original dataset.

