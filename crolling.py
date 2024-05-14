import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = '/Library/Fonts/Arial Unicode.ttf'  # 사용하고자 하는 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 파일 읽기
df = pd.read_excel('/Users/minjoo/PycharmProjects/temu/YouTube_crolling.xlsx')

# upload_date 열의 값들에 대한 개수 확인
upload_date_counts = df['upload_date'].value_counts()

# 히스토그램 그리기
plt.figure(figsize=(10, 6))
upload_date_counts.plot(kind='bar')
plt.title('테무 업로드 빈도')
plt.xlabel('Upload Date')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()