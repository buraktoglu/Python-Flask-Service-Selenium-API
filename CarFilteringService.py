from flask import Flask, jsonify
from flask import request
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

app = Flask(__name__)

@app.route('/cars/list', methods=['GET'])
def ListCars():
    driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
    driver.implicitly_wait(8)
    driver.maximize_window()
    driver.get("https://www.cars.com/for-sale/searchresults.action")

    def getCarFeatures():     
        price = driver.find_element(By.XPATH, "/html/body/section/div[5]/section/header/div[2]/span").text
        #time.sleep(2)
        trans = driver.find_element(By.XPATH, "/html/body/section/div[5]/div[2]/section[1]/dl/dd[6]").text
        #time.sleep(2)
        extcolor = driver.find_element(By.XPATH, "/html/body/section/div[5]/div[2]/section[1]/dl/dd[1]").text
        #time.sleep(2)
        title = driver.find_element(By.XPATH, "/html/body/section/div[5]/section/header/div[1]/h1").text
        #time.sleep(2)
        featureList = title.split(" ", 2)
        #time.sleep(2)

        carFeatures = {}
        carFeatures["title"] = title
        carFeatures["year"] = featureList[0]
        carFeatures["brand"] = featureList[1]
        carFeatures["model"] = featureList[2]
        carFeatures["price"] = price
        carFeatures["trans"] = trans
        carFeatures["extcolor"] = extcolor

        return carFeatures

    def goInGatherInfoNext(numberOfCars):

        driver.find_element(By.CLASS_NAME, "vehicle-card-link").click()
        #time.sleep(2)

        cars = {}
        cars[0] = getCarFeatures()

        for x in range(numberOfCars-1):
            try :
                driver.find_element(By.XPATH, "/html/body/section/div[4]/section[2]/div/div[2]/a").click()
                #time.sleep(2)
            except:
                break
            else:
                cars[x+1] = getCarFeatures()

        return cars

    ## Solves the getting 48 cars instead of 50 problem but not preferable or best practice due to time constraints
    # def goInGatherInfoGetOut(numberOfCars) :
    #     configurePagination(100)
    #     cars = {}
    #     for x in range(numberOfCars):
    #         listOfRefs = driver.find_elements(By.CLASS_NAME, "vehicle-card-link")
    #         time.sleep(2)
    #         listOfRefs[x].click()
    #         time.sleep(2)
    #         cars[x] = getCarFeatures()
    #         time.sleep(2)
    #         driver.find_element(By.XPATH, "/html/body/section/div[4]/section[1]/nav/ul/li[3]/span[2]/a").click()
    #         time.sleep(2)
    #     return cars

    # VALID PARAMETERS ["beige", "black", "blue", "brown", "gold", "gray", "green", "orange", "purple", "red", "silver", "white", "yellow"]
    def checkColor(key) :

        Colors = {
                "beige":    "//*[@id='panel_exterior_colors']/div[1]/label" ,
                "black":    "//*[@id='panel_exterior_colors']/div[2]/label" ,
                "blue":     "//*[@id='panel_exterior_colors']/div[3]/label" ,
                "brown":    "//*[@id='panel_exterior_colors']/div[4]/label" ,
                "gold":     "//*[@id='panel_exterior_colors']/div[5]/label" ,
                "gray":     "//*[@id='panel_exterior_colors']/div[6]/label" ,
                "green":    "//*[@id='panel_exterior_colors']/div[7]/label" ,
                "orange":   "//*[@id='panel_exterior_colors']/div[8]/label" ,
                "purple":   "//*[@id='panel_exterior_colors']/div[9]/label" ,
                "red":      "//*[@id='panel_exterior_colors']/div[10]/label",
                "silver":   "//*[@id='panel_exterior_colors']/div[11]/label",
                "white":    "//*[@id='panel_exterior_colors']/div[12]/label",
                "yellow":   "//*[@id='panel_exterior_colors']/div[13]/label"
                }

        click_Button_Colors = driver.find_element(By.ID, "trigger_exterior_colors")

        click_Button_Colors.click()
        time.sleep(2)
        try :
            driver.find_element(By.XPATH, Colors[key]).click()
            time.sleep(2)
        finally :      
            click_Button_Colors.click()
            time.sleep(2)
        
        return

    # VALID PARAMETERS ["automanual", "automatic", "cvt", "manual", "unknown"]
    def checkTransmission(key) :

        Transmissions = {
                        "automanual"    :"//*[@id='panel_transmissions']/div[1]/label",
                        "automatic"     :"//*[@id='panel_transmissions']/div[2]/label",
                        "cvt"           :"//*[@id='panel_transmissions']/div[3]/label",
                        "manual"        :"//*[@id='panel_transmissions']/div[4]/label",
                        "unknown"       :"//*[@id='panel_transmissions']/div[5]/label"
                        }

        click_Button_Transmission = driver.find_element(By.ID, "trigger_transmissions")

        click_Button_Transmission.click()
        time.sleep(2)
        try :
            driver.find_element(By.XPATH, Transmissions[key]).click()
            time.sleep(2)
        finally :
            click_Button_Transmission.click()
            time.sleep(2)
        
        return

    def selectBrand(brandName) :
        Select(driver.find_element(By.ID,"make_select")).select_by_value(str(brandName).lower())
        time.sleep(2)
        return

    def selectMinYear(year) :
        Select(driver.find_element(By.ID,"year_year_min_select")).select_by_value(str(year))
        return

    def selectMaxYear(year) :
        Select(driver.find_element(By.ID,"year_year_max_select")).select_by_value(str(year))
        return

    def selectYear(year) :
        selectMinYear(year)
        time.sleep(2)
        selectMaxYear(year)
        time.sleep(2)
        return

    def selectYearInterval(year1, year2) :
        selectMinYear(year1)
        time.sleep(2)
        selectMaxYear(year2)
        time.sleep(2)
        return

    # VALID PARAMETERS [10, 20, 30, 50, 100]
    def configurePagination(listSize) :
        Select(driver.find_element(By.ID, "pagination-dropdown")).select_by_value(str(listSize))
        time.sleep(6)
        return

    # main flow starts here

    colors  = list(request.args.getlist("extcolor"))
    transs  = list(request.args.getlist("trans"))
    years   = list(request.args.getlist("year"))
    brand   = list(request.args.getlist("brand"))

    colorsLen = len(colors)
    transsLen = len(transs)
    yearsLen = len(years)
    brandLen = len(brand)
    numberOfParameters = colorsLen + transsLen + yearsLen + brandLen

    configurePagination(50)

    # color filtering, support more than one color parameters
    for i in range(colorsLen) :
        checkColor(colors[i])

    # transmission filtering, support more than one transmission parameters
    for i in range(transsLen) :
        checkTransmission(transs[i])

    # brand filtering, website doesnt support more than on brand filter
    if brandLen == 1 :
        selectBrand(brand[0])
    elif brandLen != 0 :
        driver.close()
        return "Bad Request. Service supports only one brand filter!", 400
    
    # year filtering
    if yearsLen == 1:
        selectYear(years[0])
    elif yearsLen == 2:
        years.sort()
        selectYearInterval(years[0], years[1])
    elif yearsLen != 0:
        driver.close()
        return "Bad Request. Service supports only one or two year filters!", 400

    if numberOfParameters == 0 :
        configurePagination(50)

    cars = goInGatherInfoNext(50)
    driver.close()

    # main flow ends here

    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)