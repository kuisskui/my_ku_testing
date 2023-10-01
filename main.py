from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from dotenv import dotenv_values
import requests


config = dotenv_values("My.env")
username = config["USERNAME"]
password = config["PASSWORD"]
time = int(config["TIME"])

option = Options()
# option.add_argument("--start-maximized")
# option.add_experimental_option("detach", True)
# option.add_argument("--headless")

driver = webdriver.Safari()
driver.set_window_size(1600, 1200)

def user_login():
    driver.get("https://my.ku.th/login")
    sleep(time)
    
    # Fill in valid registration details
    driver.find_element(By.XPATH, "//input[@field='email']").send_keys(username)
    sleep(time)
    driver.find_element(By.XPATH, "//input[@field='password']").send_keys(password)
    sleep(time)
    
    # Click to login
    driver.find_element(By.XPATH, "//button[@class='btn btn-success btn-block']").click()
    sleep(time)

def user_logout():
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div/nav/div[6]/div/i').click()
    sleep(time)
    

def test_user_login():
    try:
        # Login
        user_login()
        
        # Verify success message on login page
        success_message = driver.find_element(By.XPATH, "//div/h4[@class='font-weight-bold mr-4 mb-0']")

        assert "ยินดีต้อนรับเข้าสู่ระบบลงทะเบียนนิสิต" in success_message.text

    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_user_login function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_user_login function")
        
def test_user_logout():
    try:
        user_logout()
    
    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_user_logout function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_user_logout function")
        
def test_view_schedule():
    user_login()
    try:
        driver.get("https://my.ku.th/std/classroom")
        response = requests.get("https://my.ku.th/std/classroom")
        sleep(time)
        
        assert response.status_code == 200
         
    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_search_registrable_subject function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_view_schedule function")
        user_logout()

def test_search_registrable_subject():
    # Login
    user_login()
    try:
        # Go to subject registration page
        driver.get("https://my.ku.th/std/subject")
        sleep(time)
        
        driver.find_element(By.XPATH, "//input[@class='rbt-input-main form-control rbt-input ']").send_keys("01219345-60")
        sleep(time)
        
        driver.find_element(By.XPATH, "//a/div/div[@class='col-12']").click()
        sleep(time)
        
        # Verify success message on list of subject
        success_message = driver.find_element(By.XPATH, "//span[text()='01219345-60']").text

        assert "01219345-60" in success_message
        
    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_search_registrable_subject function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_search_registrable_subject function")
        user_logout()
        
def test_payment_page():
    user_login()
    try:
        driver.get("https://my.ku.th/std/financeStudent")
        response = requests.get("https://my.ku.th/std/financeStudent")
        sleep(time)
        
        assert response.status_code == 200
         
    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_payment_page function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_payment_page function")
        user_logout()
        
def test_enroll_result_page():
    user_login()
    try:
        driver.get("https://my.ku.th/std/enrollresult")
        response = requests.get("https://my.ku.th/std/enrollresult")
        sleep(time)
        
        assert response.status_code == 200
         
    except Exception as e:
        # print(f"Test failed: {e}")
        print("❌ Test failed: test_enroll_result_page function")
    else:
        sleep(time)
        # driver.quit()
        print("✅ Testing Complete: test_enroll_result_page function")
        user_logout()

# Execute the test case
test_user_login()
sleep(time)
test_user_logout()
sleep(time)
test_view_schedule()
sleep(time)
test_search_registrable_subject()