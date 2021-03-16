# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler

# 검색 키워드
search_word = '신한은행'

# 텔레그램 봇 생성
token = '#####'
bot = telegram.Bot(token=token)
# 스케쥴러 생성
sched = BlockingScheduler()
# 기존에 보냈던 링크를 담아둘 리스트
old_links = []

# 링크 추출 함수
def extract_links(old_links=[]):
#    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
#    url = f'https://m.search.naver.com/search.naver?where=m_news&query=%EC%8B%A0%ED%95%9C%EC%9D%80%ED%96%89%20%EC%8B%A0%ED%95%9C%EA%B8%88%EC%9C%B5%20-%EB%86%8D%EA%B5%AC%20-%EC%95%BC%EA%B5%AC&sm=mtb_tnw&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Add%2Cp%3Aall'
# url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_amr&query=%EC%8B%A0%ED%95%9C%20-%EB%86%8D%EA%B5%AC%20-%EC%95%BC%EA%B5%AC%20-PBA&sort=1&nso=so:dd,p:all'
    url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_amr&query=신한%20-농구%20-야구%20-WKBL%20-KBO&sort=1&nso=so:dd,p:all'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    search_result = soup.select_one('#news_result_list')
    news_list = search_result.select('.bx > .news_wrap > a')

    links = []
    for news in news_list[:10]:
        link = news['href']
        links.append(link)

    new_links=[]
    for link in links:
        if link not in old_links:
            new_links.append(link)

    return new_links

# 텔레그램 메시지 전송 함수
def send_links():
    global old_links
    new_links = extract_links(old_links)
    if new_links:
        for link in new_links:
            bot.sendMessage(chat_id='-1001377656723', text=link)
#     else:
#         bot.sendMessage(chat_id='66077028', text='새로운 뉴스가 없습니다')
    old_links += new_links.copy()
    old_links = list(set(old_links))

# 최초 시작
send_links()
# 스케쥴러 세팅 및 작동
sched.add_job(send_links, 'interval', seconds=300)
sched.start()
