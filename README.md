# dm7210
We are updating the Readme file as the project goes on

1. Download the dataset
2. Import pandas if not already installed, using
    "pip install pandas"
    on certain code editors, if the connection speed is slow, this might give a timeout errror since pandas is a large package. In that case, use
    "pip --default-timeout=1000 install pandas"
3. The data_cleaning.py file will clean the original dataset by removing NaN values and including DataTime in a readable format. It will generate a cleaned_dataset.csv file. Make sure to correctly specify the relative path of the downloaded original dataset.
4. The next step is to split the dataset into training and testing data: 60% training data, 20% cross validation data and 20% testing data.
5. And then training the data on different models used in classifier.py file.
6. The file classifier.py contains code for data splitting, the models and performance measures. To run this file, install sklearn python library using "pip install sklearn".
