# DSC Korea Hackathon 2021, 오이당근조 

# 개발환경
* Ubuntu 18.04 LTS

# 기술 스택
* python 3.7.4
* django 3.1.5
* django-cors-header 3.7.0
* djangorestframework 3.12.2
* sqlparse 0.4.1
* sqlite3

# API 서버
### 제공하는 key는 다음과 같음
1. "name": 국가명
2. "address": 상세주소
3. "lat": 위도
4. "lng": 경도
5. "happened_at": 발생일
6. "reported2oie_at": OIE에 보고된 날자
7. "memo": 기타
8. "created_at": 데이터 생성일
9. "updated_at": 데이터 최근 수정일 

# 팀원 및 역할 
* 고진형: 백엔드 개발, 데이터베이스, 서버
* 이상훈: 프론트엔드 개발, Google API
* 이주형: 프론트엔드 개발
* 조영우: 데이터 크롤링, 수집
