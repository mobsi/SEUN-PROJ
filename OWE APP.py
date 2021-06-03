import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime

pd.set_option('display.max_rows', None)
##df = pd.read_csv('seun.csv')
googleSheetId = '1jfHra1V_d4BL5TN1MKqAJTQuspF0F--Aoas7XSjEEd0'
worksheetName = 'CLUSTER%201%20STREET%20BY%20STREET'
URL= 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
        googleSheetId,
        worksheetName
        )
df = pd.read_csv(URL, thousands=',')
##df = pd.read_csv('seun.csv',parse_date,s=['DATE OF POSSESSION'],  dayfirst=True)
##https://docs.google.com/spreadsheets/d/{0}/GVIZ/tq?tqx=out:csv&sheet={1}.format()
##import requests
##import pandas as pd
##
##r = requests.get('https://docs.google.com/spreadsheets/d/1jfHra1V_d4BL5TN1MKqAJTQuspF0F--Aoas7XSjEEd0/edit?usp=sharing&output=csv')
##data = r.content


print(df.to_string()) 

##a= int(df.loc[36, '2019/2020'])
##b= int(df.loc[37, '2020/2021'])
##c= int(a)
##d= int(b)
##print(a*b)
##e= df.loc[24, 'DATE OF POSSESSION']
##print(e)



df['2019/2020'] = df['2019/2020'].fillna(0)#fill Nan with 0 values
df['2019/2020']= pd.to_numeric(df['2019/2020'], errors='coerce')
print('2019/2020\n',df['2019/2020'])

df['2020/2021'] = df['2020/2021'].fillna(0)
df['2020/2021']= pd.to_numeric(df['2020/2021'], errors='coerce')
print('2020/2021\n',df['2020/2021'])

df['2021/2022'] = df['2021/2022'].fillna(0)
df['2021/2022']= pd.to_numeric(df['2021/2022'], errors='coerce')
print('2021/2022\n',df['2021/2022'])

Servicecharge_2019= df['2019/2020']
Servicecharge_2020= df['2020/2021']
Servicecharge_2021= df['2021/2022']
paid_servicecharge= Servicecharge_2019+Servicecharge_2020+Servicecharge_2021
print("Paid service charge\n",paid_servicecharge)



##df['2019/2020'].replace('', np.nan, inplace=True)
##df.dropna(subset=['2019/2020'], inplace=True)
##print(df.dtypes)

##p= df.loc[36, '2019/2020']
##q= df.loc[37, '2019/2020']
##
##g= df.loc[268, '2020/2021']

##print(g)
##print(p)

##print(d)
##print(df.info())
df['DATE OF POSSESSION'] = pd.DatetimeIndex(df['DATE OF POSSESSION'])
dates = df["DATE OF POSSESSION"]
##print(df['DATE OF POSSESSION'].dt.strftime("%Y%m%d").astype(int))
##df['DATE OF POSSESSION'] = df['DATE OF POSSESSION'].dt.strftime('%Y%m%d')


##dateslist = list(dates)
print(dates)

df['year'] =df['DATE OF POSSESSION'].dt.year
print(df['year'])
day= df['DATE OF POSSESSION'].dt.day
print(day)
month = df['DATE OF POSSESSION'].dt.month
print(month)
amount_to_pay_for_May2019_and_below= 300000
amount_to_pay_for_May2020_and_above= 200000
amount_paidthatyear=((abs(month-5))*(100000/12))
print(amount_paidthatyear)
amount_owedfornextyear= ((12-(month-5))*(100000/12))
print('amount_owedfornextyear\n',amount_owedfornextyear)


amount_owed_for_May2019_and_below= (amount_to_pay_for_May2019_and_below)-(paid_servicecharge)
rounded_amount_1= round(amount_owed_for_May2019_and_below, 2)
print('round amount for those that came from 2019 and below\n',rounded_amount_1)


amount_owed_for_May2020_and_above= (amount_to_pay_for_May2020_and_above) - (amount_paidthatyear)
rounded_amount_2= round(amount_owed_for_May2020_and_above, 2)
print('round amount for those that came from 2020 and above\n',rounded_amount_2)



amount_really_owing = round((amount_owedfornextyear+200000)-paid_servicecharge)
amount_really_owing1 = round((amount_owedfornextyear+200000)-paid_servicecharge)
amount_really_owing2 = round((amount_owedfornextyear+100000)-paid_servicecharge)
amount_really_owing3 = round((amount_owedfornextyear)-paid_servicecharge)

print('what they are really owing\n',amount_really_owing2)
##df["Amount Owed"]= rounded_amount
df.to_csv("seun.csv", index=False)
print(df[df['DATE OF POSSESSION'].notnull()])
##    dateamount= 300000-(paid_servicecharge)
##    rounded_dateamount= round(dateamount, 2)
##    print(rounded_dateamount)
    

##df['Month'] = pd.DatetimeIndex(df['DATE OF POSSESSION']).month  its the same thing as the month variable above
##print(df['Month'])
day = df['DATE OF POSSESSION'].dt.day

df.set_index('DATE OF POSSESSION', inplace=True, drop=False)
## When you set date as index, by default it removes the date column from your dataframe, that's why you got the error saying Date not in index(index here refers to the columns).
##By using the drop=False parameter, it tells pandas to keep the date filed when setting date as index


##print(df.loc['2019-05-01'])
##print(df.loc[df['DATE OF POSSESSION'] <= '2019-05-01'] == 'True')

##print(df.loc[df['year'] == 2020])
date2022 = datetime.strptime('2022-05-01', '%Y-%m-%d')
date2021 = datetime.strptime('2021-05-01', '%Y-%m-%d')
date2020 = datetime.strptime('2020-05-01', '%Y-%m-%d')
date2019 = datetime.strptime('2019-05-01', '%Y-%m-%d')
print('date 2022\n',date2022)
print(date2022)
print(pd.to_numeric(date2022, errors='coerce'))

##mask = (df['DATE OF POSSESSION'] >= date2020) & (df['DATE OF POSSESSION'] <= date2021)
##print(df.loc[mask],round((amount_owedfornextyear+100000)-paid_servicecharge),0)

mask = (df['year']>= 2019) & (df['year'] <= 2020)
print(df.loc[mask])

print(df['DATE OF POSSESSION'])
print(df['year'].loc)

##ma= (df['DATE OF POSSESSION'] >= date2019) & (df['DATE OF POSSESSION'] < date2020)

##temp = df['year'].fillna("0")
##df['Activity_2'] = pd.np.where(temp.str.contains("0"),amount_really_owing1,
##                   pd.np.where(temp.str.contains("2017"),amount_really_owing1,
##                   pd.np.where(temp.str.contains("2018"),amount_really_owing1,
##                   pd.np.where(temp.str.contains("2019"),amount_really_owing1,
##                   pd.np.where(temp.str.contains("2020"),amount_really_owing2,
##                   pd.np.where(temp.str.contains("2021"),amount_really_owing,amount_really_owing))))))
##                    



if (df['2019/2020']== 0).any() | (df['2020/2021']!=0).any() | (df['2021/2022']!=0).any():
    print(amount_really_owing2)
    if (df['2019/2020']!= 0).any() | (df['2020/2021']==0).any() | (df['2021/2022']==0).any():
        print(amount_really_owing1)
        if (df['2019/2020']!= 0).any() | (df['2020/2021']!=0).any() | (df['2021/2022']==0).any():
            print(amount_really_owing1)
            if (df['2019/2020']== 0).any() | (df['2020/2021']==0).any() | (df['2021/2022']!=0).any():
                print(amount_really_owing3)
                if (df['2019/2020']== 0).any() | (df['2020/2021']!=0).any() | (df['2021/2022']==0).any():
                    print(amount_really_owing2)
                    if (df['2019/2020']!= 0).any() | (df['2020/2021']==0).any() | (df['2021/2022']!=0).any():
                        print(amount_really_owing)
                        if (df['2019/2020']== 0).any() | (df['2020/2021']==0).any() | (df['2021/2022']==0).any():
                            print(amount_really_owing1)
                            if (df['2019/2020']!= 0).any() | (df['2020/2021']!=0).any() | (df['2021/2022']!=0).any():
                                print(amount_really_owing1)
else:
    print(amount_really_owing1)




##def owefunc(df):
##    if(df['DATE OF POSSESSION'] >= date2020):
##       return(round((amount_owedfornextyear+100000)-paid_servicecharge),0)
##    elif(df['DATE OF POSSESSION'] >= date2020 <= date2022 ):
##        return('what they are really owing\n',round((amount_owedfornextyear+100000)-paid_servicecharge),0)
##    elif(df['DATE OF POSSESSION'] >= date2021 <= date2022 ):
##        return('what they are really owing\n',round((amount_owedfornextyear)-paid_servicecharge),0)
##def owefunc(df):
##    if(df['DATE OF POSSESSION'] <= "2022-05-01") and (df['DATE OF POSSESSION'] >= "2019-05-01"):
##       return (amount_paidthatyear+200,000)
##    elif(df['DATE OF POSSESSION'] <= "2022-05-01"  >= "2020-05-01"):
##        return (amount_paidthatyear+100,000) 
##    elif(df['DATE OF POSSESSION'] <= "2022-05-01"  >= "2021-05-01"):
##        return (amount_paidthatyear)
    
##df['Amount Owing'] = df.apply(owefunc)
##df['Amount Owing'] = np.where(dates <="2019-05-01",rounded_amount_1, rounded_amount_2)
##df['Amount Owing'] = np.where(dates >="2020-05-01",rounded_amount_2, rounded_amount_1)
##df['Amount Owing']= ["yeah" if df['year'].any() == 2020 else "nah" for year in dates]
##df['Amount Owing']= ["yeah" if date<= '2019-05-01' else 'nah' if date >= '2020-05-01' for year in dates]

print(df)
print('seun',df['year'])

year =df['DATE OF POSSESSION'].dt.year

year2020= df.loc[year >= 2020]

n= amount_really_owing1
while df.loc[year <= 2022]:
    n= n-100000
    year += 1
    print(n)
##df.index.date == date(2019, 4, 1)
##df.index[df.index.date == date(2019, 4,1)].max()
##df.loc[df.index[df.index.date == date(2019, 4,1)].max()]
##print(df.loc[df.index[df.index.date == date(2019, 4,1)].max()].xs('NAME', axis=0))


##    print(df.loc[df.index[df.index.date == date(2019, 4,1)].max()].xs('S/NO', axis=0))
#.xs('ALLOTTEES NAME', axis=0)) allows you to write the string header as it is

##for i in date:
##    if i =='2019-04-01':
##        print((df.loc['2020-04-01'])+"This person owes 66,666.67")
##        print(date)



##for i in date:
##    print(df.loc[i])
