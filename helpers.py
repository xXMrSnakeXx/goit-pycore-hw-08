import datetime as dt
from datetime import datetime as dtdt

def get_upcoming_birthdays(user):
    dateNow = dtdt.today().date()
    birthday = user["birthday"]
    birthday = birthday[:6] + str(dateNow.year)
    birthday_this_year = dtdt.strptime(birthday, "%d.%m.%Y").date() 
    if birthday_this_year < dateNow:
           birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year +1) 
           return get_birthday_on_week(birthday_this_year, dateNow, user)
    else :
           return get_birthday_on_week(birthday_this_year, dateNow, user)   

def get_birthday_on_week(birthday_this_year, dateNow, user):
    differenceDays = (birthday_this_year - dateNow).days
    weekDay = birthday_this_year.isoweekday()
    if 0<=differenceDays<7  or differenceDays>0:
        if weekDay<6:
            return f"{user["name"]} need to say happy birthday {birthday_this_year.strftime("%d.%m.%Y")}"
        else :
            if (birthday_this_year + dt.timedelta(days=1)).weekday()==0 :
                return f"{user["name"]} need to say happy birthday {(birthday_this_year + dt.timedelta(days=1)).strftime("%d.%m.%Y")}"
            elif (birthday_this_year+dt.timedelta(days=2)).weekday()==0:
                return f"{user["name"]} need to say happy birthday {(birthday_this_year + dt.timedelta(days=2)).strftime("%d.%m.%Y")}"

