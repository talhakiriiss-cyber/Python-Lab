import json
import os

class user:
    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email
        

class userRespository:
    def __init__(self):
        self.users = []

        self.isloggedIn = False

        self.currentUser = {}

        self.loadusers()

    def loadusers(self):
     if os.path.exists("users.json"):
        with open("users.json", "r", encoding="utf-8") as file:
            users = json.load(file)
            for item in users: 
                user_data = json.loads(item) 
                
                
                newUser = user(username=user_data["username"], password=user_data["password"], email=user_data["email"])
                
                self.users.append(newUser)
        print(self.users)     


    def register(self, user: user):
        self.users.append(user)
        self.savetofile()
        print("Kullanıcı Oluşturuldu")

    def login(self,username,password):    
         for user in self.users:
            if user.username == username and user.password == password:
                self.isloggedIn = True
                self.currentUser = user
                print("Giriş Yapıldı")
                break

    def logout(self):
        self.isloggedIn= False
        self.currentUser={}
        print("Çıkış yapıldı")

    def identity(self):
        if self.isloggedIn:
         print(f"username: {self.currentUser.name}")
        else: 
         print("Giriş yapılmadı")


    def savetofile(self):
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users.json","w")as file:
            json.dump(list,file) 


respository= userRespository()

while True:
    print("Menü".center(50,"*"))  
    secim = input("1- Registere\n2- Login\n3- Logout\n4- identity\n5- EXİT\nSeçiminiz: ")  
    if secim == "5":
        break
    else:
       if secim == "1":
         username = input("Username: ")
         password = input("Password: ")
         email = input("Email: ")

         user = user(username=username,password=password,email=email)
         respository.register(user)
       elif secim == "2":
           if respository.isloggedIn:
              print("Zaten login oldunuz")
           else:  
                  username = input("username: ")
                  password = input("Password: ")
                  respository.login(username,password)
       elif secim == "3":
           respository.logout()
       elif secim == "4":
           respository.identity()
       else:
           print("Yanlış Seçim!")