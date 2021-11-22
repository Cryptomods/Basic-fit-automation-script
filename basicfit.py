from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium import webdriver
from os.path import abspath
from os import path
from time import sleep
from datetime import datetime


def reservePlace():
    global notReserved
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "reserveBookingId"))
        )
        element.click()
        if(tijdvlak == '2'):
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "eveningSlotsId"))
            )
            element.click()
        else:
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "afternoonSlotsId"))
            )
            element.click()

        sleep(1)

        wait = WebDriverWait(driver, 10)


        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "radio-button-row"))
        )

        datereserve = driver.find_elements_by_class_name("radio-button-row")


        for i in datereserve:
            datestring = i.text[:i.text.index(",")]
            if(datestring==DayReserved):
                # print(i.text)
                i.click()
                break
        sleep(2)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "clickable"))
        )


        gymtime = driver.find_elements_by_class_name("clickable")

        try:
            driver.find_element_by_id("nightSlotsId")
            gymtime = gymtime[5:]
        except:
            "No evening slot"
            gymtime = gymtime[4:]


        reserveerwoord = []
        for word in gymtime:
            if(word.get_attribute("style") == "background: rgb(254, 112, 0);"):
                reserveerwoord.append("RESERVEER")
            else:
                reserveerwoord.append("FULL")
        print(reserveerwoord)

        # print(len(gymtime))

        # sleep(1)
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "hEekTv"))
        )

        templist = ['Schiedam Prinses Beatrixlaan 24/7', 'Schiedam de Brauwweg 24/7', 'Nacht', 'Ochtend', 'Middag', 'Avond']
        gymtijden = []
        timestamp = driver.find_elements_by_class_name("hEekTv")
        for i in timestamp:
            if(i.text not in templist):
                gymtijden.append(i.text)

        # reserveerwoord = []
        # for gym in gymtime:
        #     reserveerwoord.append(gym.text)

        counter = BeginTime
        teller = 0 

        reservedTime = Times[BeginTime:EndTime+1]
        print(reservedTime)
        for gymtijd in gymtijden:
            if( reserveerwoord[teller] == 'RESERVEER') and gymtijden[teller] in reservedTime:
                print(gymtijden[teller])
                gymtime[teller].click()
                element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "nextBtnId"))
                )
                element.click()
                
                if Comfort:
                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='contentSection']/div[1]/div/div[13]/span"))
                    )
                    element.click()

                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='contentSection']/div[1]/div/div[22]/div[1]"))
                    )
                    element.click()

                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "nextBtnId"))
                    )
                    element.click()

                    notReserved = False
                    break
                else:
                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='contentSection']/div[1]/div[19]/span"))
                    )
                    element.click()

                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='contentSection']/div[1]/div[28]/div[1]"))
                    )
                    element.click()

                    element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "nextBtnId"))
                    )
                    element.click()

                    notReserved = False
                    break
            teller+=1
            
        # sleep(2)
        print("No place")
        print(datetime.now())
        driver.refresh()
        sleep(2)
    
    except Exception as e:
        print(e)
        driver.get("https://my.basic-fit.com/gym-time-booking")


options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Banano\AppData\Local\Google\Chrome\User Data")  # Path to your chrome profile or you can open chrome and type: "chrome://version/" on URL

chrome_driver_exe_path = abspath("C:/Users/Banano/Downloads/chromedriver_win32/chromedriver.exe")  # download from https://chromedriver.chromium.org/downloads
assert path.exists(chrome_driver_exe_path), 'chromedriver.exe not found!'

Comfort = False
DayReserved = ''
main_heading = '''
██████████████████████████████████████████████
█                                            █
█                 BASIC FIT                  █
█                 ----------                 █
█                 GO FOR IT                  █
█                                            █
██████████████████████████████████████████████


'''

print(main_heading)
print("1:Maandag\n2:Dinsdag\n3:Woensdag\n4:Donderdag\n5:Vrijdag\n6:Zaterdag\n7:Zondag")
print("")
ValidInput = True
while ValidInput:
    Daychosen  = input("Op welke dag wil je reserveren?, kies een nummber: ")
    if(Daychosen not in ['1','2','3','4','5','6','7']):
        print("Verkeerd nummer probeer nogmaals\n")
    else:
        ValidInput = False
    if(Daychosen=='1'):
        DayReserved = 'Maandag'
    elif(Daychosen=='2'):
        DayReserved = 'Dinsdag'
    elif(Daychosen=='3'):
        DayReserved = 'Woensdag'
    elif(Daychosen=='4'):
        DayReserved = 'Donderdag'
    elif(Daychosen=='5'):
        DayReserved = 'Vrijdag'
    elif(Daychosen=='6'):
        DayReserved = 'Zaterdag'
    elif(Daychosen=='7'):
        DayReserved = 'Zondag'



print("Kies een tijdvlak\n")
print("1: Middag\n2: Avond")
tijdvlak = input()

if(tijdvlak=='2'):
    Times = ['18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45']
else:
    Times = ['12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45']


for i in range(0, 24):
    print(str(i) +', ' + Times[i] + '\n')

print("Kies een begintijd:\n")

BeginTime  = int(input())

print("Kies een eindtijd:\n")

EndTime  = int(input())

driver = webdriver.Chrome(executable_path=chrome_driver_exe_path, options=options)

driver.maximize_window()

driver.get("https://my.basic-fit.com/overview")


nameList = ["ROY!", "SACHIL!"]

sleep(4)
#check if user is Sachil or Carlo
# element = WebDriverWait(driver, 10).until(
# EC.presence_of_element_located((By.XPATH, "//*[@id='welcomeMessageHead']"))
# )
# if(element.text.split()[1] in nameList): #change this later my_str[:-1]
#     Comfort = True

# print(element.text)

Comfort = True

element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "gymTimeBookingMenuId"))
)
sleep(1)
element.click()

notReserved = True
while notReserved:
    reservePlace()

