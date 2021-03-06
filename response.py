import requests, json
def sample_responses(input_text):
	user_message = str(input_text).lower()
	print(user_message)
	new_data = user_message
	pin = 507
	date = new_data
	try:
		pin = int(pin)
	except Exception as e:
		pass
	if(int(pin)<10000 and int(pin)>0):
		url = f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={pin}&date={date}'
		browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
		print(url)
		response = requests.get(url, headers=browser_header)
		print(response)
		json_data = response.json()
		final_text = ''
		if len(json_data['sessions'])==0:
			final_text=final_text + "NII H SLOTS, JAO PROTEST KRO!"
		else:
			for slots in json_data['sessions']:
				final_text = final_text + "\nName: "+str(slots['name']) +'\n'+ "Available Capacity: "+str(slots['available_capacity']) +'\n' + "Min Age Limit: "+str(slots['min_age_limit']) +'\n' + "Vaccine: "+str(slots['vaccine'])+ '\n'
				final_text = final_text + '----------------------------------------'
			final_text = final_text + "OR SLOTS NI H...JAO PROTEST KRO.. "
		return final_text
	else:
		return "Invalid input"