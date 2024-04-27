from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
from selenium.webdriver.common.keys import Keys
import unittest

#test_user
#test_user2
#testT1234

class Hosttest(LiveServerTestCase, unittest.TestCase):
    
    def testHomePage(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('http://127.0.0.1:8000/')

        # implemented so selenium has time to setup browser
        time.sleep(3)

        # Press the login button with its XPATH
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        
        login_button.click()

        # Login using test username and password
        username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')

        # implemented so selenium has time show test
        time.sleep(3)

        username_input.send_keys('test_user')
        password_input.send_keys('testT1234')

        # implemented so selenium has time show test
        time.sleep(3)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        # implemented so selenium has time show test
        time.sleep(3)

        driver.quit()

    def testCreatingAssigningTask(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('http://127.0.0.1:8000/')

        # implemented so selenium has time to setup browser
        time.sleep(3)

        # Press the login button with its XPATH
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        login_button.click()

        # Login using test username and password
        username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')

        # implemented so selenium has time show test
        time.sleep(3)

        username_input.send_keys('test_user')
        password_input.send_keys('testT1234')

        time.sleep(3)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Select Team
        team_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        team_button.click()

        time.sleep(3)

        # Select Team Member
        team_member_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/ul/li/a')
        team_member_button.click()

        time.sleep(3)

        # Select new task
        new_task_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/a/button')
        new_task_button.click()

        time.sleep(3)

        # Create task
        title_input = driver.find_element(By.XPATH, '//*[@id="id_title"]')
        description_input = driver.find_element(By.XPATH, '//*[@id="id_description"]')
        due_date_input = driver.find_element(By.XPATH, '//*[@id="id_due_date"]')

        title_input.send_keys('test task')
        description_input.send_keys('this is a test description')
        due_date_input.send_keys('2024-08-24')
        
        # Create task extended for drop down menus
        completion_stage_input = driver.find_element(By.XPATH, '//*[@id="id_completion_stage"]')
        assignee_input = driver.find_element(By.XPATH, '//*[@id="id_assignee"]')

        completion_stage_select = Select(completion_stage_input)
        assignee_select = Select(assignee_input)

        completion_stage_select.select_by_visible_text('Not Started')
        assignee_select.select_by_visible_text('test_user2')

        time.sleep(3)

        submit_button = driver.find_element(By.XPATH, '/html/body/div[2]/form/button')
        submit_button.click()

        time.sleep(3)

        driver.quit()

    def testUpdatingViewingTask(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('http://127.0.0.1:8000/')

        # implemented so selenium has time to setup browser
        time.sleep(3)

        # Press the login button with its XPATH
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        login_button.click()

        # Login using test username and password
        username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')

        # implemented so selenium has time show test
        time.sleep(3)

        username_input.send_keys('test_user2')
        password_input.send_keys('testT1234')

        time.sleep(3)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Select Team
        team_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        team_button.click()

        time.sleep(3)

        task_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/ul/li/a')
        task_button.click()

        time.sleep(3)

        completion_stage_input = driver.find_element(By.XPATH, '//*[@id="id_completion_stage"]')
        completion_stage_select = Select(completion_stage_input)
        completion_stage_select.select_by_visible_text('Working On')

        time.sleep(3)

        update_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/form/button')
        update_button.click()

        time.sleep(3)

        driver.quit()

    def testDeletingTask(self):
        # using webdriver-manager to obtain the appropriate driver for firefox
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('http://127.0.0.1:8000/')

        # implemented so selenium has time to setup browser
        time.sleep(3)

        # Press the login button with its XPATH
        login_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        login_button.click()

        # Login using test username and password
        username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        password_input = driver.find_element(By.XPATH, '//*[@id="id_password"]')

        # implemented so selenium has time show test
        time.sleep(3)

        username_input.send_keys('test_user2')
        password_input.send_keys('testT1234')

        time.sleep(3)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)

        # Select Team
        team_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[2]')
        team_button.click()

        time.sleep(3)

        task_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/ul/li/a')
        task_button.click()

        time.sleep(3)

        remove_task_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/a/button')
        remove_task_button.click()

        time.sleep(3)

        driver.quit()

if __name__ == "__main__":
    # Load tests and specify their order
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Hosttest)
    tests = [
        test_suite.testHomePage,
        test_suite.testCreatingAssigningTask,
        test_suite.testUpdatingViewingTask,
        test_suite.testDeletingTask
    ]
    
    # Run the tests
    suite = unittest.TestSuite(tests)
    unittest.TextTestRunner(verbosity=2).run(suite)