from greet import *
import random 
#import datetime
from datetime import date,datetime

if __name__=="__main__":
    result=random.randint(1,10)
    print(result)
    today_date=date.today()
    current_time=datetime.now()
    print(today_date, current_time)
    hello()
    bye()