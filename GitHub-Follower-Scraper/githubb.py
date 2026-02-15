from GithubUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By  
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def signIN(self):
        self.browser.get("https://github.com/login")

        time.sleep(2) 

        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH,"/html/body/div[1]/div[4]/main/div/div[2]/form/div[3]/input").click()

    def getfollowers(self):
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        kullanici_etiketleri = self.browser.find_elements(By.CSS_SELECTOR, ".d-table .Link--secondary")   

        for etiket in kullanici_etiketleri:
            isim = etiket.text
            if isim != "": 
                self.followers.append(isim)
                print(f"Bulunan Takipçi: {isim}")

github = Github(username,password)
github.signIN()
github.getfollowers()
print(github.followers)                       


        
        

