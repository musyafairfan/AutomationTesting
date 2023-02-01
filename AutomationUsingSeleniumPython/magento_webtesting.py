import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker()
firstName = fake.first_name()
lastName = fake.last_name()
email = firstName + "@mailinator.com"
password = fake.password()
fullName = (firstName) + " " + (lastName)
# ================================== #
emailTerdaftar = "joko@mailinator.com"
pwd = "@Joko123"


class TestMagento(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver.set_window_size(1480, 860)

    def test_a_register_success(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(firstName)
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(lastName)
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID, 'password-confirmation').send_keys(password)
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        welcome = driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[1]/span')
        assert welcome.text == "Welcome, " + fullName + "!"
        success_register = driver.find_element(
            By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')
        assert success_register.text == "Thank you for registering with Fake Online Clothing Store."

    def test_b_register_failed_already_account(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(firstName)
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(lastName)
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(email)
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID, 'password-confirmation').send_keys(password)
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(
            By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')
        assert messageError.text == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."

    def test_c_register_failed_empty_firstname(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(fake.last_name())
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(
            firstName + "@mailinator.com")
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.ID, 'password-confirmation').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'firstname-error')
        assert messageError.text == "This is a required field."

    def test_d_register_failed_empty_lastname(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(fake.first_name())
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(
            firstName + "@mailinator.com")
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.ID, 'password-confirmation').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'lastname-error')
        assert messageError.text == "This is a required field."

    def test_e_register_failed_empty_email(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(fake.first_name())
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(fake.last_name())
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.ID, 'password-confirmation').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'email_address-error')
        assert messageError.text == "This is a required field."

    def test_f_register_failed_empty_password(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(fake.first_name())
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(fake.last_name())
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(
            firstName + "@mailinator.com")
        time.sleep(1)
        driver.find_element(
            By.ID, 'password-confirmation').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'password-error')
        assert messageError.text == "This is a required field."

    def test_g_register_failed_empty_confirm_password(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(fake.first_name())
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(fake.last_name())
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(
            firstName + "@mailinator.com")
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(
            By.ID, 'password-confirmation-error')
        assert messageError.text == "This is a required field."

    def test_h_register_failed_empty_all_field(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'firstname-error')
        assert messageError.text == "This is a required field."
        messageError = driver.find_element(By.ID, 'lastname-error')
        assert messageError.text == "This is a required field."
        messageError = driver.find_element(By.ID, 'email_address-error')
        assert messageError.text == "This is a required field."
        messageError = driver.find_element(By.ID, 'password-error')
        assert messageError.text == "This is a required field."
        messageError = driver.find_element(
            By.ID, 'password-confirmation-error')
        assert messageError.text == "This is a required field."

    def test_1_register_failed_invalid_format_email(self):
        driver = self.driver
        driver.implicitly_wait(1)
        driver.get("https://magento.softwaretestingboard.com/")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.ID, 'firstname').send_keys(fake.first_name())
        time.sleep(1)
        driver.find_element(By.ID, 'lastname').send_keys(fake.last_name())
        time.sleep(1)
        driver.find_element(By.ID, 'email_address').send_keys(
            firstName + "@mailinatorcom")
        time.sleep(1)
        driver.find_element(By.ID, 'password').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.ID, 'password-confirmation').send_keys(fake.password())
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()
        time.sleep(2)
        messageError = driver.find_element(By.ID, 'email_address-error')
        assert messageError.text == "Please enter a valid email address (Ex: johndoe@domain.com)."

    # def test_b_login_success(self):
    #     driver = self.driver
    #     driver.implicitly_wait(1)
    #     driver.get("https://magento.softwaretestingboard.com/")
    #     time.sleep(1)
    #     driver.find_element(
    #         By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a').click()
    #     time.sleep(1)
    #     driver.find_element(By.ID, 'email').send_keys(email)
    #     time.sleep(1)
    #     driver.find_element(By.ID, 'pass').send_keys(password)
    #     time.sleep(1)
    #     driver.find_element(
    #         By.ID, 'send2').click()
    #     time.sleep(2)
    #     welcome = driver.find_element(By.CLASS_NAME, 'logged-in')
    #     assert welcome.text == "Welcome, " + fullName + "!"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
