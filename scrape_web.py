from bs4 import BeautifulSoup
import requests
import csv

# with open('simple_web.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())

# match = soup.title.text
# match = soup.div
# match = soup.find('div', class_='footer')
#
# for article in soup.find_all('div',class_='article'):
#     # print(article)
#     headline = article.h2.a.text
#     print(headline)
#
#     summary = article.p.text
#     print(summary)
#     print()


source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source,'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)

csv_writer.writerow(['headline', 'summary', 'video_link'])

# print(soup.prettify())

for article in soup.find_all('article'):

    # print(article.prettify())
    #
    headline = article.h2.a.text

    print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text

    print(summary)



    try:
        video_src = article.find('iframe', class_='youtube-player')['src']
        # print(video_src)

        vid_id = video_src.split('/')[4]
        # print(vid_id)

        vid_id = vid_id.split('?')[0]
        # print(vid_id)

        yt_link = f'https://youtube.com/watch?v={vid_id}'

    except Exception as e:
        yt_link = None

    print(yt_link)

    print('\n'*2)

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()


