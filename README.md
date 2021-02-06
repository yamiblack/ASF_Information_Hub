# 아프리카 돼지열병(ASF) 정보 허브
 - 해커톤명 : <a href="https://dsc.community.dev/events/details/developer-student-clubs-sookmyung-womens-university-presents-2021-developer-student-clubs-korea-solution-challenge-hackathon/">DSC Korea Hackathon 2021</a>
 - 팀명 : 오이당근(<a href="https://github.com/jinhgoh">고진형</a>, <a href="https://github.com/yeongwooCho">이상훈</a>, <a href="https://github.com/yamiblack">이주형</a>, <a href="https://github.com/yeongwooCho">조영우</a>)
 - 기간 : 2021.01.31 ~ 2021.02.06
<br>

## 주제 및 기대효과
* United Nation sustainable development goal no.15 (Life on Land)
* 아프리카 돼지열병의 창궐지 등의 정보를 실시간으로 관찰 가능하고, 동시에 추가/수정이 가능한 서비스
* 질병 관련 정보들이 전세계에 산발적으로 존재하며, 시각적으로 한눈에 알기 어려운 문제점을 해결
* 다른 연구자들이 DB의 정보를 이용할 수 있도록 API를 제공
<br>

## 발표 영상
[![Video Label](https://user-images.githubusercontent.com/50551349/107113750-4b2b8280-68a4-11eb-839d-b6782a37916c.png)](https://user-images.githubusercontent.com/50551349/107113305-82e4fb00-68a1-11eb-824b-fafe10d82693.mp4)
<br>

## 서비스 소개
<img src="https://user-images.githubusercontent.com/50551349/107113326-aad45e80-68a1-11eb-99cb-ed7f0c8a0b89.png"> 

 - 사이트를 접속하면 초기화면은 위 그림과 같다.
 <br>
 
<img src="https://user-images.githubusercontent.com/50551349/107113336-b2940300-68a1-11eb-8f47-0dd961bae096.png"> 
<img src="https://user-images.githubusercontent.com/50551349/107113337-b32c9980-68a1-11eb-9dbc-3edd2da3baf7.png"> 

 - 지도를 확대하면 확대된 지도에서의 정보를 확인할 수 있다. 
 - 확대 시에는 바이러스 모형 내부에 숫자가 해당 지역에 맞게 동적으로 변하는 것을 확인할 수 있다.
 <br>
 
<img src="https://user-images.githubusercontent.com/50551349/107113335-b1fb6c80-68a1-11eb-87e5-6f9a1deb5777.png"> 

 - 바이러스 모형를 클릭하면 해당 지역에서의 상세한 정보를 확인할 수 있다.
<br>

<img src="https://user-images.githubusercontent.com/50551349/107113330-af007c00-68a1-11eb-8a34-ebba31a1d2be.png"> 

 - 하단의 '발생지 등록'을 클릭하면 위 그림과 같이 발생지를 등록할 수 있는 팝업에서 발생지를 직접 등록할 수 있다.
 <br>
 
<img src="https://user-images.githubusercontent.com/50551349/107113334-b162d600-68a1-11eb-853d-ae2e4d51053d.png"> 

 - 하단의 '관리자 모드'를 클릭하면 위 그림과 같이 관리자 비밀번호를 입력하는 팝업을 확인할 수 있으며, 로그인 시 관리자 메뉴를 확인할 수 있다.
 <br>
 
<img src="https://user-images.githubusercontent.com/50551349/107113332-b0ca3f80-68a1-11eb-8b5f-18d3e3904904.png"> 

 - 하단의 'ipserializer(API서버)'를 클릭하면 등록된 데이터를 확인할 수 있는 팝업을 확인할 수 있다.


<br>

## 개발환경
* Ubuntu 18.04 LTS
<br>

## 기술 스택
* python 3.7.4
* django 3.1.5
* djangorestframework 3.12.2
* sqlite3
* uWSGI 2.0.19.1
* NGINX 1.19
* AWS EC2
<br>

## API 서버
### 제공하는 key는 다음과 같음
1. "name" : 국가명
2. "address" : 상세주소
3. "lat" : 위도
4. "lng" : 경도
5. "happened_at" : 발생일
6. "reported2oie_at" : OIE에 보고된 날자
7. "memo" : 기타
8. "created_at" : 데이터 생성일
9. "updated_at" : 데이터 최근 수정일 


<img src="https://user-images.githubusercontent.com/50551349/107113608-5e8a1e00-68a3-11eb-822c-a71927d0d000.png">

 - 저장된 데이터의 예시는 위 그림과 같다.
<br>

## 팀원별 역할 
* <a href="https://github.com/jinhgoh">고진형</a> : 백엔드 개발, 데이터베이스, 서버
* <a href="https://github.com/yeongwooCho">이상훈</a> : 프론트엔드 개발, Google API
* <a href="https://github.com/yamiblack">이주형</a> : 프론트엔드 개발
* <a href="https://github.com/yeongwooCho">조영우</a> : 데이터 크롤링, 수집
