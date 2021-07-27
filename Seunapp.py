import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import time
import tkinter as tk
from tkinter import *

##root= Tk()

##df = pd.read_csv("seun.csv",encoding="latin1")

window = tk.Tk()





#RECIEVING THE DATA FROM THE GOOGLE SHEET
pd.set_option('display.max_rows', None)

def execute_csv(df, pd, np, date, datetime, time ):     
    # COLLECTING THE INPUTTED PAID SERVICE CHARGE FROM THEIR DIFFERENT YEARS
    df['2019/2020'] = df['2019/2020'].fillna(0)#fill Nan with 0 values
    df['2019/2020']= pd.to_numeric(df['2019/2020'], errors='coerce')
    #print('2019/2020\n',df['2019/2020'])
    
    df['2020/2021'] = df['2020/2021'].fillna(0)
    df['2020/2021']= pd.to_numeric(df['2020/2021'], errors='coerce')
    ##print('2020/2021\n',df['2020/2021'])

    df['2021/2022'] = df['2021/2022'].fillna(0)
    df['2021/2022']= pd.to_numeric(df['2021/2022'], errors='coerce')
    ##print('2021/2022\n',df['2021/2022'])

    Servicecharge_2019= df['2019/2020']
    Servicecharge_2020= df['2020/2021']
    Servicecharge_2021= df['2021/2022']
    paid_servicecharge= Servicecharge_2019+Servicecharge_2020+Servicecharge_2021
    #print("Paid service charge\n",paid_servicecharge)

##    print(df['DATE OF POSSESSION'].dtype)
    ## TURNING THE DATE OF POSSESSION INTO A DATE TIME COLUMN 
    df['DATE OF POSSESSION'] = pd.to_datetime(df['DATE OF POSSESSION'])
    dates = df["DATE OF POSSESSION"]
    dates.dropna(inplace = True)

    ##print(type(dates.astype('float')))
    #print(dates)

    ## EXTRACTING THE YEAR, MONTH AND DAYS OF THE DATE OF POSSESSION COLUMNS
    year =df['DATE OF POSSESSION'].dt.year
    pd.to_numeric(year, errors='coerce')
    ##year = year.apply(lambda x: x.value)
    day= df['DATE OF POSSESSION'].dt.day
##    print('day', day)
    month = df['DATE OF POSSESSION'].dt.month
##    print('month', month)

    ## ALGORITHM FOR THE CALCULATION OF THE SERVICE CHARGE AMOUNT OWING
    amount_to_pay_for_May2019_and_below= 300000
    amount_to_pay_for_May2020_and_above= 200000
    amount_paidthatyear=((abs(month-5))*(100000/12))
##    print(amount_paidthatyear)
    amount_owedfornextyear= ((12-(month-5))*(100000/12))
##    print('amount_owedfornextyear\n',amount_owedfornextyear)


    amount_owed_for_May2019_and_below= (amount_to_pay_for_May2019_and_below)-(paid_servicecharge)
    rounded_amount_1= round(amount_owed_for_May2019_and_below, 2)
##    print('round amount for those that came from 2019 and below\n',rounded_amount_1)


    amount_owed_for_May2020_and_above= (amount_to_pay_for_May2020_and_above) - (amount_paidthatyear)
    rounded_amount_2= round(amount_owed_for_May2020_and_above, 2)
##    print('round amount for those that came from 2020 and above\n',rounded_amount_2)



    amount_really_owing = round((amount_owedfornextyear+200000)-paid_servicecharge)
    amount_really_owing2 = round((amount_owedfornextyear+100000)-paid_servicecharge)
    amount_really_owing3 = round((amount_owedfornextyear)-paid_servicecharge)

##    print('what they are really owing\n',amount_really_owing2)

    ## TRYING TO SAVE IT TO FILE WHEN DONE, TEST RUN OF IT
    df.to_csv("seun.csv", index=False)
##    print(df[df['DATE OF POSSESSION'].notnull()])

        

    day = df['DATE OF POSSESSION'].dt.day

    df.set_index('DATE OF POSSESSION', inplace=True, drop=False)

    date2022 = pd.to_datetime('2022-05-01').value
    date2021 = pd.to_datetime('2021-05-01').value
    date2020 = pd.to_datetime('2020-05-01').value
    date2019 = pd.to_datetime('2019-05-01').value
##    print('date 2022\n',date2022)


    df['DATE OF POSSESSION'] = pd.to_datetime(df['DATE OF POSSESSION'], format='%m/%d/%Y')
    ##year= df['year']

    ##print(df.loc[4, '2019/2020'])

    #dates= dates.values.astype("float")
##    print(dates.dtype)
    asf = dates.values.astype("int64")
##    print('dateeeeee',type(asf))
##    print(asf.dtype)
##    print(type(year))

    ##dates= str(dates)    ##tried converting the datetime value to string and compare then like this dates >= '01-05-2019' but it didnt work
    ##print(type(dates))   ##so i will try to convert them to date time date time to compare them
##    print(type(pd.to_datetime(dates)))
##    print(type(date2020))

    ##df['Amount Owing'] = np.where(asf >= date2019, amount_really_owing,
    ##                     np.where(asf >= date2020, amount_really_owing2,amount_really_owing3))
    ##print(df)

    ##TRY TO LEARN NP.WHERE WELL AND STRUCTURE THE CODE ABOVE WELL
    


    conditions = [
        np.logical_and(np.logical_and(df['2019/2020'] != 0, df['2020/2021']== 0), df['2021/2022']== 0),
        np.logical_and(np.logical_and(df['2019/2020'] != 0, df['2020/2021']!= 0), df['2021/2022']!= 0),
        np.logical_and(np.logical_and(df['2019/2020'] != 0, df['2020/2021']!= 0), df['2021/2022']== 0),
        np.logical_and(np.logical_and(df['2019/2020'] != 0, df['2020/2021']== 0), df['2021/2022']!= 0),
        np.logical_and(np.logical_and(df['2019/2020'] == 0, df['2020/2021']== 0), df['2021/2022']== 0),
        np.logical_and(np.logical_and(df['2019/2020'] == 0, df['2020/2021']!= 0), df['2021/2022']!= 0),
        np.logical_and(np.logical_and(df['2019/2020'] == 0, df['2020/2021']!= 0), df['2021/2022']== 0),
        np.logical_and(np.logical_and(df['2019/2020'] == 0, df['2020/2021']== 0), df['2021/2022']!= 0),
        ]    

    choices = [
        amount_really_owing,
        amount_really_owing,
        amount_really_owing,
        amount_really_owing,
        amount_really_owing,
        amount_really_owing2,
        amount_really_owing2,
        amount_really_owing3,
        ]


    df['Amount Owing'] = np.select(conditions, choices)
##    print(df)

##    df['PLOT'] = df['PLOT'].astype(str)
    search_result= df[df['Amount Owing'] == plot_number_var.get()]
    df.set_index('PLOT NUMBER', inplace=True, drop=False), #ignore the cell's value is Nancase=False)] 
    


    t1.insert(tk.END,  search_result)
    








sheets = ["VINCENT%20AZIKE%20STREET", "PAUL%20ODILI%20CRESCENT", "O%20SEYI%20KEHINDE%20CLOSE", "JOHN%20ODIGIE%20OYEGUN%20STREET", "IDRIS%20KPOTUN%20DRIVE", "IDUMU%20UWALA%20STREET", "DR%20JONATHAN%20ABIODUN%20STREET", "KPRC%20CO-OP%20STREET", "SAMUEL%20NLEMOHA%20STREET", "DR%20IFEANYI%20OKOWA%20STREET", "GOLF%20CLOSE", "LAWRENCE%20NWABUNOR%20STREET", "JOAO%20MONTERO%20STREET", "IMIKE%20ABO%20STREET", "BISHOP%20NICHOLAS%20OKOH%20STREET", "ADRIAN%20OGUN%20STREET", "AKIN%20MOGOGUNJE%20BOULEVARD%20STREET", "BABATUNDE%20FOLAWIYO%20STREET", "JEFF%20GOLDWAY%20STREET", "COLLINS%20WATERTON%20STREET", "KOLAKPO%20CLOSE", "NWAEFUNE%20OSAJI%20STREET", "JOHN%20TOWNLEY%20JOHNSON%20STREET", "RENI%20ADEGBITE%20STREET", "BISHOP%20ABIOYE%20STREET", "OLUSEGUN%20OBASANJO%20STREET"]
# Fill up the array yourself

for sheet in sheets:
    googleSheetId = '1jfHra1V_d4BL5TN1MKqAJTQuspF0F--Aoas7XSjEEd0'
    worksheetName = sheet#'PAUL%20ODILI%20CRESCENT'#'VINCENT%20AZIKE%20STREET' #'CLUSTER%201%20STREET%20BY%20STREET'
    URL= 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
            googleSheetId,
            worksheetName,

            )
    df = pd.read_csv(URL, thousands=',', index_col=False, parse_dates=["DATE OF POSSESSION"])

##    print(df.to_string())

    # THE GUI    


    #creating the entry widgets to collect enteries of the plot numbers
    plot_number_var = tk.StringVar()
    ##plot_name_var = tk.StringVar()

    e1 = tk.Entry(window, textvariable=plot_number_var)
    e1.grid(row=0,column=0)
    e1.bind("<Return>", execute_csv) 

    #Creates a text box
    t1=tk.Text(window,height=80,width=80)
    t1.grid(row=0,column=2)
         
      
    #Creates a button
    b1=tk.Button(window,width=10,text='search',command=execute_csv)

    b1.grid(row=0,column=1)

    execute_csv( df, pd, np, date, datetime, time)  






window.mainloop()
