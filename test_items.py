from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestItems:
    def test_product_add_button_is_available(self, browser):
        browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(@class,'btn-add-to-basket')]")))
        assert browser.find_element(By.XPATH, "//button[contains(@class,'btn-add-to-basket')]"), 'No button'
