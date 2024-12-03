from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest


url = "http://localhost:8080/"


@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Chrome()
    driver.get(url)
    yield driver

def table(driver):
    table = driver.find_element(By.ID, "example")
    return table

def searchbutton(driver):
    searchbutton = driver.find_element(By.ID, "search")
    return searchbutton

def click_button(elem,string,driver,result):
    elem.send_keys(string)
    searchbutton(driver).click()
    assert result in table(driver).text
    elem.clear()
    

def test_loading_table(driver):
    assert "Aarika Plante" in driver.page_source

def test_first_name_field(driver):
    elem = driver.find_element(By.ID, "first_name_input")
    click_button(elem,'Dan',driver,"Scholig")

def test_last_name_field(driver):
    elem = driver.find_element(By.ID, "last_name_input")
    click_button(elem,'Mintoff',driver,"Mintoff")

def test_date_of_birth_field(driver):
    elem = driver.find_element(By.ID, "date_of_birth_input")
    click_button(elem,"05/30/1981",driver,"Addy")

def test_email_field(driver):
    elem = driver.find_element(By.ID, "email_input")
    click_button(elem,"agould18@tuttocitta.it",driver,"Alaster Gould")

def test_phone_field(driver):
    elem = driver.find_element(By.ID, "phone_input")
    click_button(elem,"217-746-9979",driver,"Bradan Gianelli")

def test_address_field(driver):
    elem = driver.find_element(By.ID, "address_input")
    click_button(elem,"96529 Esch Alley",driver,"Amaleta Hadaway")

def test_city_field(driver):
    elem = driver.find_element(By.ID, "city_input")
    click_button(elem,"El Paso",driver,"Alix Bestwerthick")

def test_state_field(driver):
    elem = driver.find_element(By.ID, "state_input")
    
    select = Select(elem)
    select.select_by_visible_text('TX')
    searchbutton(driver).click()
    assert "Adaline Zarfat" in table(driver).text
    select.select_by_visible_text('')

def test_zipcode_field(driver):
    elem = driver.find_element(By.ID, "zipcode_input")
    click_button(elem,"71342",driver,"Adelheid Ratcliff")

def test_contact_selection(driver):
    td_list = driver.find_elements(By.CSS_SELECTOR, "#example tr td")
    for td in td_list:
        if(td.text == "Abbi Hawse"):
            td.click()
    assert 'Abbi Hawse' == driver.find_element(By.ID, "selected_name").text
    assert 'ahawsem7@seesaa.net' == driver.find_element(By.ID, "selected_email").text
    assert '865-771-4794' == driver.find_element(By.ID, "selected_phone").text
    assert '3 Hauk Terrace' == driver.find_element(By.ID, "selected_address").text