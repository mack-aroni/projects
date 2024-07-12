import booking.constants as const
import os
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("includeSwitches", ["enable-logging"])
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
                By.CSS_SELECTOR, "[aria-label='Dismiss sign-in info.']"
            )
            button.click()
        except:
            print("No Dismiss Sign-In Button")

    # selects currency
    def select_currency(self, currency):
        # find and click currency selector button
        currency_selector = self.find_element(
            By.CSS_SELECTOR, "[aria-label='Prices in U.S. Dollar']"
        )
        currency_selector.click()
        # find and click selected currency
        selected_currency_element = self.find_element(
            By.XPATH,
            f"//button[.//div[contains(text(),'{currency}')]]",
        )
        selected_currency_element.click()

    # selects intended destination
    def select_destination(self, destination):
        # inputs destination
        destination_field = self.find_element(By.ID, ":re:")
        destination_field.clear()
        destination_field.send_keys(destination)
        # clicks first autocomplete result
        confirm_destination_element = self.find_element(By.ID, "autocomplete-result-0")
        confirm_destination_element.click()

    # helper function to parse a string date into a date object
    def __parse_date(self, str_date):
        temp = str_date.split("-")
        year = int(temp[0])
        month = int(temp[1])
        day = int(temp[2])
        parsed_date = date(year, month, day)
        return parsed_date

    # helper function to properly return the number of next_button presses
    def __date_count(self, startDate, endDate):
        count = 0
        count += 12 * (endDate.year - startDate.year)
        count += endDate.month - startDate.month
        return count - 1

    # selects check-in and check-out dates
    def select_dates(self, checkin, checkout):
        # find the next month button
        next_button = self.find_element(By.CSS_SELECTOR, "[aria-label='Next month']")

        # find the number of clicks to reach the checkin date
        count = self.__date_count(date.today(), self.__parse_date(checkin))
        while count > 0:
            next_button.click()
            count -= 1

        # find and select check-in date element
        checkin_element = self.find_element(
            By.XPATH, f"//td[./span[@data-date='{checkin}']]"
        )
        checkin_element.click()

        # determine the number of clicks to reach the checkout date
        count = self.__date_count(
            self.__parse_date(checkin), self.__parse_date(checkout)
        )
        while count > 0:
            next_button.click()
            count -= 1

        # find and select check-out date element
        checkout_element = self.find_element(
            By.XPATH, f"//td[./span[@data-date='{checkout}']]"
        )
        checkout_element.click()

    # selects the number of adults and rooms desired
    def select_adults_rooms(self, adults, rooms):
        # selects person and room element
        selector_element = self.find_element(
            By.CSS_SELECTOR, "[data-testid='occupancy-config']"
        )
        selector_element.click()

        # find increment buttons (0-2)
        increment_buttons = self.find_elements(By.CLASS_NAME, "f4d78af12a")

        # increments adults to desired amount
        adults_field = self.find_element(By.ID, "group_adults")
        while int(adults_field.get_attribute("value")) < adults:
            increment_buttons[0].click()

        # increments rooms to desired amount
        rooms_field = self.find_element(By.ID, "no_rooms")
        while int(rooms_field.get_attribute("value")) < rooms:
            increment_buttons[2].click()

    # selects the number of children and their ages
    def select_children(self, children, ages):
        # find increment buttons (0-2)
        increment_buttons = self.find_elements(By.CLASS_NAME, "f4d78af12a")

        # increments children to desired amount
        children_field = self.find_element(By.ID, "group_children")
        while int(children_field.get_attribute("value")) < children:
            increment_buttons[1].click()

        # inputs ages for each child
        age_elements = self.find_elements(By.CSS_SELECTOR, "[name='age']")
        for i in range(len(age_elements)):
            age_elements[i].click()
            age_element = age_elements[i].find_element(
                By.CSS_SELECTOR, f"[value='{ages[i]}']"
            )
            age_element.click()

    # click search button and wait for subsequent page to load
    def search(self):
        search_button = self.find_element(By.CSS_SELECTOR, "[type='submit']")
        search_button.click()
        time.sleep(1)

    # applies
    def apply_filters(self):
        rating_div = self.find_element(
            By.CSS_SELECTOR, "[data-testid='filters-sidebar']"
        )
        rating_elements = rating_div.find_elements(By.CSS_SELECTOR, "[data-testid]")
        print(len(rating_elements))

        time.sleep(5)
