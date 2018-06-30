import pandas as pd
import numpy as np

def fileToDataFrame(text_file):
    txt_file = pd.read_csv(text_file,sep='/n',header=None)
    txt_df = txt_file[0].str.split('\t',expand=True)
    return txt_df


def balanceDataset(x_data, y_data, num_of_class):
    '''
    @args:
        x_data: glance sequence
        y_data: label with values from 0 to n
        num_of_class: num of types of label
    Balance the dataset by oversampling classes with smaller dataset
    In the resulting dataset, each class has size equal to the class with the largest dataset
    '''
    # Array with one inner array for each class
    x_train = [[] for i in range(num_of_class)]
    y_train = [[] for i in range(num_of_class)]
    
    # Allocate data according to class
    for i,y in enumerate(y_data):
        x_train[y].append(x_data[i])
        y_train[y].append(y_data[i])
        
    # Get largest class size
    size = max(map(len,y_train))

    # slice_at = int(0.9*len(y_train))
    
    # Oversample smaller classes randomly
    for x,y in zip(x_train,y_train):
        for i in range(size - len(y)):
            num = random.randint(0,len(y)-1)
            x_data.append(x[num])
            y_data.append(y[num])
    
    # Shuffle data before returning to spread the dataset
    shuffles = zip(x_data,y_data)
    random.shuffle(shuffles)
    x_data,y_data = zip(*shuffles)

    return x_data,y_data