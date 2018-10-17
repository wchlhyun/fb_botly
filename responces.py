from selenium.webdriver.common.keys import Keys
import time

import sheet

names = set(['@Woocheol',
       '@Nick',
       '@Daniel',
       '@Patrick',
       '@Max',
       '@Ajay',
       '@Caitlin',
       '@Alex'])

def respond(driver, at, text):
    sender = driver.find_element_by_xpath("//div[@role='combobox']")
    sender.send_keys('@' + at)
    time.sleep(0.2)
    sender.send_keys(Keys.TAB)
    sender.send_keys(" ")
    
    splits = text.split('\n')
    for split in splits:
        sender.send_keys(split)
        sender.send_keys(Keys.SHIFT, Keys.RETURN)

    sender.send_keys('\n')
    if at == 'Nick':
        sender.send_keys('fucking weeb \n')

def respond_help(driver, msg_info):
    text = """Here's are my current functions:
        \'help\' - lists current functions,
        \'rent\' - returns upcoming payment,
        \'nyseg\' - returns NYSEG's contact info
        \'landlord\' - returns landlord's contact info
        More to come in the future!"""
    name = msg_info[1]
    respond(driver, name, text)
    print("command help to: " + name)
    
def respond_rent(driver, msg_info):
    name = msg_info[1]
    commands = msg_info[0].replace('@Bot Ly', "").split()
    if len(commands) == 1:
        text = sheet.get_next(name)
        respond(driver, name, text)
    elif len(commands) == 3 and commands[1] in names:
        name = commands[1].replace('@', '')
        text = sheet.get_next(name)
        respond(driver, name, text)
    else:
        text = "Invalid Args for command \'rent\'"
        respond(driver, name, text)
    print("command rent to: " + name)
    
def respond_unknown(driver, msg_info):
    name = msg_info[1]
    text = "Unknown Command. Maybe try \'help\'?"
    respond(driver, name, text)
    print("command unknown to: " + name)

def respond_nyseg(driver, msg_info):
    name = msg_info[1]
    text = """Here is NYSEG's contact info:
    Self Service Line: 800-600-2275 - (24/7)
    Customer Service: 800-572-1111  - (Mon - Fri | 7 - 19)
    Payment Arrangements: 888.315.1755
Link: https://tinyurl.com/nyseg"""
    respond(driver, name, text)
    print("command nyseg to: " + name)
    
def respond_landlord(driver, msg_info):
    name = msg_info[1]
    text = """Here is Ike's contact info:
    email: mnestopo@twncy.rr.com
    phone: (607)-339-1137
Here is John's contact info:
    email: bgm900@gmail.com"""
    respond(driver, name, text)
    print("command landlord to: " + name)

def respond_fu(driver, msg_info):
    name = msg_info[1]
    text = "fuck you"
    respond(driver, name, text)
    print("command fu to: " + name)

p1 = "⭕️"
p4 = "❌"
p0 = "⬜️"

games = {}

newboard  = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

currentboard = newboard

def boardtotext(board):
    text = ''
    for row in board:
        for element in board:
            if element == 0:
                text += p0
            elif element == 1:
                text += p1
            elif element == 4:
                text += p4
        text += "\n"
    return text

# =============================================================================
# def makemove(board, difficulty):
#     if difficulty == 0:
#         row = random.randint(3)
#         col = random.randint(3)
#         
#         while(board[row][col] != 0):
#             row = random.randint(3)
#             col = random.randint(3)
#         board[row][col] = 4
#         return board
#     
#     elif difficulty == 1:
#         if board[1][1] == 0:
#             board[1][1] = 4
#             return board
#         elif 
#     elif difficulty == 2:
#         print(2)
#         
# def ticktacktoe(driver, msg_info):
#     name = msg_info[1]
#     if commands[1] == 'new':
#         text = ''
#         difficulty = 1
#         if len(commands > 2):
#             try:
#                 difficulty = int(commands[2])
#             execpt:
#                 text += 'Invalid difficulty. Defaulting to 1.\n'
#         text += 'Starting new game at difficulty ' + str(difficulty) + "\n"
#         if(random.randint(2) == 0):
#             games[name] = newboard
#             text += "You start.\n"
#             text += boardtotext(games[name])
#         else:
#             text += "I start."
# 
#     commands = msg_info[0].replace('@Bot Ly', "").split()
#     if commands.length != 2:
#         text = "Invalid Args for command TickTackToe (TTT)"
# 
# 
# =============================================================================




