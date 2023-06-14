# pandas
> 데이터 자료 구조 처리 및 분석을 위한 python library  
> high-performance, easy-to-use __data structures and data analysis tools__ for the Python programming language  
> [pandas document](https://pandas.pydata.org/docs/)  
> ...

-------

## 파일입출력
- `pd.read_excel('경로/파일명', sheet_name = '시트명')`
    > sheet_name = None 이면 전체 시트를 읽어옴
- `df.to_excel('경록/파일명', index=True)`  
- `pd.read_csv('경로/파일명')`  
- `df.to_csv('경로/파일명')`
- `pd.read_json('경로/파일명')`
- `df.to_json('경로/파일명')`

## 조회정렬필터
- `df.info()`: 컬럼별 정보 조회(데이터 개수, 타입 등)
- `df.value_counts()`: 데이터 개수 조회
- `df.ndim`: 데이터 프레임 차원 조회
- `df.shape`: (행, 열) 순서로 차원 조회
- `df.index`: 인덱스 조회
- `df.columns`: 컬럼 조회
- `df.values`: 값 조회
- `df.T`: 전치(Transpose) 행, 열 바꾸기
- `df.astype('int32')`: 타입 변경
- `df.sort_index(ascending=False)`: 인덱스 기준 정렬
- `df.sort_values(by=['컬럼명', '컬럼명'], ascending=[False, Ture])`: 컬럼 값 기준 정렬
- `df.loc[5, '컬럼명']`
- `df.loc[2:10:2, '컬럼명']`: 2부터 10까지 2씩 증가해서
- `df.loc[2:5, '컬럼명A':'컬럼명C']`: 2~5행, 컬럼 A~C까지 Slicing
- `df.loc[df['컬럼명'] >= 70]`: boolean index slicing
- `df.iloc[1,3]`: loc와 유사하고 index만 허용
- `df.isin(['값A', '값B'])`: 특정 값의 포함 여부 확인

## 통계
- `df.describe(include='object')`: 전반적인 주요 통계
- `df.count()`: 전체 개수
- `df.mean()`: 평균
- skipna=True: skipna=False로 설정하게 되면 NaN 값이 있는 컬럼은 NaN으로 출력
- `df.median()`: 데이터의 중앙값
- `df.sum()`: 
- `df.cumsum()`: 누적합
- `df.cumprod()`: 누적곱
- `df.var()`: 분산
- `df.std()`: 표준편차
- `df.min()`: 최소값
- `df.max()`: 최대값
- `df.agg(['min', 'max', 'count'])`: 여러 통계함수 동시 적용
- `df.quantile()`: 주어진 데이터를 동등한 크기로 분할하는 지점
- `df.unique()`: 고유값
- `df.nunique()`: 고유값 개수
- `df.mode()`: 최빈값
- `df.corr()['컬럼명']`: 컬럼간 상관관계 (-1 ~ 1사이 값을 가짐, -1에 가까울 수록 반비례)

## 복제및결측치
- `df.copy()`: DataFrame 전체 복사
- `df.isnull()`: 결측치 확인
- `df.isnull().sum()`: 결측치 개수 확인
- `df.isna()`: isnull 함수와 동일
- `df.notnull()`: 결측치가 아닌 
- `df.notnull().sum()`: 결측치가 아닌 컬럼 개수
- `df.fillna('값')`: 결측치 채우기
- `df.dropna(how='any/all')`: 결측치 제거 any 1개라도 NaN값 존재시 drop

## 전처리
- `df['컬럼명'] = 값`: 컬럼 추가 (**컬럼 끝에 추가됨**)
- `df.insert(index, 컬럼명, 값)`: 특정 위치에 컬럼 추가
- `df.drop(index)`: index 행 삭제
- `df.drop(np.arange(10))`: 범위 지정 삭제
- `df.drop(['컬럼명A', '컬럼명B'], axis=1, inplace=True)`: 열 삭제 **axis=1** 삭제하면 안됨
    > inplace=True 옵션은 삭제 결과를 원본 DataFrame에 반영
- Category type 변경: df.astype('catageory')
    > Category 타입 변경 시 사용하는 메모리도 줄어 듬
    > .cat으로 접근 `df.cat.cagegories`: 카테고리 출력
    > `df.cat.categories = ['값A', '값B']`: 카테고리 값 변경
- 문자열 처리
    - `df.str.split()`:
- Datatime
    - `pd.to_datetime(df/df['컬럼명'])`: datetime type으로 변경
    - datatime으로 변경 후 .dt로 속성 접근 가능
    - `df['컬럼명'].dt.year` -> 2004(년도) 출력
- binning (pd.cut())
    - `pd.cut(df, bins, labels=labels, right=False)`
    - `bins=[0, 6000, 10000, df['컬럼명'].max()]`
    - `labels=['레이블A', '레이블B', '레이블C']`
    - pd.cut()은 최소에서 최대구간을 지정한 Bin 개수 만큼 균등 분할
    - 데이터가 편향되어 있을 경우 적절하지 않음.
- binning (pd.qcut())
    - 데이터가 균등 분할 될 수 있도록 나눔
    - `pd.qcut(df, q=5)`

## 고급 - apply()
- **apply()**
    - 데이터 전처리를 위한 함수를 생성하고 적용하는 것
    ```
        def transform(x):
            if x < 30: 
                return young
            else:
                return old
        
        df['컬럼명'].apply(transform)
    ```
    - lambda: 간단한 로직의 경우 별도 함수 생성하지 않고 inline 처리
    ```
        df['컬럼명'].apply(lambda x: 'yound' if x <30 else 'old')
    ```
- **groupby()**
    - `df.groupby(['컬럼명A', '컬럼명B']).mean()`
    - `df.groupby(['컬럼명A', '컬럼명B']).mean().reset_index()`: 그룹핑 해제한 새로운 df

- **pivot_table()**
    - //
    - `df.pivot_table(index=['컬럼명' ..], columns=['컬럼명' ..], values='컬럼명', aggfunc=['mean' ..])`

- **pd.concat()**
    - 병합 (axis=0 행방향 병합, axis=1 열방향 병항)
    - `pd.concat([df1, df2], ignore_index=True, axis=1)`

- **pd.merge()**
    - 병합 데이터셋 간 공통키를 기준으로 병합
    - `pd.merge(left=, right=, how=, on/left_on/right_on=)`

## 주요 error
- type(df['컬럼명'])
    - DataFrame에서 컬럼 **1개**를 Slicing했을 경우 해당 type은 Series임.
    - Series Type이기 때문에 DataFrame 관련 함수가 적용되지 않음.

## Open API
- 실시간 환율 정보 조회 API
"https://api.exchangerate-api.com/v4/latest/USD"

- open data
    ```
    from opendata import dataset

    dataset.download('소상공인상권정보')
    dataset.download('서울시자전거')
    dataset.download('민간아파트분양')
    ```
## IPython
- Image 가져오기
    > Image('https://static1.squarespace.com/static/5006453fe4b09ef2252ba068/t/5090b249e4b047ba54dfd258/1351660113175/TItanic-Survival-Infographic.jpg')
- 

## warning 무시
- `warnings.filterwarnings('ignore')`: 

## e notation 표현 방식 변경
- `pd.options.display.float_format = '{:.2f}'.format`