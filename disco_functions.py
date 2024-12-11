import pandas as pd


def remove_identifiers(df_in):
    df_out = df_in.copy()
    df_out = df_in.drop(columns=['Name', 'National Insurance Number'])
    return df_out


def change_age(df_in):
    df_out = df_in.copy()
    widowed_un25a = df_out[(df_out['Age']<=25) & (df_out['Marital Status']=='Widowed')]
    df_out.loc[widowed_un25a.index, 'Age'] = 25
    return df_out


def new_marital(df_in):
    df_out = df_in.copy()
    marital_dict = {'Married':True, 'Single':False, 'Widowed':False}
    df_out['Is Married'] = df_out['Marital Status'].map(marital_dict) 
    return df_out.drop(columns=['Marital Status'])


def new_age(df_in):
    df_out = df_in.copy()
    under25 = df_out[(df_out['Age']<=25)]
    df_out.loc[under25.index, 'Age'] = '<=25'
    return df_out

