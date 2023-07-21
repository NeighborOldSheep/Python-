import pdfplumber
import pandas as pd

def read_pdf(read_path,save_path):
    pdf_2020 = pdfplumber.open(read_path)
    result_df = pd.DataFrame()
    for page in pdf_2020.pages:
        table = page.extract_table()
        print(table)
        df_detail = pd.DataFrame(table[1:],columns=table[0])
        result_df = pd.concat([df_detail,result_df],ignore_index=True)
    result_df.dropna(axis=1,how='all',inplace=True)
    