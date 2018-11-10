#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string
import random
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

class testing():
    def signup(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/register/')
        name=''.join(random.sample(string.ascii_letters + string.digits, 8))
        pwd=''.join(random.sample(string.ascii_letters + string.digits, 8))
        e1=''.join(random.sample(string.ascii_letters + string.digits, 8))
        e2=e1+"@gmail.com"
        username=self.driver.find_element_by_id("id_username")
        username.send_keys(name)
        password=self.driver.find_element_by_xpath('//*[@id="id_password1"]')
        password.send_keys(pwd)
        confirm=self.driver.find_element_by_xpath('//*[@id="id_password2"]')
        confirm.send_keys(pwd)
        email=self.driver.find_element_by_xpath('//*[@id="id_email"]')
        email.send_keys(e2)
        s=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        s.click()
        self.driver.close()

        
    def createRecipe(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('TestingAccount')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("@kmitl2018")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get('http://127.0.0.1:8000/recipes/search/')
        create=self.driver.find_element_by_css_selector('body > div > div > div.col-sm-8 > div:nth-child(1) > a')
        create.click()
        recipe_name=self.driver.find_element_by_xpath('//*[@id="id_recipe_initial-title"]')
        recipe_name.send_keys("Fried rice with ice-cream.")
        about=self.driver.find_element_by_xpath('//*[@id="id_recipe_initial-description"]')
        about.send_keys("Very delicious.")
        calories=self.driver.find_element_by_xpath('//*[@id="id_recipe_initial-calories"]')
        calories.send_keys("200")
        prepare_time=self.driver.find_element_by_xpath('//*[@id="id_recipe_initial-prep_time"]')
        prepare_time.send_keys("10")
        serving_size=self.driver.find_element_by_xpath('//*[@id="id_recipe_initial-serving"]')
        serving_size.send_keys('5')
        ingredients=self.driver.find_element_by_xpath('//*[@id="id_ingredients-0-text"]')
        ingredients.send_keys("Rice, ice-cream,salt,oil.")
        directions=self.driver.find_element_by_xpath('//*[@id="id_directions-0-text"]')
        directions.send_keys("Just fry.")
        category=Select(self.driver.find_element_by_xpath('//*[@id="id_category-0-title"]'))
        category.select_by_index(3)
        submit=self.driver.find_element_by_css_selector('#create-form > div > div:nth-child(1) > button')
        submit.click()
        self.driver.close()

        
    def searchmovie(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('TestingAccount')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("@kmitl2018")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get('http://127.0.0.1:8000/movies/browse/')
        ipt=self.driver.find_element_by_css_selector('body > div.first-part > div > ul > form > li > input')
        ipt.send_keys("Titanic")
        time.sleep(1)
        search=self.driver.find_element_by_css_selector('  body > div.first-part > div > ul > form > button')
        search.click()
        self.driver.close()

        
    def privateMessage(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('nicky1997')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("ttylakers24")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get("http://127.0.0.1:8000/accounts/profile/TestingAccount/")
        text=self.driver.find_element_by_xpath('//*[@id="id_post"]')
        text.send_keys("How is it going?")
        post_button=self.driver.find_element_by_css_selector('#profile-post > button')
        post_button.click()
        
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('TestingAccount')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("@kmitl2018")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get('http://127.0.0.1:8000/accounts/profile/TestingAccount/')
        reply=self.driver.find_element_by_css_selector('#message-output > div:nth-child(1) > div > div > div.col-sm-11 > div:nth-child(1) > div > div:nth-child(5) > a')
        reply.click()
        text1=self.driver.find_element_by_xpath('//*[@id="id_reply"]')
        text1.send_keys("I am fine.")
        reply_button=self.driver.find_element_by_css_selector('#message-output > div:nth-child(1) > div > div > div.col-sm-11 > div:nth-child(1) > div > div.reply-box > form > button')
        reply_button.click()
        self.driver.close()

        
    def review_book(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('TestingAccount')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("@kmitl2018")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get('http://127.0.0.1:8000/books/browse/')
        target=self.driver.find_element_by_css_selector('body > div.sec-part > ul > li > div > span > span > a > button')
        target.click()
        rating=self.driver.find_element_by_css_selector('body > div > div.ment > div > form > div > div:nth-child(1) > div.col-sm- > div > label.star.star-5')
        rating.click()
        review_text=self.driver.find_element_by_xpath('//*[@id="myTextarea"]')
        review_text.send_keys("Very fun!")
        submit=self.driver.find_element_by_css_selector('body > div > div.ment > div > form > div > div:nth-child(1) > div.col > button')
        submit.click()
        self.driver.close()

        
    def create_book_and_delete_book(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.get('http://127.0.0.1:8000/accounts/login/?next=/sites/home/')
        username=self.driver.find_element_by_xpath('//*[@id="username"]')
        username.send_keys('TestingAccount')
        pwd=self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd.send_keys("@kmitl2018")
        login=self.driver.find_element_by_css_selector('body > div > div > div > form > button')
        login.click()
        self.driver.get('http://127.0.0.1:8000/books/browse/')
        create_book=self.driver.find_element_by_css_selector('body > div.first-part > div > ul > form > a > button')
        create_book.click()
        ISBN=self.driver.find_element_by_xpath('//*[@id="id_isbn"]')
        ISBN.send_keys('978-0-511-39341-9')
        Book_name=self.driver.find_element_by_xpath('//*[@id="id_book_name"]')
        Book_name.send_keys('Distributed ComputingPrinciples, Algorithms, and Systems')
        Author=self.driver.find_element_by_xpath('//*[@id="id_author"]')
        Author.send_keys('Ajay D. Kshemkalyani&Mukesh Singhal')
        Genre=Select(self.driver.find_element_by_xpath('//*[@id="id_genre"]'))
        Genre.select_by_index(9)
        upload_cover=self.driver.find_element_by_xpath('//*[@id="id_book_cover"]')
        image_path=str(os.getcwd())+"\\textbook.png" 
        upload_cover.send_keys(image_path)
        create_button=self.driver.find_element_by_css_selector('      body > div.info > div > div > div > form > button')
        create_button.click()
        time.sleep(2)
        delete_button=self.driver.find_element_by_css_selector('        body > div > div.row.row-set > div > div > form > button')
        delete_button.click()
        self.driver.close()

        
        

                
                                            
        
if __name__=="__main__":
    a=testing()
    a.signup()
    print("Test 1")
    
    b=testing()
    b.createRecipe()
    print("Test 2")
    
    c=testing()
    c.searchmovie()
    print("Test 3")
    
    d=testing()
    d.privateMessage()
    print("Test 4")
    
    e=testing()
    e.review_book()
    print("Test 5")
    
    f=testing()
    f.create_book_and_delete_book()
    print("Test 6")



    
    
