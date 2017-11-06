import webbrowser


base_url = 'https://api.whatsapp.com/send?phone='

phone_number = 447449737838

message = 'I am interested in your car for sale'

split_message = message.split(' ')

urlformatted_msg = ''

for msg_chunk in split_message:
	urlformatted_msg = urlformatted_msg + msg_chunk + '%20'

final_url = base_url + str(phone_number) + '&text=' + urlformatted_msg

webbrowser.open(final_url) 


