import fitz 
import pandas as pd
# pdf_file1=r'C:\Users\sonde\OneDrive\Desktop\Flask_App_Demo-main (1)\Flask_App_Demo-main\flask_tutorial\pdf_file1.pdf'
# doc=fitz.open(pdf_file1)
# a=pd.DataFrame()
# tables=[]
# for i in range(0,doc.page_count):
#     page=doc[i]
#     t=page.find_tables()
#     a=pd.concat([a,t[0].to_pandas()])
# a.to_csv("file1.csv",index=False)

pdf_file2=r'C:\Users\sonde\OneDrive\Desktop\Flask_App_Demo-main (1)\Flask_App_Demo-main\flask_tutorial\pdf_file2.pdf'
doc2=fitz.open(pdf_file2)
b=pd.DataFrame()
tables=[]
for i in range(0,doc2.page_count):
    page=doc2[i]
    t=page.find_tables()
    b=pd.concat([b,t[0].to_pandas()])
b.to_csv("file2.csv",index=False)