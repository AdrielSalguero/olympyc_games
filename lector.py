import pandas as pd
import numpy as np



def reader(route):
    

    df=pd.read_csv(f'{route}',encoding='utf-8')
    return df


def get_list(df,column):

    print_columns(df)
    column_to_list= df[column].tolist()
    #print(f'\n{column_to_list}')
    return(column_to_list)

def print_columns(df):

    column_name= df.columns.values
    print(f' \n{column_name}\n')
    i= int(input('How many columns do you want to show?'))
    try:
        j=0
        columns_list=[]
        while j< i:
            column= input('What column do you want to show?  ')  
            columns_list.append(column)
            j+=1   
        
    except ValueError:
        return ('Error, you have to inserte a int type. Ex> 1,10, 120')
    
    return columns_list

def show_df(df):
    pass




if __name__=='__main__':
    

    route= input('Please copy your path:   ')
    df= reader(route)
    print(f'\n{df}')
    columns_values=(print_columns(df))
    print(get_list(df,columns_values))
