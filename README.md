# skong1

### Introduction
- pynecone 체험 
- 오랜 친구 생일선물로 웹페이지를 편지대신 전달할 예정
- start : 2023.01.29 ~
- finish : ~ 2023.02.05


### Design
🎁 [framer](https://charts-dam-188584.framer.app/)

<br>

### pynecone

- [공식 홈페이지](https://pynecone.io/)
- [공식 document](https://pynecone.io/docs/getting-started/introduction)

<br>

### Result

- 각 페이지의 디자인 

HBD | Gift
-----|-----
![hbd](https://user-images.githubusercontent.com/80612249/216810829-b335b258-072a-4e19-916d-9fb48aa30e25.png)|![gift](https://user-images.githubusercontent.com/80612249/216810949-5fd55bac-327d-4213-b170-0ee89b587263.png)

Letter | Timeline 
-----|-----
![letter](https://user-images.githubusercontent.com/80612249/216810984-91bb33d6-2476-4f7e-9ab9-ea9332040a1b.png)|![timeline_open](https://user-images.githubusercontent.com/80612249/216810981-98437a35-69ce-4b16-9164-1e872134777a.png)

- Accordion을 이용한 설명 숨기기
<img src="https://user-images.githubusercontent.com/80612249/216811087-b9f2a3e9-4cdd-43a6-abcb-bc4dd7985390.png" width="700"/>

- Button을 누르면 편지의 상세한 내용이 열리고 닫힘
<img src="https://user-images.githubusercontent.com/80612249/216811095-c1bafc2d-1e78-47c9-ac86-4dee8dff2bc7.png" width="700"/>


- 처음 본 시간부터 현재까지의 날짜 변화를 Slider로 시각화. 

Min | Max
----|----
![timeline_min](https://user-images.githubusercontent.com/80612249/216811093-bc8d4f40-b617-40e6-89b3-933a4b042bc2.png)|![timeline_max](https://user-images.githubusercontent.com/80612249/216811092-1d7dfa9f-1535-405e-9e9f-bfe2e16c3717.png)

- 소소한 tooltip 기능...  

<img src="https://user-images.githubusercontent.com/80612249/216811097-37c9a59d-877b-4abf-9eb6-39d9ac0f3f8f.png" width="400"/>


<br>

문제점은 이렇게 반응형 웹으로 잘 구성해 뒀는데, pynecone에서 제공하는 호스팅 서비스 (pc deploy)가 아직 준비 중이었다!
그래서 pc export로 html로는 내보낼 수가 있는데 반응형 컴포넌트로는 변환을 하지 못해서(백엔드 파트는 그대로 python 코드로 만든다)
호스팅을 따로 할 때 그냥 html로만... 정적인 웹 사이트로 변환해서 일단 만들어두었다.

<br>

열심히 구상했는데 정적인 페이지를 선물로 주게 되어 아쉽다.
하지만 리액트 JS 거의 모르는데 파이썬으로 이만큼이라고 편하게 만들어줄 수 있게 지원해 주는 게 어디인가, 싶기도 하다.
유익한 경험이었지만 확실히 나는 개발이랑 안 맞는 거 같다는 걸 다시 한번 더 알 수 있었다. 
