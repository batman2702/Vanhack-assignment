from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dic = {
    'Travel':('travel_2', 1),
    'Mystery':('mystery_3', 2),
    'Historical Fiction':('historical-fiction_4', 2),
    'Sequential Art': ('sequential-art_5', 4),
    'Classics':('classics_6', 1),
    'Philosophy': ('philosophy_7', 1),
    'Romance': ('romance_8', 2),
    'Womens Fiction': ('womens-fiction_9', 1),
    'Fiction': ('fiction_10', 4),
    'Childrens':('childrens_11', 2),
    'Religion':('religion_12',1),
    'Nonfiction':('nonfiction_13',6),
    'Music':('music_14',1),
    'Default':('default_15',8),
    'Science Fiction':('science-fiction_16', 1),
    'Sports and Games':('sports-and-games_17',1),
    'Add a comment': ('add-a-comment_18',4),
    'Fantasy':('fantasy_19',3),
    'New Adult': ('new-adult_20',1),
    'Young Adult':('young-adult_21',),
    'Science':('science_22',1),
    'Poetry':('poetry_23',1),
    'Paranormal':('paranormal_24',1),
    'Art':('art_25',1),
    'Psychology':('psychology_26',1),
    'Autobiography':('autobiography_27',1),
    'Parenting':('parenting_28',1),
    'Adult Fiction':('adult-fiction_29',1),
    'Humor':('humor_30',1),
    'Horror':('horror_31',1),
    'History':('history_32',1),
    'Food and Drink':('food-and-drink_33',2),
    'Christian Fiction':('christian-fiction_34',1),
    'Business':('business_35',1),
    'Biography':('biography_36',1),
    'Thriller':('thriller_37',1),
    'Contemporary':('contemporary_38',1),
    'Spirituality':('spirituality_39',1),
    'Academic':('academic_40',1),
    'Self Help':('self-help_41',1),
    'Historical':('historical_42',1),
    'Christian':('christian_43',1),
    'Suspense':('suspense_44',1),
    'Short Stories':('short-stories_45',1),
    'Novels':('novels_46',1),
    'Health':('health_47',1),
    'Politics':('politics_48',1),
    'Cultural':('cultural_49',1),
    'Erotica':('erotica_50',1),
    'Crime':('crime_51',1),
}


def in_stock(title: str, topic: str) -> str:
    page_title = dic[topic.title()]
    url_1 = f"https://books.toscrape.com/catalogue/category/books/{page_title[0]}/index.html"
    url_2 = "https://books.toscrape.com/catalogue/category/books/{page_title}/page-{num}.html"
    for i in range(1 ,page_title[1]+1):
        if i==1:
            myurl = url_1
        else:
            myurl = url_2.format(page_title=page_title[0], num=i)
        uClient = uReq(myurl)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        bookshelf = page_soup.findAll(
            "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for books in bookshelf:
            book_title = books.h3.a["title"]
            if book_title.lower()==title.lower():
                return True
    return False

print(in_stock("While You Were Mine", "Historical Fiction"))
