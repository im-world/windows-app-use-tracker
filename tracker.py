import os
import win32process
import win32gui          
import psutil
import hashlib
import time
import datetime
import pandas as pd

#C:\Users\current_user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\ 


def initDataframe():
    data = pd.Dataframe(columns=['App Name', 'Time Used', 'Start Times', 'End Times'])
    data.set_index('App Name')
    data['Start Times'] = data['Start Times'].astype(list)
    data['End Times'] = data['End Times'].astype(list)
    return data


def initVariables():
    yearStored, monthStored, dayStored = datetime.date
    previousAppTitle = ' '
    data.loc[previousAppTitle]['Start Times'].append() = getCurrentTime()
    return


def isDifferentDay(dayCurrent, monthCurrent, yearCurrent, data):
    if(dayCurrent != dayStored):
        data = saveData(data)
        UpdateStoredDate(dayCurrent, monthCurrent, yearCurrent)
    return data


def appMonitor(data):
    try:
        currentAppTitle = getCurrentAppTitle()
        
        if(currentAppTitle != previousAppTitle):
            previousAppTitle = currentAppTitle
            data.loc[currentAppTitle]['Start Times'].append() = getCurrentTime()
            data.loc[previousAppTitle]['End Times'].append() = getCurrentTime()
            data.loc[previousAppTitle]['Time Used'] += calcTimeUsedRecent(AppTitle)
            
        except psutil.NoSuchProcess:

        return data
            
        
def saveData(data):
    lastDay = str(dayStored + ':' + monthStored + ':' + yearStored)
    data.to_csv(lastDay)
    data = pd.DataFrame(columns=data.columns)
    return data


def loop():
    yearCurrent, monthCurrent, dayCurrent = datetime.date
    data = isDifferentDay(yearCurrent, monthCurrent, dayCurrent, data):
    data = appMonitor(data)
    return data
    
    
def process():
    data = initDataframe()
    initVariables()
    while True:
        data = loop(data)
        time.sleep(1)
    return


#Utility Functions
def UpdateStoredDate(dayCurrent, monthCurrent, yearCurrent):
    dayStored = dayCurrent
    monthStored = monthCurrent
    yearStored = yearCurrent
    return


def getCurrentAppTitle():
    currentAppTitle = str(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    return currentAppTitle

    
def getCurrentTime():
    currentTime = datetime.now().strftime("%H:%M:%S")
    return currentTime


def calcTimeUsedRecent(AppTitle):
    timeUsed = data.loc[AppTitle]['Start Times'][-1] - data.loc[AppTitle]['End Times'][-1]
    return timeUsed


#run
process()











#os.chdir(foldername)
#todo - auth, UI, autorun