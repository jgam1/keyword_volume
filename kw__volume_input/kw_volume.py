import json
import requests
import csv
import time
import os
import shutil

undone_keywords = []

row_name = ["search_keyword",
			"cmp",
            "cpc",
            "m1",
            "m10",
            "m10_month",
            "m10_year",
            "m11",
            "m11_month",
            "m11_year",
            "m12",
            "m12_month",
            "m12_year",
            "m1_month",
            "m1_year",
            "m2",
            "m2_month",
            "m2_year",
            "m3",
            "m3_month",
            "m3_year",
            "m4",
            "m4_month",
            "m4_year",
            "m5",
            "m5_month",
            "m5_year",
            "m6",
            "m6_month",
            "m6_year",
            "m7",
            "m7_month",
            "m7_year",
            "m8",
            "m8_month",
            "m8_year",
            "m9",
            "m9_month",
            "m9_year",
            "string",
            "volume"
            ]

def testing(keywordsss,file_name,number):
	dict_keys_list = []
	apikey = '23d330113804a91b2d795143b20f05e84a074872'
	apiurl = 'https://api.keywordtool.io/v2/search/volume/google'
	apiparams = {
	    'apikey': apikey, 
	    'keyword': json.dumps(keywordsss), 
	    'metrics_location': '',#2840-America, 2410-korea 2392-japan
	    'metrics_language': '',#en-english, ko-korean ja-japanese
	    'metrics_network': 'googlesearchnetwork',
	    'metrics_currency': 'USD',
	    'output': 'json'
	}
	response = requests.post(apiurl, data=apiparams)
	while_cond = True
	#if response~~~== 200
	max_while = 0
	if response.status_code != 200:
		print('response body', response.content)
		#print(response.content[20:40])
		#print(type(response.content))
		if response.content.decode('utf-8') == '{"error":{"message":"Sorry, you have reached your daily limit of searches. Please try again another day.","code":9}}':
			return 2
	#while_count = 0
	while while_cond:

		if response.status_code == 200:
		    deff = json.dumps(response.json(), indent=4, sort_keys=True)
		    #print(deff)
		    deff = json.loads(deff)
		    #print('the deff: ', deff)
		    
		    #print(deff['results'])
		    dict_keys = deff['results'].keys()
		    dict_keys_list = [key for key in dict_keys]
		    result_dir = '../results/'
		    ff = csv.writer(open(result_dir+file_name, "a+"))
		    if first_cond:
			    ff.writerow(row_name)#list that tells you row name
		    count = 0
		    print(dict_keys_list[:10])
		    #print(len(dict_keys_list))
		    #print(len(keywordsss))
		    #print(deff['results'][dict_keys_list[count]][row_name[40]])
		    
		    print('year shouldnt be none: ', deff['results'][dict_keys_list[count]][row_name[38]])
		    
		    if max_while > 3:
		    	print('respons status!!', response.status_code)
		    	print('response body', response.content)
		    	undone_keywords.append(str(number))
		    	max_while=0
		    	return 2
		    elif deff['results'][dict_keys_list[count]][row_name[38]] == None:
		    	print('the output was none but continued!')
		    	max_while += 1
		    	print(max_while, 'times the while loop has been run!')
		    	continue

		    if deff['results'][dict_keys_list[count]][row_name[38]] == None:
		    	print('the output was none but continued!')
		    	undone_keywords.append(str(number))
		    	continue

		    ret_total = []
		    for count in range(0,len(dict_keys_list)):
		    	for i in range(1,13):
		    		total_volume = deff['results'][dict_keys_list[count]]['m'+str(i)]
		    	ret_total.append(total_volume)
		    		# add all the data

		    	ff.writerow([dict_keys_list[count],
		    				 deff['results'][dict_keys_list[count]][row_name[1]],
		    				 deff['results'][dict_keys_list[count]][row_name[2]],
		    				 deff['results'][dict_keys_list[count]][row_name[3]],
		    				 deff['results'][dict_keys_list[count]][row_name[4]],
		    				 deff['results'][dict_keys_list[count]][row_name[5]],
		    				 deff['results'][dict_keys_list[count]][row_name[6]],
		    				 deff['results'][dict_keys_list[count]][row_name[7]],
		    				 deff['results'][dict_keys_list[count]][row_name[8]],
		    				 deff['results'][dict_keys_list[count]][row_name[9]],
		    				 deff['results'][dict_keys_list[count]][row_name[10]],
		    				 deff['results'][dict_keys_list[count]][row_name[11]],
		    				 deff['results'][dict_keys_list[count]][row_name[12]],
		    				 deff['results'][dict_keys_list[count]][row_name[13]],
		    				 deff['results'][dict_keys_list[count]][row_name[14]],
		    				 deff['results'][dict_keys_list[count]][row_name[15]],
		    				 deff['results'][dict_keys_list[count]][row_name[16]],
		    				 deff['results'][dict_keys_list[count]][row_name[17]],
		    				 deff['results'][dict_keys_list[count]][row_name[18]],
		    				 deff['results'][dict_keys_list[count]][row_name[19]],
		    				 deff['results'][dict_keys_list[count]][row_name[20]],
		    				 deff['results'][dict_keys_list[count]][row_name[21]],
		    				 deff['results'][dict_keys_list[count]][row_name[22]],
		    				 deff['results'][dict_keys_list[count]][row_name[23]],
		    				 deff['results'][dict_keys_list[count]][row_name[24]],
		    				 deff['results'][dict_keys_list[count]][row_name[25]],
		    				 deff['results'][dict_keys_list[count]][row_name[26]],
		    				 deff['results'][dict_keys_list[count]][row_name[27]],
		    				 deff['results'][dict_keys_list[count]][row_name[28]],
		    				 deff['results'][dict_keys_list[count]][row_name[29]],
		    				 deff['results'][dict_keys_list[count]][row_name[30]],
		    				 deff['results'][dict_keys_list[count]][row_name[31]],
		    				 deff['results'][dict_keys_list[count]][row_name[32]],
		    				 deff['results'][dict_keys_list[count]][row_name[33]],
		    				 deff['results'][dict_keys_list[count]][row_name[34]],
		    				 deff['results'][dict_keys_list[count]][row_name[35]],
		    				 deff['results'][dict_keys_list[count]][row_name[36]],
		    				 deff['results'][dict_keys_list[count]][row_name[37]],
		    				 deff['results'][dict_keys_list[count]][row_name[38]],
		    				 deff['results'][dict_keys_list[count]][row_name[39]],
		    				 deff['results'][dict_keys_list[count]][row_name[40]]
		    				 ])
		    while_cond = False
		    #print(ret_total)
		else:
			print('error occurred and need to be refractored here')
			print('check the line!')
			while_cond = False
			#this needs to be checked.
	return 1
	    #return json.dumps(response.json(), indent=4, sort_keys=True)
#print(keywords[-9:])
#keywords = ['abc mart','adidas','nike','ascics','onitsuka tiger']


files = [f for f in os.listdir('.') if os.path.isfile(f)]
#files = 'ipad 6 7.csv'
for file in files:
	#time.sleep(60)
	print(file)
	if file[len(file)-4:len(file)] != '.csv':
		continue
	file_name = ''
	file_name = str(file)[:len(file)-4]+'_results.csv'
	print(file_name)
	keywords = []
	first_cond = True
	with open(file) as f:
		reader = csv.reader(f)
		for i in reader:
			if len(i[0]) > 80:
				i[0] = i[0][:80]
			keywords.append(i[0])
	#print(reader[:10])

	num_loops = len(keywords) //800#check
	start_num = 0#this was 0 originally
	ret_list = []
	while_count = 0
	file_name = str(file)[:len(file)-4]+'_results.csv'
	print('file_name is: ',file_name)
	#the error occurred at 13, 33, 38
	for number in range(1, num_loops+1):
		print("******************")
		print('the quota number is : ', number)
		#need to implement the last one by subtracting the last num
		end_num = number * 800
		#if start_num >= 8000:
		while_count += 1
		while testing(keywords[start_num:end_num],file_name, number) != 1:
			print('the real while loop...please get the right resultsls and quota num is: ',number)
			continue
		first_cond = False
		if while_count % 10 == 0:
			time.sleep(60)
		#ret_list.append(returned)
		start_num=end_num

	if len(keywords) - start_num >0:
		testing(keywords[start_num:len(keywords)],file_name,num_loops+1)
		#ret_list.append(returned)
	shutil.move("/Users/ascent/Desktop/keyword_volume/kw__volume_input/"+str(file), "/Users/ascent/Desktop/keyword_volume/done_files/")

	print(ret_list)
	print(undone_keywords)

