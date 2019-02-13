#authored by jgam
"""
possible db variables!

"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#from lxml import html
#import requests
import csv
import os
#import pandas as pd
#from pandas import ExcelWriter
#from pandas import ExcelFile
#import numpy as np
import xlwt
from datetime import date



today = str(date.today())


def sel_suggest(keywords, file_name, work_book):
	#ff = csv.writer(open(result_dir+file_name, "a+"))
	file_name = file_name[:len(file_name)-4]
	driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
	driver.get('https://searchad.naver.com/login?returnUrl=https:%2F%2Fmanage.searchad.naver.com%2Fcustomers%2F760223%2Ftool%2Fkeyword-planner')
	#here we should use a for loop
	driver.find_element_by_name('id').send_keys('ascentnet')
	driver.find_element_by_name('pw').send_keys('1qazxsw2')
	driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/span/button').click()
	time.sleep(5)
	columns = 1
	sheet_name = 'hong-sam'+keywords[0]
	work_sheet = work_book.add_sheet(sheet_name)
	ret_list = []
	
	for keyword in keywords:
		key_list = []
		continue_condition = False
		key_list.append(keyword)
		driver.find_element_by_class_name('form-control').clear()
		#<textarea class="form-control ng-pristine ng-valid ng-empty ng-valid-maxlength ng-touched" ng-disabled="!vm.hints.use.keyword" ng-model="vm.hints.keyword.str" rows="5" ng-attr-placeholder="{{ &quot;TOOL.TERM.RELATIONAL_KEYWORD_HINT&quot; | translate | striptags }}" autofocus="" spellcheck="false" maxlength="250" data-input-composition="" placeholder="Enter one by one in each line (max.5)" style=""></textarea>
		driver.find_element_by_class_name('form-control').send_keys(keyword)
		#<span translate="" class="ng-scope">Search</span>
		time.sleep(1)
		driver.find_element_by_class_name('btn-primary').click()
		time.sleep(2)

		#keyword case conversion
		for i in range(len(keyword)):
			if keyword[i].isalpha():
				keyword = keyword.swapcase()
				break
				"""
				if keyword[i].islower():
					#make it upper
					keyword[i] = keyword[i].upper()
				else:
					continue
			else:
				continue
				"""
		#now the keyword is searched what is the search volumes

		#//*[@id="wgt-세그윗"]/td[3]
		#//*[@id="wgt-세그윗"]/td[3]

		#//*[@id="wgt-BANG"]/td[3]
		#//*[@id="wgt-BANG"]/td[4]
		#//*[@id="wgt-BANG"]/td[8]
		for i in range(3,9):
			#//*[@id="wgt-세그윗"]/td[3]
			time.sleep(4)

			try:
				each_col = driver.find_element(By.XPATH, '//*[@id="wgt-'+keyword.replace(" ","")+'"]/td['+str(i)+']')
			except:
				continue_condition = True
				break
			
			key_list.append(each_col.text)
		#write to excel file
		#key_list contains volumes for keyword
		if continue_condition:
			driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
			driver.get('https://searchad.naver.com/login?returnUrl=https:%2F%2Fmanage.searchad.naver.com%2Fcustomers%2F760223%2Ftool%2Fkeyword-planner')
			#here we should use a for loop
			driver.find_element_by_name('id').send_keys('ascentnet')
			driver.find_element_by_name('pw').send_keys('1qazxsw2')
			driver.find_element_by_xpath('//*[@id="container"]/div/div/fieldset/span/button').click()
			#driver.get('https://manage.searchad.naver.com/customers/760223/tool/keyword-planner')
			time.sleep(10)
			continue
		else:
			for row, item in enumerate(key_list):
				work_sheet.write(row, columns, item)
			#ret_list.append(key_list)
			columns+=1
	"""
	for keyword in keywords:
		suggest_list = []
		suggest_list.append(keyword)
		if keyword[-1] == '_':
			keyword = keyword.replace('_',' ')
		print(keyword)
		sheet_name =str(columns)
		search = driver.find_element_by_name('q')
		search.send_keys(keyword)
		print('time sleep')
		time.sleep(5)
		while_cond = True
		child_index = 1
		

		while while_cond:
			try:
				#print('should be here 8 times')
				added = driver.find_element(By.XPATH, '//*[@id="tsf"]/div[2]/div/div[2]/div[2]/ul/li['+str(child_index)+']/div[1]/div/span')
				added_word = added.text
				#print(added_word)
				suggest_list.append(added_word)
				child_index += 1
			except:
				print('end of child_index and done')
				while_cond = False
		
		#also erase the search keyword in a search keyword tab.
		search.clear()
		#this needs to be written in a column of excel
		
		
		

		for row, item in enumerate(suggest_list):
			work_sheet.write(row, columns, item)

		columns += 1
		
		print(suggest_list)
	"""
	return 0




#get the list of all the keywords.


files = [f for f in os.listdir('.') if os.path.isfile(f)]
#open the excel file here with bunch of tabs
work_book = xlwt.Workbook()


for file in files:
	today = str(date.today())
	if file[len(file)-4:len(file)] != '.csv':
		continue

	real_keywords = []
	file_name = ''
	file_name = today + str(file)[:len(file)-4]+'_naverVolume_results.csv'
	with open(file) as f:
		reader = csv.reader(f)
		for i in reader:
			real_keywords.append(i[0])
	
	
	print(real_keywords)
	sel_suggest(real_keywords, file_name, work_book)
	work_book.save(file_name)


	
