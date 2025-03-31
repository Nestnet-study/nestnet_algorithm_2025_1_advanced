# 0. nestnet_algorithm_2025_1_advanced

2025-1 네스트넷 알고리즘 스터디 (골드)

<b>
스터디장 - 정한울
</b>

<br>

<h1>
1. 스터디 소개
</h1>
충북대학교 소프트웨어학과 학술동아리 네스트넷에서 진행하는 알고리즘 스터디로, 
<b>코딩 테스트 대비</b>와 <b>GitHub 기반 기록 관리</b>를 목표로 함.

<br>

문제 난이도: 백준 골드

<h2>1-1. 문제 선정 및</h2>

랜덤한 알고리즘, 골드 난이도 3문제를 ❗매주 일요일❗에 선정.<br>
선정된 문제는 [백준 그룹 문제집](https://www.acmicpc.net/group/workbook/18220)에서 확인.
<br>

<h2>1-2. 풀이 기간</h2>
해당 주차의 ❗월요일 ~ 토요일❗까지 풀이.<br>

### ❌ 주의사항

불참 시 벌금이 부과됨.<br>
단, 최초 불참 시에는 벌금이 면제됨.<br>

<br>
불참 벌금: ❗10,000원❗
<br>

<h2>1-3. 진행 방식</h2>
스터디는 온라인으로 진행됨.<br>
모든 스터디원은 매주 토요일까지 선정된 문제를 풀고, 각자의 레포지토리에 push한 후 PR을 보냄.<br>
<br>
<details>
  <summary><h3> 🔎 PR (Pull Request) 템플릿 </h3></summary>
<br>
<img src="https://github.com/user-attachments/assets/c61fa085-2e00-43a9-b234-977249040cc3", width=100%>

</details>
모든 PR은 위 템플릿의 형식에 맞춰 작성해야 함.<br>
<br>
PR을 작성한 이후, 다른 스터디원의 모든 PR을 확인하여 ❗1개 이상의 피드백❗ 코멘트로 작성<br>

<h1>2. 깃 관리 + Issue & PR(Pull Request) </h1>

<b>먼저 fork & Pull Request를 잘 모른다면 <a href="https://inpa.tistory.com/entry/GIT-%E2%9A%A1%EF%B8%8F-%EA%B9%83%ED%97%99-PRPull-Request-%EB%B3%B4%EB%82%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-folk-issue">블로그 참고</a></b>

<details>
  <summary>본문 보기</summary>

### 사진은 클릭하면 잘 보임.

  <ol>
    <li>본인이 코드를 작성할 프로젝트 or 폴더 생성</li>
    <br>
    <li>
      Nestnet-study Organization의 <a href="https://https://github.com/Nestnet-study/nestnet_algorithm_2025_1_advanced">nestnet_algorithm_2025_1_advanced
</a> 레포지토리 fork
      <img src="https://github.com/user-attachments/assets/02bf5dcb-bab6-4cf8-bd96-2fe554a7e8b3", width=100%>
    </li>
    <br>
    <li>
      fork 후에는 내 깃허브 레포지토리가 생김. <br>
      - organization의 레포지토리 : "Nestnet-study / nestnet_algorithm_2025_1_advanced" <br>
      - 내 레포지토리 : "본인 아이디 / nestnet_algorithm_2025_1_advanced" <br>
      내 레포지토리를 git clone.
      <img src="https://github.com/user-attachments/assets/2a04f1fd-d79a-49f4-b78d-d612e4726227", width=100%>
    </li>
    <br>
    <li>
      본인이 소스 코드를 작성할 프로젝트 or 폴더를 생성하고 적절한 위치에서 <b>git clone</b>을 해줌. <br>
      필자의 경우(자바), D:\jho7535\sample\untitled\src 하위에서 clone. <br>
      <img src="https://github.com/user-attachments/assets/d6a6a83f-532d-489e-8198-262eb5f422ae", width=100%>
    </li>
    <br>
    <li>
      클론한 레포지토리 하위에 본인의 이름으로 폴더 생성<br>
      본인 이름 폴더 하위에 주차별 폴더 생성. <br>
      반드시 <b>영문 이름(띄어쓰기 없이)/week_해당주차</b> <br> 
      ex) JeongHanUl/week_1
      <img src="https://github.com/user-attachments/assets/bb40688f-02fc-46ca-8c0a-ec24131ba1bf", width=100%>
      <br>
      폴더 구조는 다음과 같음
      <br>
      <img src="https://github.com/user-attachments/assets/4da3b35d-4324-4c6f-9bb5-df4e7b116d19", width=100%>
    </li>
    <br>
    <li>
      week_해당주차 하위에 소스 파일을 생성. <br>
      반드시 소스 파일 이름은 <b>boj_문제번호</b> <br>
      ex) week_1/boj_1374.java
      <br>
      <img src="https://github.com/user-attachments/assets/646c093b-81b5-49f8-8670-5b47919c292e", width=100%>
      해당 주차 문제를 모두 풀면 소스 파일을 커밋. <br>
      반드시 커밋 메시지는<b> git commit -m "(#이슈번호) [해당주차] 이름" </b><br>ex) git commit -m "(#3) [week1] JeongHanUl"<br><br>
      아래처럼 이슈 배너를 클릭하면 생성된 이슈 리스트를 확인할 수 있음.<br>
      <img src="https://github.com/user-attachments/assets/5add73b3-2233-431f-afad-de73a9eaced8", width=100%>
      <br>해당 주차에 해당되는 이슈 클릭.
      <img src="https://github.com/user-attachments/assets/1e8ce7df-2f19-4fbf-a695-c023c94ac572", width=100%>
      이슈 번호 확인 가능.      
    </li>
    <br>
    <li>
      커밋을 완료 후, 본인 레포지토리에 push<br>
      본인 레포지토리에서 push가 잘 된 것을 확인.
      <img src="https://github.com/user-attachments/assets/54a498eb-a537-4179-a469-cd4cfca191d1", width=100%><br>
      <br>새로운 PR 생성을 위해 Pull Request 배너를 클릭하여 New pull request 클릭.
      <img src="https://github.com/user-attachments/assets/ae47d456-cd22-4f52-b350-cc7adc1aa7bd", width=100%>
    </li>
    <br>
    <li>
      <b>head repository</b> : fork해서 가져온 내 레포지토리 <br>
      <b>base repository</b> : organization의 레포지토리 <br> 
      head의 main 브랜치에서 base의 main 브랜치로 PR을 보내는 것.
      <img src="https://github.com/user-attachments/assets/42aed2c4-f866-430b-8b39-e739e09da068", width=100%>
    </li>
    <br>
    <li>
      반드시 PR 제목은 <b>[n주차] 이름</b> <br>
      ex) [1주차] 정한울
      <img src="https://github.com/user-attachments/assets/6b51b37b-bf33-4032-874d-5c8f6952cc85", width=100%> <br>
      <br>본문은 세팅되어 있는 템플릿에 맞춰 작성. 작성 완료 후 Create pull request 클릭
      <img src="https://github.com/user-attachments/assets/177b9642-b6ee-4ac3-a6bd-1e2141daa051", width=100%>
    </li>
  </ol>
</details>

<br>

### ❌주의사항
PR을 제출하기 전에 본인 레포지토리에서 Sync fork를 통해 동기화 해줄 것.

![image](https://github.com/user-attachments/assets/77e3367c-4c28-48aa-b463-791f3a2d9639)
### 깃허브와 관련한 문제가 발생할 경우 스터디장에서 문의.

