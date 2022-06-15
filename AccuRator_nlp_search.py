from konlpy.tag import Okt, Mecab
import re

# 화면을 통한 사용자 질의내용 Sample1
question = "당사는 식료품 제조업을 영위하고 있습니다. 팬데믹으로 인해 소비의 형태가 많이 바뀌었고, 매출에 영향을 주고 있습니다.이에 코로나로 인한 소비형태 변화를 반영해 수요예측을 하고 싶습니다."

p_dictpath = "C:/mecab/mecab-ko-dic"

def get_tokenizer(tokenizer_name):
    if tokenizer_name == "okt":
        tokenizer = Okt()
    elif tokenizer_name == "mecab":
        tokenizer = Mecab(dicpath=p_dictpath)
    else:
        tokenizer = Mecab(dicpath=p_dictpath)
    return tokenizer

question = question.rstrip('\n')
question = question.strip()
question = question.replace(",","")
question = question.replace("."," ")
question = re.sub('[^가-힣a-z]', ' ', question)   
print(question)

tokenizer = get_tokenizer("mecab")
tokenizer.pos(question)
tokenizer.nouns(question)

tokens=[]
tokens = tokenizer.nouns(question)
print(tokens)
print(len(tokens))