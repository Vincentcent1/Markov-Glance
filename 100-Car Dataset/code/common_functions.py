import pandas as pd
import numpy as np

def fileToDataFrame(text_file):
    txt_file = pd.read_csv(text_file,sep='/n',header=None)
    txt_df = txt_file[0].str.split('\t',expand=True)
    return txt_df
