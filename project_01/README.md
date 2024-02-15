# 사주고냥
![채팅룸 페이지](./assets/media/meta_image.png)

## 1. 목표와 기능
### 1.1. 목표
- 오름캠프 상반기 수업 요소를 다양하게 활용해 학습내용을 체화
    - AI
        - chatGPT api : 답변에 고양이라는 캐릭터성을 부여하고 감정표현을 추가
    - JavaScript
        - 프레임워크를 사용하지 않고 바닐라 자바스크립트로 동적 웹사이트 구현

### 1.2. 기능
- 채팅 UI를 통해 사용자의 생년월일을 입력받고 신년운세를 대화형으로 제공

## 2. 개발환경 및 배포 URL
### 2.1. 개발 환경
- 개발 환경 : HTML, CSS, JavaScript
- 서비스 배포 환경 : GitHub Page

### 2.2. 배포 URL
- https://escape1001.github.io/ormcamp/project_01

### 2.3. URL 구조
| App | URL | Views Function | HTML File Name | Note |
| --- | --- | --- | --- | --- |
| project01 | '/project01’ | welcome | project01/index.html | 홈 화면 |
| project01 | '/project01/chatroom’ | chatroom | project01/chatroom/index.html | 채팅 화면 |

## 3. 기능 명세

```mermaid
sequenceDiagram
    actor User
    participant Website
    participant API

    User->>Website: 사용자가 메시지 입력
    Website->>Website: 로딩 표시
    Website-->>API: API로 메시지 전송
    API->>API: 메시지 처리
    alt 처리 성공
        API-->>Website: 처리 결과 반환
        Website->>User: 로딩 표시 해제 및 메시지 출력
    else 처리 실패
        API-->>Website: 에러 반환
        Website->>User: 에러 메시지 표시하고 재시도 요청
    end
    opt 입력한 값에서 날짜를 확인할 수 없는 경우
        Website->>User: 재시도 요청
    end
    opt api 받아온 값을 파싱할 수 없을 때
        Website->>User: 재시도 요청
    end
```

## 4. 프로젝트 구조와 개발 일정
### 4.1. 프로젝트 구조
```bash
📂project_01
├─ 📂assets
│  ├─ 📂media
│  ├─ 📂script
│  │  └─📜chatroom.js
│  └─ 📂style
│     ├─📜chatroom.css
│     ├─📜global.css
│     └─📜welcome.css
├─ 📂chatroom
│  └─ 📜index.html
└─ 📜index.html
```

### 4.2. 개발 일정(WBS)
```mermaid
gantt
    title 프로젝트 일정

    section 일정
    프로젝트 개설 후 러프작업       :a1, 2024-02-08, 5d
    문서작업 - 초안                 :a2, 2024-02-13, 1d
    코드개선                        :a4, 2024-02-14, 2d
    프롬포트 개선                   :a3, 2024-02-14, 1d
    문서작업 - 마무리               :a5, 2024-02-15, 1d
    프로젝트 발표                   :a6, 2024-02-16, 1d
```

## 5. 와이어프레임 / UI

### 5.1. 와이어프레임
[Figma - 사주고냥 와이어 프레임](https://www.figma.com/file/ofWNGMj0v0mjAA2t96KEtZ/%EC%82%AC%EC%A3%BC%EA%B3%A0%EB%83%A5?type=design&node-id=0%3A1&mode=design&t=IJlP2xiSfTRX3v1R-1)

![와이어프레임](./assets/media/readme_wireframe.png)

### 5.2. 화면설계
- 메인 페이지

![메인 페이지](./assets/media/readme_welcome.png)

- 채팅룸 페이지

![채팅룸 페이지](./assets/media/readme_chatroom.png)

	

## 6.Architecture

```mermaid
graph TD;
A[Frontend] -->|Request| B[ChatGPT API]
B -->|Response| A
A -->|Deploys to| C[GitHub Pages]
```

## 7. 에러와 에러 해결
- [TO DO : 작성 필요]

## 8. 개발하며 느낀점
- [TO DO : 작성 필요]