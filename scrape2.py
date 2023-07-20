import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the Eventbrite page
url = 'https://www.eventbrite.com/d/ny--new-york/tech/?page=1'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the event cards on the page

#event_cards = soup.find_all('div', class_='eds-media-card-content__content')
#event_cards = soup.find_all('div', class_='browse-cards-container')
event_cards = soup.find_all('div', class_='Stack_root__1ksk7')
event_links = soup.find_all("a", class_="event-card-link")

# Create a CSV file to store the extracted information
csv_file = open('event_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Event Name', 'Date', 'Location', 'Time', 'Link'])

event_urls = [link["href"] for link in event_links]
#event_urls = list(dict.fromkeys(event_urls))
print(len(event_cards))
print(len(event_urls))
#print(event_urls)

def find_occurrence_positions(input_string, occurrence):
    positions = []
    index = -1

    for x in range(occurrence):
        print(input_string)
        print("------------")
        
        print(type(index))
        indexTemp = input_string.find('"', index + 1)
        
        positions.append(indexTemp)
        print(indexTemp)

    return positions


counter = 0
print(event_cards)

for card in event_cards:
    # Extract the event name
    event_name_element = card.find('div', class_='Stack_root__1ksk7')
    event_name = event_name_element.text.strip() if event_name_element else "N/A"

    # Extract the event date
    event_date_element = card.find('div', class_='Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one eds-text-color--ui-600 Typography_align-match-parent__4bejd')
    event_date = event_date_element.text.strip() if event_date_element else "N/A"

    # Extract the event location
    event_location_element = card.find('div', class_='Typography_root__4bejd')
    event_location = event_location_element.text.strip() if event_location_element else "N/A"

    # Extract the event time
    event_time_element = card.find('div', class_='Typography_root__4bejd #585163 Typography_body-md__4bejd event-card__clamp-line--one eds-text-color--ui-600 Typography_align-match-parent__4bejd')
    event_time = event_time_element.text.strip() if event_time_element else "N/A"

    event_url_element = card.find("a", class_="event-card-link")

    fifth_occurrence = 5
    sixth_occurrence = 6

    fifth_position = find_occurrence_positions(event_url_element, fifth_occurrence)
    sixth_position = find_occurrence_positions(event_url_element, sixth_occurrence)


    position1 = fifth_position[4]
    print(position1)


    position2 = sixth_position[5]
    print(position2)

    event_url = event_url_element[position1:position2 + 1]
    #print("==========")
    #print(type(event_url_element))
    #print("==========")


    # Write the extracted information to the CSV file
    #print(counter)
    #if(counter >= len(event_urls)):
    #    break
    csv_writer.writerow([event_name, event_date, event_location, event_url])
    counter+=1

#print(soup)

# Close the CSV file
csv_file.close()
