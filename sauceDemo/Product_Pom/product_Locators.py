from selenium.webdriver.common.by import By


class productLocators(object):
    ptitle =(By.XPATH, '//*[@id="item_4_title_link"]/div')
    desc=(By.XPATH,"//div[@class='inventory_details_desc large_size']")
    price=(By.XPATH,"//div[@class='inventory_details_price']")
