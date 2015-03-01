import requests
from BeautifulSoup import BeautifulSoup as bs

def scrape():

    # URL for i-league
    URL="http://www.goal.com/en-india/tables/i-league/150?ICID=TA"

    # Get the page
    page = requests.get(URL)

    # Instantiate a soup wrapper around it
    soup = bs(page.text)

    # Fetch the FIRST table and inside that, the FIRST(duh) tbody
    tbody = soup.find("table").find("tbody")

    clubs = tbody.findAll("tr")

    # Table
    table = ""

    # Headers
    table += "Team|P|GD|Pts\n"
    table += "----|-|--|---\n"

    # Go through the list of clubs
    for club in clubs:

        club_name = club.find("td", {"class":"flag"}).find("a")["title"]


        pts = club.findAll("td")[4].text
        p = club.findAll("td")[5].text
        w = club.findAll("td")[6].text
        d = club.findAll("td")[7].text
        l = club.findAll("td")[8].text
        gd = club.find("td", {"class":"always-ltr"}).text

        # Print the info in markdown format
        table += "%s|%s|%s|%s\n" % (club_name, p, gd, pts)

    #END for

    return table
