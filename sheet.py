import os
currDirectory = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(currDirectory)

from datetime import datetime  as dt
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(currDirectory + '\\google_sheet_info.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("Monies").sheet1


name_to_col = {'Date':1,
               'For':2,
               'To': 3,
               'Woocheol':4,
               'Nick':5,
               'Daniel':6,
               'Patrick': 7,
               'Max': 8,
               'Ajay':9,
               'Caitlin':10,
               'Alex':11,
               'amount':12}

def get_next(name):
    num_rows = len(wks.col_values(name_to_col['Date']))
    
    for row_num in range(2, num_rows+1):
        row_values = wks.row_values(row_num)
        date_str = row_values[name_to_col['Date']-1]
        due_date = dt.strptime(date_str, "%m/%d/%Y").date()
        today = dt.now().date()
        if due_date >= today:
            amount_due= row_values[name_to_col['amount']-1]
            payed = row_values[name_to_col[name]-1]
            to = row_values[name_to_col['To']-1]
            for_ = row_values[name_to_col['For']-1]
            if payed != amount_due:
                text = "You owe $" + str(int(amount_due) - int(payed)) + " on " + \
                        dt.strftime(due_date, "%m/%d") + \
                        " to " + to + " for the " + for_ + "."
                return text

    else:
        return "You currently owe nothing"
    
















