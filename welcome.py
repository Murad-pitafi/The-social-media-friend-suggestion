class authorization():
    userinfo = {}
    friendlist = {}
    def signup(self):
        name = input("Enter your name")
        passwords = input("Enter your password")
        self.userinfo[name] = passwords
    def login(self):
        name = input("Enter your name")
        passwords = input("Enter your password")
        if self.userinfo[name] == passwords:
            return True
class menu(authorization):
    def welcome(self):
        opt = 1
        while opt:
            print("Hello welcome to newsfedia ")
            print("please select the options")
            print("1-> Signup ")
            print("2-> Login")
            opt = int(input())
        
            if opt == 1:
                self.signup()
            elif opt == 2:
                #self.HomePage(login)
                if self.login():
                    print("logged")
                    HomePage()
            else:
                print("Invalid option")    
        
    def HomePage(self):
         print("Home page")
         print("1 Add Friend ")
         print("2 view Friend")
         print("3 Friend Suggestions")


    def addfriend(self, username, friendname):
        #addfriend[username] = []
        for key, values in self.friendlist.items():
            if username not in key:
                self.friendlist[username] = [friendname]
            else:
                self.friendlist[username].append(friendname)    

    def view_friend(self, name):
        print(self.friendlist[name])


    def suggest_friend(self, name):
         suggest_friend = []
         freinds = self.friendlist[name]
         for i in freinds:
            suggest_friend.append(self.friendlist[i])
         print(suggest_friend)






obj = menu()
obj.welcome()
