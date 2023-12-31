from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
chrome_driver_path = r"C:\Users\swnagras\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver_path)


def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(service=service, options=options)
  driver.get("http://automated.pythonanywhere.com/login/")
  return driver

def clean_text(text):
  #print(text.split(": "))
  output = float(text.split(": ")[1])
  return output


def main():
  driver = get_driver()
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(1)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated")
  driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[3]/form/button").click()
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  time.sleep(3)

  while True:
    print("loop started")
    text= driver.find_element(by="id", value="displaytimer").text
    temp= str(clean_text(text))
    filename= datetime.now().strftime("%Y-%m-%d.%H-%M-%S")+".txt"
    # Open a file for writing (creates a new file if it doesn't exist)
    with open(filename, 'w') as file:
      # Write data to the file
      file.write(temp)
    # The file is automatically closed when the 'with' block is exited
    time.sleep(3)
def del_files:

main()
print("loop ends")
