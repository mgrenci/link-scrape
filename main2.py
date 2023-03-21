from requests_html import HTMLSession
session = HTMLSession()


def category_link_scrape(r):
    article_links = []
    links = r.html.find('.entry-more-link')
    for link in links: 
        article_links.append(link.links)

    return article_links


BASE_URL = 'https://fs.blog/blog/'

r = session.get(BASE_URL)

link_list = []
menu_link_list = []
cleaned_link_list = []
completed_link_list = []
article_links = []

contents = r.html.find('.wp-block-categories-list')
for content in contents:
    links = r.html.find('li a') 
    menu_links = r.html.find('.menu-item-link')
  
for menu_link in menu_links:
    menu_link_list.append(menu_link.links)

for link in links: 
    link_list.append(link.links)
 
for menu_link in menu_link_list:
    if menu_link in link_list:
        link_list.remove(menu_link)
    else:
        pass 

for link in link_list:
    for l in link: 
        cleaned_link_list.append(l)

while len(cleaned_link_list) >= 1:
    for link in cleaned_link_list:
        try:
            if link in completed_link_list: 
                pass 
            else: 
                print(link)
                r = session.get(link)
                article_links.append(category_link_scrape(r))
                print("Valid Link")
                print(len(cleaned_link_list))
                completed_link_list.append(link)
                print(len(completed_link_list))
                cleaned_link_list.remove(link)
        except: 
            print("Invalid Link")
            cleaned_link_list.remove(link)
            

with open('article-links.txt', 'w') as f:
    for link_list in completed_link_list:
        for article_link in article_links:
            for link in article_link:
                for l in link:
                    f.write(l)
