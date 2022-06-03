from bs4 import BeautifulSoup
from pycep_correios import get_address_from_cep, WebService
import requests

def getTemperature(CEP):
    address = get_address_from_cep(CEP, webservice=WebService.CORREIOS)
    city = address['cidade']+" temperatura"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    temperature = soup.select('#wob_tm')[0].getText().strip()
    return temperature

# example
# print(getTemperature("90010-170"))