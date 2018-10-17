import os
currDirectory = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(currDirectory)

import time
import datetime as dt
from datetime import datetime
import json
from selenium import webdriver

import responces as r

from bs4 import BeautifulSoup

def log_in(headless):
    with open(currDirectory + '\\info.json') as f:
        info = json.load(f)
    login_ = info['FBUsername']
    password_ = info['FBPassword']
    chrome_options = webdriver.ChromeOptions()
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(currDirectory + "\\chromedriver_win32\\chromedriver.exe",
                              chrome_options=chrome_options)
    driver.get("https://www.messenger.com/login/")
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    signin = driver.find_element_by_id("loginbutton")
    username.send_keys(login_)
    password.send_keys(password_)
    signin.click()
    groupchat = driver.find_element_by_xpath("//span[text()='testing']")
    groupchat.click()
    return driver

def message_source(driver):
    return driver.find_element_by_class_name("_4_j4").get_attribute('innerHTML')

def messages_info(driver, source, numToCheck = 5, time_retain = 2):
    ago = (datetime.now() - dt.timedelta(minutes=time_retain)).time()
    soup = BeautifulSoup(source, "html.parser")
    lst_msg=[]
    messages = soup.findAll('div', class_="_3058")
    if len(messages) > numToCheck:
        messages=messages[-numToCheck:]
    for message in messages:
        #could be None if typing bubbles
        bubble = message.parent.parent.find('h5', class_="_ih3")
        if bubble is not None and message.has_attr('body'):
            text = message['body']
            sender = message.parent.parent.find('h5', class_="_ih3").text
            raw = message['data-tooltip-content']
            if str.isdigit(raw[0]) or raw[0:2].lower() == ago.strftime("%A")[0:2].lower():
                beginning = raw.find(':') - 2
                if beginning < 0:
                    beginning = 0;
                raw2 = raw[beginning:raw.find(':')+3].strip()
                time_sent = datetime.strptime(raw2, '%H:%M')
                if "PM" in raw:
                    time_sent += dt.timedelta(hours=12)
                if time_sent.time() >= ago:
                    lst_msg.append((text, sender, time_sent.time()))
    return lst_msg

def check(driver, seen):
    source = message_source(driver)
    msgs_info = messages_info(driver, source)
    for msg_info in msgs_info:
        if "@bot ly" in msg_info[0].lower() and msg_info not in seen:
            seen.add(msg_info)
            command = msg_info[0].replace('@Bot Ly', "").split()[0]
            print(msg_info[0].replace('@Bot Ly', "").split())

# =============================================================================
#             negatives = msg_info[0].count("no")
#             if negatives > 0:
#                 r.respond_fu(driver, msg_info)
# =============================================================================

            if command.lower() == "!help":
                r.respond_help(driver, msg_info)
            elif command.lower() == "!rent":
                r.respond_rent(driver, msg_info)
            elif command.lower() == "!landlord":
                r.respond_landlord(driver, msg_info)
            elif command.lower() == "!nyseg":
                r.respond_nyseg(driver, msg_info)
            else:
                r.respond_unknown(driver, msg_info)
    return seen






