# from requests_html import HTML, HTMLSession

# with open('simple.html') as html_file:
#     source = html_file.read()
#     html = HTML(html = source)
    
# # match = html.find('title', first = True)
# # match = html.find('#footer', first = True)
# # print(match.text)
# # article = html.find('div.article', first = True)
# # headline = article.find('h2', first = True).text
# # summary = article.find('p', first = True).text
# # print(headline)
# # print(summary)

# # articles = html.find('div.article')
# # for article in articles:
# #     headline = article.find('h2', first = True).text
# #     summary = article.find('p', first = True).text
# #     print(headline)
# #     print(summary)
# #     print()



# import csv
# from requests_html import HTML, HTMLSession
# csv_file=open('cms_scrape.csv', 'w')
# csv_writer=csv.writer(csv_file)
# csv_writer.writerow(['headline','summary','video'])
# session=HTMLSession()
# r=session.get('https://coreyms.com/')
# articles=r.html.find('article')
# for article in articles:
#     headline=article.find('.entry-title-link', first=True).text
#     print(headline)
#     summary=article.find('.entry-content p', first=True).text
#     print(summary)
#     try:
#       vid_src=article.find('iframe', first=True).attrs['src']
#       vid_id=vid_src.split('/')[4]
#       vid_id=vid_id.split('?')[0]
#       yt_link=f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link=None
#     print(yt_link)
#     print()
#     csv_writer.writerow([headline,summary,yt_link])
# csv_file.close()


    
    
    
    
# -------------------------------------------------------------------------




from bs4 import BeautifulSoup
import requests
# with open('simple_1.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')
# for article in soup.find_all('div', class_ = 'article'):
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print()



source=requests.get('http://coreyms.com').text
soup=BeautifulSoup(source, 'lxml')
# article = soup.find('article')
# print(article.prettify())
# headline = article.h2.a.text
# print(headline)
# summary = article.find('div', class_ = 'entry-content').p.text
# print(summary)
# vid_src = article.find('iframe', class_ = 'youtube-player')['src']
# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# print(vid_id)
# yt_link=f'https://youtube.com/watch?v={vid_id}'
# print(yt_link)
# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     print(headline)
#     summray = article.find('div', class_ = 'entry-content').p.text
#     print(summray)
#     try:
#         vid_src = article.find('div', class_ = 'youtube-player')['src']
#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None
#     print(yt_link)
#     print()


import csv
source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])
for article in soup.find_all('article'):
    headline = article.h2.a.text
    print(headline)
    summary = article.find('div', class_ = 'entry-content').p.text
    print(summary)
    
    try:
        vid_src=article.find('iframe', class_='youtube-player')['src']
        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]
        yt_link=f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link=None
    print(yt_link)
    print()
    csv_writer.writerow([headline, summary, yt_link])
csv_file.close()

        

