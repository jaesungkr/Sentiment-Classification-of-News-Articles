# ImportError: DLL load failed while importing _jpype 오류 해결 https://github.com/konlpy/konlpy/issues/351

try:
    import jpype

    import jpype1
except:
    import jpype
import re
import konlpy
from konlpy.tag import Kkma
from konlpy.tag import Hannanum
from konlpy.tag import Okt


hannanum = Hannanum()
okt = Okt()

positive_news = ['코스피 상승 출발... 펄어비스 상승', '펄어비스 8% 상승', '한국 전력 주가 5%대 상승',
                 '8년만에 오른다.. 한국전력, 전기료 인상에 주가 상승', '주가 상승률 12.33%, 4.33%']
negative_news = ['코스피 하락 출발... 펄어비스 하락', '펄어비스 8% 하락', '한국 전력 주가 5%대 하락',
                 '8년만에 내린다.. 한국전력, 전기료 인상에 주가 하락', '주가 하락률 12.33%']

positive_label, negative_label = [0,0,0,0,0], [1,1,1,1,1]
stopwords = ['의', '가', '이', '은', '들', '는', '좀', '잘', '걍', '과', '도', '를', '으로', '자', '에', '와', '한', '하다']

x_train = []
for sentence in positive_news:
    '''
    텍스트에 소수점이 있을 경우, 분석기가 점(.)을 기준으로 나눠서 토큰화를 시키는걸 발견.
    이를 해결하기 위해 소수점 제거
    예) 12.33% 의 경우, '12'와 '33%'로 인식. 이 문제를 12퍼센트로 변환  
    '''
    tmp = re.findall(r"([0-9.]+.[0-9]+)", sentence)
    if tmp:
        for tm in tmp:
            sentence = sentence.replace(tm, tm.split('.')[0])
    # %가 누락되는 점을 감안하여, 한글로 변경
    if '%' in sentence:
        sentence = sentence.replace('%', '퍼센트')


    sen = []
    #sen = okt.morphs(sentence, stem=True) # 토큰화
    #sen = okt.nouns(sentence)
    sen = hannanum.nouns(sentence)

    #print(sen)
    sen = [word for word in sen if not sen in stopwords]
    x_train.append(sen)
print(x_train)


# pip install C:\Users\Jaesung_Park\Downloads\JPype1-1.1.2-cp39-cp39-win_amd64.whl
