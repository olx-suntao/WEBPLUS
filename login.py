import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://capouwebplusdoubleluck-test-app-dev.azurewebsites.net/#/')
time.sleep(5)
# 要素を取得してキーボード入力
driver.find_element(By.ID, 'input-9').send_keys("10001")
time.sleep(2)
driver.find_element(By.ID, 'input-10').send_keys('0002')
time.sleep(2)
driver.find_element(By.ID, 'input-11').send_keys('00102')
time.sleep(2)
driver.find_element(By.ID, 'input-12').send_keys('DLtest02')
time.sleep(2)
# ログインボタンをクリック
driver.find_element(By.XPATH, '//*[@id="inspire"]/div/main/div/div/div/div/div[2]/div[6]/div[2]/button').click()
time.sleep(2)