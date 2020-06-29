from selenium import webdriver


def get_element(driver,method,value):
    if method=="id":
        elm = driver.find_element_by_id(value)
        return elm
    elif method=="xpath":
        elm = driver.find_element_by_xpath(value)
        return elm
    elif method=="name":
        elm = driver.find_element_by_name(value)
        return elm


