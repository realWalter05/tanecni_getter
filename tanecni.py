import requests
from bs4 import BeautifulSoup
import os
import datetime


URL = "https://www.centrumkultury.cz/event/571509/venecek-tanecnich-kurzu-c"
#URL = "https://www.centrumkultury.cz/event/571580/venecek-tanecnich-kurzu-a"

def get_buy_btn():
	print("requesting buy-btn")
	# Request the page
	page = requests.get(URL)

	# Parse is to beautiful soup
	soup = BeautifulSoup(page.content, "html.parser")
	buy_btn = soup.find("span", {"class": "btn-buy"})
	return buy_btn


def open_browser(buy_btn):
	# If buy button already apperead, open it in browser
	ticket_link = buy_btn.parent["href"]
	os.startfile(ticket_link)


if __name__ == "__main__":
	# Setting the times
	start_time = datetime.datetime(2022, 3, 22, 17, 59, 40)

	while start_time > datetime.datetime.now():
		continue 

	print("Getting tanecni buy-btn quuickly xDd")

	buy_btn = None
	while not buy_btn:
		buy_btn = get_buy_btn()

	if buy_btn:
		open_browser(buy_btn)
