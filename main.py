from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from openpyxl import Workbook

import time

# 웹 드라이버 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
url = "https://www.youtube.com/results?search_query=%ED%85%8C%EB%AC%B4%EA%B9%A1"
driver.get(url)

last_height = driver.execute_script("return document.documentElement.scrollHeight")
max_videos = 2000  # 수집할 최대 영상 수
collected_videos = 0  # 현재까지 수집한 영상 수

# 페이지 스크롤하여 더 많은 영상 로드
last_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    new_height = driver.execute_script("return document.documentElement.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height

# 스크롤 후 잠시 대기
time.sleep(2)


# 더 많은 영상이 로드되지 않을 때까지 스크롤
while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(2)
    new_height = driver.execute_script("return document.documentElement.scrollHeight;")
    if new_height == last_height:
        break
    last_height = new_height

    # 엑셀 파일 및 시트 생성
    wb = Workbook()
    ws = wb.active
    ws.title = "YouTube_crawling"
    ws.append(['title', 'link', 'upload_date'])


    # 영상 정보 수집
    titles = driver.find_elements(By.CSS_SELECTOR, "#dismissible")
    for title in titles:
        main_title = title.find_element(By.CSS_SELECTOR, "#video-title").get_property("title")
        tube_url = title.find_element(By.CSS_SELECTOR, "#video-title").get_property("href")

        # metadata-line 요소에서 조회수와 게시일자를 따로 추출
        metadata_line = title.find_element(By.ID, "metadata-line")
        metadata_items = metadata_line.find_elements(By.CSS_SELECTOR, ".inline-metadata-item")

        # 조회수와 게시일자가 각각 첫 번째와 두 번째로 나타남
        upload_date = metadata_items[1].text.strip() if len(metadata_items) >= 2 else "N/A"

        print(main_title, " ", tube_url,  " ", upload_date)
        ws.append([main_title, tube_url, upload_date])


        collected_videos += 1

    # 엑셀 파일 저장 및 브라우저 종료
    wb.save('/Users/minjoo/PycharmProjects/temu/YouTube_temuGang_crolling.xlsx')
    wb.close()

    if collected_videos >= max_videos:
        break

# 브라우저 종료
driver.quit()
