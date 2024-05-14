import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = '/Library/Fonts/Arial Unicode.ttf'  # 사용하고자 하는 한글 폰트 경로
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# Excel 파일 읽기
df = pd.read_excel('clothing_waste.xlsx')

# 양(kg)에 대한 바 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(df['연월'], df['양(kg)'])
plt.title('테무깡 업로드 빈도')
plt.xlabel('연월')
plt.ylabel('양(kg)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

