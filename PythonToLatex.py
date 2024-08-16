import pandas as pd

def dataframe_to_latex_table(df,include_column_names=True,align='c'):
    '''
    This function receives a pandas dataframe and returns the latex code for a 
    table containing the information stored in the dataframe.
    '''
    num_cols = df.shape[1]
    assert align in ['c','l','r'] 
    num_columns_str = '|' + num_cols*(align+'|')
    table_body_script = ""
    for j in df.index.to_list():
        row = str(df.iloc[j,0])
        for col_name in df.columns.to_list()[1:]:
            row += " & " + str(df.loc[j,col_name])
        row += "\\\\ \\hline"
        table_body_script += row + "\n" 
    if include_column_names:
        col_names = df.columns.to_list()
        header_text = str(col_names[0])
        for x in col_names[1:]:
            header_text += " & " + str(x)
        header_text += "\\\\ \\hline"
        script = f'''\\begin{{table}}[h]
        \\centering
        \\begin{{tabular}}{{{num_columns_str}}}
            {header_text}
            {table_body_script}\\end{{tabular}}
        \\end{{table}}
        '''
    else:
        script = f'''\\begin{{table}}[h]
        \\centering
        \\begin{{tabular}}{{{num_columns_str}}}\\hline
            {table_body_script}\\end{{tabular}}
        \\end{{table}}
        '''
    return script
