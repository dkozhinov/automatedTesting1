__author__ = 'Dmitry Kozhinov'

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import time
import smtplib
import os


#Для запомнинания текста предупреждения
save_warning_text = ""

def deletefile(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def sendemail(filename):
    sendemail_host = "smtp.mail.ru"
    sendemail_subject = "Screenshot from automated testing by python"
    sendemail_to_address = "d.kozhinov@mail.ru"
    sendemail_from_address = "mytest19741106@mail.ru"
    sendemail_from_password = "Qwer123$"
    sendemail_text = "This email has been sent automatically. No answer required."

    # Создаем email сообщение
    msg = MIMEMultipart()
    msg['From'] = sendemail_from_address
    msg['To'] = sendemail_to_address
    msg['Subject'] = sendemail_subject

    # Добавляем текст в сообщение
    msg.attach(MIMEText(sendemail_text, 'plain'))

    # Добавляем файл скриншота в сообщение
    if os.path.isfile(filename):
        with open(filename, 'rb') as fp:
            img = MIMEImage(fp.read())
            fp.close()
            msg.attach(img)

    deletefile(filename)

    server = smtplib.SMTP_SSL(sendemail_host, 465)
    server.login(sendemail_from_address, sendemail_from_password)
    server.send_message(msg)
    server.quit()


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



@then("make screenshot and send email")
def step(context):
    screenshot_filename='screenshots\\screenshot.png'
    deletefile(screenshot_filename)
    context.browser.save_screenshot(screenshot_filename)
    sendemail(screenshot_filename)




@then("press the button Three strips")
def step(context):
    my_href = '//span[contains(@class,"burger")]'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    context.browser.find_element_by_xpath(my_href).click()


@then("clicked on the section About")
def step(context):
    my_link_text = 'О сайте'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, my_link_text))
    )
    assert context.browser.find_element_by_link_text(my_link_text)
    context.browser.find_element_by_link_text(my_link_text).click()


@then("clicked link Warning")
def step(context):
    my_link_text = 'Предупреждение'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, my_link_text))
    )
    assert context.browser.find_element_by_link_text(my_link_text)
    context.browser.find_element_by_link_text(my_link_text).click()


@then("save warning text")
def step(context):
    my_id = 'content'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.ID, my_id))
    )
    assert context.browser.find_element_by_id(my_id)
    save_warning_text = context.browser.find_element_by_id(my_id).text
    #print("save_warning_text=", save_warning_text)


@then("changed page language to en")
def step(context):
    my_href = '//a[contains(.,"EN")]'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.XPATH, my_href))
    )
    assert context.browser.find_element_by_xpath(my_href)
    context.browser.find_element_by_xpath(my_href).click()



@then("check warning text is different from the memorized text previously")
def step(context):
    my_id = 'content'
    WebDriverWait(context.browser, 20).until(
        EC.presence_of_element_located((By.ID, my_id))
    )
    assert context.browser.find_element_by_id(my_id)
    assert save_warning_text != context.browser.find_element_by_id(my_id).text, \
        "Aborting test: warning text is equal from the memorized text previously"


@then("end test")
def step(context):
    context.browser.quit()
