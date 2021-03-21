import requests
def convert_url_img(urls):
	url="https://webpagetopdf999.herokuapp.com/api/render?output=screenshot&url="+urls
	response = requests.get(url)
	path = "tmp/google.png"
	with open('tmp/google.png', 'wb+') as f:
		f.write(response.content)
	return path

def convert_url_pdf(urls):
	url="https://webpagetopdf999.herokuapp.com/api/render?url="+urls+"&scrollPage=true"
	response = requests.get(url)
	path = "tmp/google.pdf"
	with open('tmp/google.pdf', 'wb+') as f:
		f.write(response.content)
	return path