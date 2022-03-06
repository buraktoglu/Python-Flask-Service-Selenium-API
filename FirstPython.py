from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# VALID PARAMETERS
# "beige"
# "black"
# "blue"
# "brown"
# "gold"
# "gray"
# "green"
# "orange"
# "purple"
# "red"
# "silver"
# "white"
# "yellow"
def checkColor(colorID) :

    Colors = {
            "beige":    "//*[@id='panel_exterior_colors']/div[1]/label",
            "black":    "//*[@id='panel_exterior_colors']/div[2]/label",
            "blue":     "//*[@id='panel_exterior_colors']/div[3]/label",
            "brown":    "//*[@id='panel_exterior_colors']/div[4]/label",
            "gold":     "//*[@id='panel_exterior_colors']/div[5]/label",
            "gray":     "//*[@id='panel_exterior_colors']/div[6]/label",
            "green":    "//*[@id='panel_exterior_colors']/div[7]/label",
            "orange":   "//*[@id='panel_exterior_colors']/div[8]/label",
            "purple":   "//*[@id='panel_exterior_colors']/div[9]/label",
            "red":      "//*[@id='panel_exterior_colors']/div[10]/label",
            "silver":   "//*[@id='panel_exterior_colors']/div[11]/label",
            "white":    "//*[@id='panel_exterior_colors']/div[12]/label",
            "yellow":   "//*[@id='panel_exterior_colors']/div[13]/label"
            }

    click_Button_Colors = browser.find_element(By.ID, "trigger_exterior_colors")

    click_Button_Colors.click()
    time.sleep(2)

    (browser.find_element(By.XPATH, Colors[colorID])).click()
    time.sleep(2)
    
    click_Button_Colors.click()
    time.sleep(2)
    return

# VALID PARAMETERS
# "automanual"
# "automatic"
# "cvt"
# "manual"
# "unknown"
def checkTransmission(transmissionsID) :

    Transmissions = {
                    "automanual"    :"//*[@id='panel_transmissions']/div[1]/label",
                    "automatic"     :"//*[@id='panel_transmissions']/div[2]/label",
                    "cvt"           :"//*[@id='panel_transmissions']/div[3]/label",
                    "manual"        :"//*[@id='panel_transmissions']/div[4]/label",
                    "unknown"       :"//*[@id='panel_transmissions']/div[5]/label"
                    }

    click_Button_Transmission = browser.find_element(By.ID, "trigger_transmissions")

    click_Button_Transmission.click()
    time.sleep(2)
    (browser.find_element(By.XPATH, Transmissions[transmissionsID])).click()
    time.sleep(2)
    click_Button_Transmission.click()
    time.sleep(2)

    return


def getCarFeatures2() :
    carFeatures = {}

    headers = browser.find_elements(By.TAG_NAME,"dt")
    features = browser.find_elements(By.TAG_NAME,"dd")

    for x in range(0,11):
        carFeatures[headers[x].text] = features[x].text
    
    return carFeatures

def getCarFeatures():
    browser.find_element(By.CLASS_NAME, "vehicle-card-link").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/section/div[4]/section[2]/div/div[2]/a").click()
    time.sleep(2)
    price = browser.find_element(By.XPATH, "/html/body/section/div[5]/section/header/div[2]/span").text
    time.sleep(2)
    trans = browser.find_element(By.XPATH, "/html/body/section/div[5]/div[2]/section[1]/dl/dd[6]").text
    time.sleep(2)
    extcolor = browser.find_element(By.XPATH, "/html/body/section/div[5]/div[2]/section[1]/dl/dd[1]").text
    time.sleep(2)
    title = browser.find_element(By.XPATH, "/html/body/section/div[5]/section/header/div[1]/h1").text
    featureList = title.split(" ", 2)
    time.sleep(2)

    carFeatures = {}
    carFeatures["title"] = title
    carFeatures["year"] = featureList[0]
    carFeatures["brand"] = featureList[1]
    carFeatures["model"] = featureList[2]
    carFeatures["price"] = price
    carFeatures["transmission"] = trans
    carFeatures["extcolor"] = extcolor

    time.sleep(2)
    return


def selectBrand(brandName) :
    Select(browser.find_element(By.ID,"make_select")).select_by_value(str(brandName).lower())
    return


def selectMinYear(year) :
    Select(browser.find_element(By.ID,"year_year_min_select")).select_by_value(str(year))
    return


def selectMaxYear(year) :
    Select(browser.find_element(By.ID,"year_year_max_select")).select_by_value(str(year))
    return


def selectYearInterval(year1, year2) :
    if year2 >= year1:
        selectMinYear(year1)
        time.sleep(2)
        selectMaxYear(year2)
    return

# VALID PARAMETERS
# 10
# 20
# 30
# 50
# 100
def configurePagination(listSize) :
    Select(browser.find_element(By.ID, "pagination-dropdown")).select_by_value(str(listSize))
    return

# def goInGatherInfoGetOut() :

#     cars = {}
#     for x in range(5):
#         listOfRefs = browser.find_elements(By.CLASS_NAME, "vehicle-card-link")
#         time.sleep(2)
#         listOfRefs[x].click()
#         time.sleep(2)
#         cars[x] = getCarFeatures()
#         time.sleep(2)
#         browser.find_element(By.XPATH, "/html/body/section/div[4]/section[1]/nav/ul/li[3]/span[2]/a").click()
#         time.sleep(2)
#     return cars

def gatherInfoFromMainPage() :

    cars = {}
    
    return

def goInGatherInfoNext():

    browser.find_element(By.CLASS_NAME, "vehicle-card-link").click()
    time.sleep(2)
    cars = {}
    cars[0] = getCarFeatures()

    for x in range(3):

        cars[x+1] = getCarFeatures()
        time.sleep(2)
        browser.find_element(By.XPATH, "/html/body/section/div[4]/section[2]/div/div[2]/a").click()
        time.sleep(2)

    return cars

# main flow starts here

browser = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
browser.maximize_window()
browser.implicitly_wait(8)
browser.get("https://www.cars.com/for-sale/searchresults.action")


# configurePagination(10)

# time.sleep(2)
# selectBrand()
# time.sleep(2)
# selectYearInterval(2020,2022)
# time.sleep(2)
# checkColor("red")
# time.sleep(2)
# checkTransmission("automanual")
# time.sleep(2)
# cars = goInGatherInfoNext()
# selectBrand("audi")
# time.sleep(2)
# print(cars)
# selectBrand()
# selectYearInterval(2020,2022)
# checkColor("blue")
# checkTransmission("automanual")
getCarFeatures()

time.sleep(3)

browser.close()