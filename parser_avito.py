from selenium import webdriver  # библиотека
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class Parser:
    def __init__(self) -> None:
        options = webdriver.EdgeOptions()
        options.headless = True  # включение фонового режима
        self.browser = webdriver.Edge(service=EdgeService(
            EdgeChromiumDriverManager().install()), options=options)
        self.browser.maximize_window()

    def __start__(self, url: str) -> None:  # переход на главную страницу
        self.browser.get(url=url)

    def __end__(self) -> None:
        self.browser.quit()

    def __back__(self) -> None:
        self.browser.back()

    def __ref__(self) -> None:  # перезагрузка страницы
        self.browser.refresh()

    def __next__(self) -> None:
        next = self.browser.find_element(
            By.CSS_SELECTOR, "span[class='pagination-item-JJq_j pagination-item_arrow-Sttbt']")
        next.location_once_scrolled_into_view
        next.click()

    def __closes__(self) -> None:
        self.browser.close()  # закрытие вкладки и переход на основную вкладку
        self.browser.switch_to.window(self.browser.window_handles[0])

    def __win_too__(self) -> None:  # переход на вторую вкладку
        self.browser.switch_to.window(self.browser.window_handles[1])

    def __scroll__(self, number: int) -> None:
        self.browser.execute_script(f"window.scrollTo(0,{number})")

    def __city__(self, city: str) -> None:  # функция смены города на выбранный пользователем
        self.browser.find_element(
            By.CSS_SELECTOR, ".main-select-JJyaZ.main-location-XUs1_").click()
        self.browser.find_element(
            By.CSS_SELECTOR, "input[placeholder='Город или регион']").send_keys((f"{city}"))
        time.sleep(5)
        parametr = self.browser.find_element(
            By.CSS_SELECTOR, ".suggest-suggests-CzXfs")
        parametr.find_element(By.TAG_NAME, "li").click()
        time.sleep(2)
        self.browser.find_element(
            By.CSS_SELECTOR, ".button-button-CmK9a.button-size-m-LzYrF.button-primary-x_x8w").click()
        time.sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "#category").click()
        parametr = self.browser.find_elements(
            By.CLASS_NAME, "category-select-group-H5Ufe")
        parametr[1].click()
        time.sleep(5)
        self.browser.find_element(By.CSS_SELECTOR, ".desktop-py03yc").click()

    def __perebor__(self, iteration) -> None:  # функция отбора объявлений по очереди
        city = self.browser.find_element(
            By.CSS_SELECTOR, (f"body > div:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > div:nth-child({iteration}) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1) > h3:nth-child(1)"))
        city.location_once_scrolled_into_view
        city.click()

    def __name__(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, ".title-info-title-text")

    def __url__(self):
        return self.browser.current_url

    def __price_full__(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, ".js-item-price.style-item-price-text-_w822.text-text-LurtD.text-size-xxl-UPhmI")

    def __price_sell__(self):
        return self.browser.find_element(
            By.CSS_SELECTOR, "span[class='style-item-line-mix-qV0Mt text-text-LurtD text-size-s-BxGpL'] span")

    def __adres__(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".style-item-address__string-wt61A")

    def __product__(self):
        discription = self.browser.find_element(
            By.CSS_SELECTOR, ".params-paramsList-zLpAu")
        discription = discription.find_elements(By.TAG_NAME, "li")
        return discription
