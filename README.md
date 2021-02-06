# 아프리카 돼지열병(ASF) 정보 허브
DSC Korea Hackathon 2021, 오이당근팀 


## 주제
* United Nation sustainable development goal no.15 (Life on lnad)
* 아프리카 돼지열병의 창궐지 등의 정보를 실시간으로 관찰 가능하고, 동시에 추가/수정이 가능한 서비스
* 질병 관련 정보들이 전세계에서 산발적으로 존재하며, 시각적으로 한눈에 알기 어려운 문제점을 해결함.
* 다른 연구자들이 DB의 정보를 이용할 수 있도록 API를 제공함. 

## 개발환경
* Ubuntu 18.04 LTS

## 기술 스택
* python 3.7.4
* django 3.1.5
* djangorestframework 3.12.2
* sqlite3

## API 서버
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

## 팀원 및 역할 
* 고진형: 백엔드 개발, 데이터베이스, 서버
* 이상훈: 프론트엔드 개발, Google API
* 이주형: 프론트엔드 개발
* 조영우: 데이터 크롤링, 수집
