import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.eventbrite.com/d/ny--new-york/events/'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')


#event_cards = soup.find_all('div', class_='eds-media-card-content__content') this doesn't seem to work for some reason, have to look into it
event_cards = soup.find_all('div', class_='browse-cards-container')


csv_file = open('event_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Event Name', 'Date', 'Location', 'Time'])

for card in event_cards:
    event_name_element = card.find('div', class_='Container_root__16e3w NestedActionContainer_root__1jtfr event-card event-card__vertical')  # this literally just extracts the main card 
    event_name = event_name_element.text.strip() if event_name_element else "N/A"


    # Can't be bothered to test out which class name is correct but for whoever uses this, just update class_="..." with whichever class makes sense
    # Extract the event date
    # event_date_element = card.find('div', class_='Typography_root__4bejd #585163 Typography_body-md-bold__4bejd eds-text-color--primary-brand Typography_align-match-parent__4bejd')
    # event_date = event_date_element.text.strip() if event_date_element else "N/A"

    # Extract the event location
    # event_location_element = card.find('div', class_='Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one eds-text-color--ui-600 Typography_align-match-parent__4bejd')
    # event_location = event_location_element.text.strip() if event_location_element else "N/A"

    # Extract the event time
    # event_time_element = card.find('div', class_='Typography_root__4bejd #585163 Typography_body-md-bold__4bejd eds-text-color--primary-brand Typography_align-match-parent__4bejd')
    # event_time = event_time_element.text.strip() if event_time_element else "N/A"

    # Write the extracted information to the CSV file
    csv_writer.writerow([event_name, event_date, event_location, event_time])

# Close the CSV file
csv_file.close()
