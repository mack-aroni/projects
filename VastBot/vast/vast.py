import vast.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Vast(webdriver.Chrome):
    def __init__(self, driver_path = const.DRIVER_PATH, teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown

        os.environ["PATH"] += self.driver_path
        super(Vast, self).__init__()
        self.implicitly_wait(1)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_page(self):
        self.get(const.URL)
        wait = WebDriverWait(self, 10)
        try:
            first_name = wait.until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/div/div[1]/div[5]/div[2]/div[2]/div/form/fieldset[2]/div[2]/div/div/div[1]/label/div[2]/input"))
            )
            first_name.clear()
            first_name.send_keys(const.FIRST_NAME)
        except: 
            pass