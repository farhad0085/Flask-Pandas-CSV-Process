import pandas as pd

def csv_processing(file1 ='report.xlsx'):

    
    df_dict = pd.read_excel(file1, header=[0,1], sheet_name='DataSet')
    df_dict.columns = df_dict.columns.map('-'.join)
    df2=pd.melt(df_dict,id_vars=[df_dict.columns[0]],var_name='metrics', value_name='values')
    Open_end =[]
    for i in df_dict.columns:
        if (len(df2['values'][df2.metrics ==i].unique())) > 10:
            Open_end.append(i)
        
    df3 = pd.DataFrame()
    df3['Open Ended Questions'] = Open_end

    return df3

if __name__ == "__main__":
    csv_processing()