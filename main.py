from requests_html import HTMLSession
session = HTMLSession()

BASE_URL = 'https://fs.blog/mental-models/'

link_list = []
menu_link_list = []
completed_links = []
cleaned_link_list = []
additional_links = []

def link_scrape(r): 
    contents = r.html.find('.entry-content.entry-content-single')
    for content in contents: 
        links = r.html.find('a')
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

    return cleaned_link_list


def main():
    cleaned_link_list = [BASE_URL] 
    while len(cleaned_link_list) >= 1: 
        for link in cleaned_link_list:
            try:
                if link in completed_links:
                    pass 
                else:
                    r = session.get(link)
                    print("Valid link")
                    print(link)
                    cleaned_link_list += set(link_scrape(r)) 
                    print(len(cleaned_link_list))
                    completed_links.append(link) 
                    print(len(completed_links))
                    cleaned_link_list.remove(link)
            except:
                print("Invalid link")
                cleaned_link_list.remove(link)

main()
print(cleaned_link_list)
print(completed_links)
print(additional_links)