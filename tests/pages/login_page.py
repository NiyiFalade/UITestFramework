
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username="#user-name"
        self.password="#password"
        self.login="#login-button"


    def load(self):
        self.page.goto("/")

    def loginAsUser(self,username,password):
        self.page.fill(self.username, username)    
        self.page.fill(self.password, password) 

        assert self.page.locator(self.username).input_value() == username
        assert self.page.locator(self.password).input_value() == password

        self.page.screenshot(path="reports/screenshots/login.png")
        
        self.page.click(self.login)   


