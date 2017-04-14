import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#for the purpose of pausing the browser b4 we open new tab


Goolge = 'https://google.com'
Craigs = 'https://craigslist.org'
Cars = 'https://cars.com'

response = requests.get(Goolge)
response2 = requests.get(Craigs)

GoogleHtml = response.content
CraigsHtml = response2.content #dont really have a need for the raw html tho

BaseQuery = input("What exactly are you searching for ?")

NewBaseQuery = TextBlob(BaseQuery)#Have to make query a blob before we correct it
#BaseQuery.noun_phrases
print(NewBaseQuery.correct()) #attempts to correct any spelling errors
NewBaseQuery = NewBaseQuery.correct()
print("so you're looking for " + BaseQuery)


print(NewBaseQuery.words)
AutoGroup = ['auto', 'car', 'vehicle']
if any(word in AutoGroup for word in NewBaseQuery.words): #checks Autogroup against NewBaseQuery.words

    MakeQuery = input("Do you have a preference of Make?")
    #ModelQuery = input("Do you have a Model preference?")
    #CashValue = input("And exactly how much are you willing to spend?")
    Zip = input("And Lastly what is your zipcode?")

    Ibrowser = webdriver.Chrome()
    Ibrowser.get(Cars)

    CarElementSearch = Ibrowser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/cars-tabs/div/div/div/div/cars-pane[1]/div/cars-inventory-search-form/form/div[2]/div[1]/div/div[1]/div/select")
    CarElementSearch.send_keys(MakeQuery)

    ZipElement = Ibrowser.find_element_by_name("zipField")
    ZipElement.send_keys(Zip)

    Submit = Ibrowser.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/cars-tabs/div/div/div/div/cars-pane[1]/div/cars-inventory-search-form/form/div[2]/div[2]/div/div[4]/input")
    Submit.click()

print("***********************")
print(NewBaseQuery.noun_phrases)
print(NewBaseQuery.pos_tags)
print(NewBaseQuery)



browser = webdriver.Chrome() #Assign Chrome as the browser
browser.get(Goolge)          #Open Chrome for use
tab1 = browser.current_window_handle
element = browser.find_element_by_name('q')  #Finds & assings the searchbar, named 'q' on Google Page to element

element.send_keys(NewBaseQuery) #Sends the initial query to the searchbar q
submit = browser.find_element_by_name("btnG") #Assings submit to the search button on Google Page
submit.click()                                #Lets press Enter

#tab1 = browser.current_window_handle
#print(tab1)

browser.implicitly_wait(15)
browser.execute_script("window.open('https://craigslist.org');") #This executs javascript in the python code
         #Attempts to open a new tab in Chrome
#tab2 = browser.current_window_handle
#print(tab2)


#browser.get(Craigs) #Opens Craigslist

#browser.switch_to.window(tab2)
print(browser.window_handles) #prints the fact that there are 2 tabs open

browser.implicitly_wait(10)    ###NOT ABLE TO SWITCH TABS NEEDS HELP
browser.switch_to.window(browser.window_handles[-1])  # attempts to switch using its araay placement
#browser.switch_to.window(tab1)



element2 = browser.find_element_by_name('query') #Element 2 isnt being assigned to query
element2.send_keys(NewBaseQuery.noun_phrases)
element2.send_keys(Keys.ENTER)

