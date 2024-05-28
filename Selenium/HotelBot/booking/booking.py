import booking.constants as const
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        # self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # opens landing page and closes signin popup
    def land_first_page(self):
        self.get(const.LANDING_URL)
        # lets page fully load
        time.sleep(1)
        # closes signin popup if necessary
        try:
            button = self.find_element(
                By.CSS_SELECTOR, '[aria-label="Dismiss sign-in info."]'
            )
            button.click()
        except:
            print("No Dismiss Sign In Button")

    # changes currency
    def change_currency(self, currency):
        # find and click currency selector button
        currency_selector = self.find_element(
            By.CSS_SELECTOR, '[aria-label="Prices in U.S. Dollar"]'
        )
        currency_selector.click()
        # find and click selected currency
        selected_currency_element = self.find_element(
            By.XPATH,
            f"//button[.//div[contains(text(),'{currency}')]]",
        )
        selected_currency_element.click()

    # change intended destination
    def change_destination(self, destination):
        # inputs destination
        destination_field = self.find_element(By.ID, ":re:")
        destination_field.clear()
        destination_field.send_keys(destination)
        # clicks first autocomplete result
        confirm_destination_element = self.find_element(By.ID, "autocomplete-result-0")
        confirm_destination_element.click()

        time.sleep(10)
