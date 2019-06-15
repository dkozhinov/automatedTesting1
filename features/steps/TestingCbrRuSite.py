__author__ = 'Dmitry Kozhinov'

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

@given('website www.google.ru')
def step(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()
    context.browser.get('http://www.google.ru')


@when("push search button with text '{text}'")
def step(context, text):
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='q']"))
    )
    context.browser.find_element_by_xpath('//input[@name="q"]').send_keys(text)
    context.browser.find_element_by_xpath('//input[@name="btnK"]').submit()


@then("displayed page www.google.ru and opened link '{link}'")
def step(context, link):
    my_href = '//a[@href="%s"]' % link
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    # cbr.ru Открываем в том же окне, потому что selenium больше трех вкладок не хочет открывать
    url = context.browser.find_element_by_xpath(my_href).get_attribute("href")
    context.browser.get(url)


@then("on cbr.ru opened link Internet-reception")
def step(context):
    my_href = '//a[contains(.,"Интернет-приемная")]'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    context.browser.find_element_by_xpath(my_href).click()


@then("opened link Write gratitude")
def step(context):
    my_href = '//h2[contains(.,"Написать благодарность")]'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    context.browser.find_element_by_xpath(my_href).click()


@then("write in textarea MessageBody '{text}'")
def step(context,text):
    my_textarea = '//textarea[contains(@name,"MessageBody")]'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_textarea))
    )
    assert context.browser.find_element_by_xpath(my_textarea)
    context.browser.find_element_by_xpath(my_textarea).send_keys(text)



@then("select the checkbox Agreement")
def step(context):
    my_href = '//input[@name="Agreement"]'
    WebDriverWait(context.browser, 20).until(
        EC.element_to_be_clickable((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    context.browser.find_element_by_xpath(my_href).click()



@then("make screenshot")
def step(context):
    context.browser.save_screenshot("screenshot.png")
    time.sleep(10)

#context.browser.quit()
