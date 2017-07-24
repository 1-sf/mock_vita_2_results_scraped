from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import pandas as pd

def scraper():
	res_url = 'http://www.tcscodevita.com/CodevitaV6/result.jsp'
	res_page = urlopen(res_url)
	
	soup = BeautifulSoup(res_page)
	tables = soup.findAll('table')
	table = tables[-2]
	
	tbody = table.find('tbody')
	rows = tbody.findAll('tr')
	
	res_list = list()
	
	for tr in rows:
		cols = tr.findAll('td')
		record = list()
		for td in cols:
			record.append(td.text)
		res_list.append(tuple(record))
		
	return res_list
	
res_list = scraper()

labels = ['Rank', 'User Name', 'TCS Region', 'College Name']

df = pd.DataFrame.from_records(res_list, columns=labels)
df.to_csv('tcs_mock_vita_2_results.csv')
