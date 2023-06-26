---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.6
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# class


## class 정의

```python
class MyClass:
    def __init__(self, a: str = "initial"):
        self.__a = a
        
    def __call__(self):
        print('class/object invoke')
        
    @property
    def a(self):
        return self.__a
    
    @a.setter
    def a(self, new_value):
        self.__a = new_value
    
    def melon(self):
        print('I would like to eat melon')

    def apple(self):
        print('I would like to eat apple')

    def banna(self):
        print('I would like to eat banna')
 
```

### 변수명
* 클래스 선언 시 클래스 내부 변수 명에 double underscores을 prefix로 선언하면 obj.변수명으로 접근하는 것 방지
### Dunder Method
* Dunder: double underscore 약어
* 클래스 내부 동작을 정의하기 위한 내장 함수 (__init__: 클래스 생성/초기화, __call__: 클래스를 함수처럼 사용 가능하게 하기 위한 함수)
* 아래와 같이 클래스에 선언하지는 않았지만 사용가능한 dunder method 


### decorator(@property)
* 객체 내부 변수 및 함수에 쉽게 접근하게 하기 위한 것
* 객체 내부 변수 접근/조작을 하기 위한 별도 함수(def) 선언하지 않고 변수명으로 접근
    - obj.a = "second"

```python
print(dir(MyClass))
```

### getattr
* 객체의 속성값을 리턴하는 함수
* 복잡한 코드를 간결하게 만들기 위해 사용함 (변수명으로 관련함수 실행)

```python
obj = MyClass()

arr = ['apple', 'banna', 'melon']

for fruit in arr:
    getattr(obj, f'{fruit}')() #변수명으로 MyClass의 함수 실행
```

## 객체(Object) 생성(호출)
* MyClass()로 객체 생성
* 객체 생성 시 '__init__' 함수가 싫행되어 객체 초기화(initialize) 수행

```python
# 객체 생성 및 객체 변수(a) 출력
obj = MyClass()
print(obj.a)
```

```python
# 객체 변호(a)에 다른 값 assign 및 출력
obj.a = "second"
print(obj.a)
```

```python
# 객체 내부 변수를 아래와 같이 호출 시 에러 발생
print(obj.__a)
```

```python

```
