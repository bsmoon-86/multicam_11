import pandas as pd
import numpy as np
from konlpy.tag import Komoran
from gensim.models import FastText
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def tokenize(text):
    """Komoran을 이용한 형태소 분석 및 토큰화"""
    try:
        komoran = Komoran()
        # 명사, 동사, 형용사, 외국어, 일반 부사만 추출
        allow_pos = ['NNP', 'NNG', 'VV', 'VA', 'SL', 'MAG']
        tokens = []
        for word, pos in komoran.pos(str(text)):
            if pos in allow_pos:
                tokens.append(word)
        return tokens
    except Exception as e:
        # Komoran 사용 불가 시 단순 공백 분리
        return str(text).split()

def sent_embed_mean(tokens, model):
    """FastText 단위 벡터의 평균을 이용해 문장 임베딩"""
    vector = []
    for word in tokens:
        # FastText는 n-gram을 통해 OOV(사전 외 단어)를 추론할 수 있습니다.
        if word in model.wv:
            vector.append(model.wv[word])
            
    if vector:
        return np.mean(vector, axis=0)
    else:
        return np.zeros(model.vector_size)

def main():
    # 1. 데이터 로드 (NSMC 등 일반적인 ratings 데이터는 주로 탭(\t)으로 구분됩니다)
    file_path = 'data/ratings_test.txt'
    
    try:
        print("데이터 로드 중...")
        df = pd.read_csv(file_path, sep='\t')
        df = df.dropna(subset=['document']) # 내용이 없는 결측치 제거
    except Exception as e:
        print(f"데이터 로드 실패: {e}")
        return

    # 2. 텍스트 토큰화
    print("텍스트 토큰화 진행 중...")
    df['tokens'] = df['document'].apply(tokenize)
    # 토큰이 비어있는(예: 특수문자만 있는 경우 등) 행 제거
    df = df[df['tokens'].map(len) > 0]

    # 3. FastText 모델 학습
    print("FastText 모델 학습 중...")
    fasttext_model = FastText(
        sentences=df['tokens'].tolist(),
        vector_size=100,
        window=5,
        min_count=1,
        epochs=10, 
        sg=1,      # Skip-gram 방식 사용
        workers=4,
        seed=42
    )

    # 4. 문장 벡터(임베딩) 생성
    print("문장 임베딩 벡터 생성 중...")
    df['vector'] = df['tokens'].apply(lambda x: sent_embed_mean(x, fasttext_model))

    # 5. 독립변수(X)와 종속변수(y) 생성 및 데이터 분할
    X = np.stack(df['vector'].values)
    y = df['label'].values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6. SVC(Support Vector Classifier) 모델 학습
    print("SVC 분류 모델 학습 중...")
    svc_model = SVC(kernel='rbf', random_state=42)
    svc_model.fit(X_train, y_train)

    # 7. 예측 및 성능 평가
    print("\n--- SVC 모델 평가 결과 ---")
    y_pred = svc_model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

if __name__ == '__main__':
    main()