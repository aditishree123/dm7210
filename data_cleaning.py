import pandas as pd

if __name__ == '__main__':
    #put relative location of dataset here
    data = pd.read_csv("./venv/btc_dataset.csv")

    #Data Cleaning
    DF = pd.DataFrame(data)
    
    #Percentage of rows having NULL values
    print("Percentage of NULL values in each column:")
    print(DF.isnull().mean()*100)
    #Count of rows having no NULL values
    print("Count of non NULL values in each column:")
    print(DF.count())
    
    #Dropping NaN value Tuples
    DF.dropna(axis=0, how='any', thresh=None, subset=None, inplace=True)
    
    #Converting UNIX timestamp to date and time format
    DF['dateTime'] = pd.to_datetime(DF['Timestamp'], unit='s')
    DF.to_csv('cleaned_dataset.csv')
