from datetime import date
import date
import csv
import datetime
import calendar
from dateutil import parser

def generateDate():
    mydate = parser.parse('Aug 01 2015')
    record = 0
    final_date = []
    while(record < 365):
        final_date = []
        mydate = mydate + datetime.timedelta(days = 1)
        day = calendar.day_name[mydate.weekday()]
        weekNumber = mydate.isocalendar()[1]
        print(mydate, weekNumber, day)
        dt= mydate.strftime('%d-%m-%Y')
        date_s = dt.split('-')
        month = date_s[1]
        year = date_s[2]
        if(int(month) <= 6):
            sem = 'Even'
        elif(int(month) > 6):
            sem = 'Odd'
        if(day == 'Sunday'):
            isHoliday = 'True'
        else:
            isHoliday = 'False'
        final_date.append(mydate)
        final_date.append(day)
        final_date.append(weekNumber)
        final_date.append(month)
        final_date.append(year)
        final_date.append(sem)
        final_date.append(isHoliday)
        with open('dates.csv', 'a+') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(final_date)
            f.close()
        with open('dates.csv', 'a+') as f1:
            writer = csv.writer(f1, delimiter=',')
            writer.writerow(final_date)
            f1.close()
        record = record + 1



if __name__ == '__main__':
    generateDate()