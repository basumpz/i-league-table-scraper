import requests
from BeautifulSoup import BeautifulSoup as bs

def scrape():

    # URL for i-league
    URL="http://i-league.org/?page_id=1044"

    # Get the page
    page = requests.get(URL)

    # Instantiate a soup wrapper around it
    soup = bs(page.text)

    # Fetch the FIRST table and inside that, the FIRST(duh) tbody
    tbody = soup.find("table").find("tbody")
    
    # Fetch all the td's with the class "club"
    # This contains all the club details
    # All the parent td's have alternating classes - "Even" and "Odd" so what i did
    # was to take the club classes and then work my way upward from there
    clubs = tbody.findAll("td",{"class":"club"})

    # Table
    table = ""

    # Headers
    table += "Team|P|GD|Pts\n"
    table += "----|-|--|---\n"

    # Go through the list of clubs
    for club in clubs:

      # Pick up the club name as the title of the image (logo)
      # Doing this because the content of the td's aren't consistent
      club_name = club.find("img")["title"]

      # Get the parent of the club (this gives us the whole td)
      parent = club.parent

      # From the parent get the required info
      p = parent.find("td",{"class":"p"}).getText()
      gd = parent.find("td",{"class":"gd"}).getText()
      pts = parent.find("td",{"class":"pts"}).getText()

      # Print the info in markdown format
      table += club_name + "|" + p + "|" + gd + "|" + pts + "\n"

    #END for

    return table
