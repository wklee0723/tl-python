## ⚠️ Security Notice & Configuration
원활한 과제 검토를 위해 **예외적으로** 유효한 API Key와 Index ID가 포함된 `.env` 파일을 압축 파일 내에 첨부하였습니다. 

* **주의:** .env 파일은 과제 채용 담당자의 테스트 편의를 위해 제공하였으며, 실제 실무 환경에서는 보안을 위해 `.env` 파일을 공유하거나 버전 관리 시스템(Git)에 포함하지 않습니다.
* **사용 후 폐기:** 검토가 완료된 후에는 보안을 위해 해당 키를 즉시 폐기하거나 파일을 삭제해 주시기 바랍니다.


---

## TwelveLabs SDK Search Test Suite

### 1. Overview (개요)
- This project provides an automated test suite for the TwelveLabs SDK search.query() functionality.
- 본 프로젝트는 TwelveLabs SDK의 search.query() 기능을 검증하기 위한 자동화 테스트 코드입니다.

The goal is to validate:
- Correct behavior under normal conditions
- Stability under repeated usage
- Robustness against invalid inputs and edge cases
- Proper handling of API errors
- Integrity of response schema


### 2. Scope & Assumptions (범위 및 가정)
1. Testing Scope (테스트 범위)
- Target Method: `search.query()`
- Selected Parameters: `query_text`, `index_id`, `search_options` (검색의 핵심 기능을 담당하는 파라미터 위주로 구성)
- Reasoning: 방대한 파라미터 조합 중 실제 사용자가 가장 빈번하게 사용하며, 에러 발생 가능성이 높은 경계값 및 필수 파라미터 누락 케이스를 우선적으로 선정하였습니다.

2. Assumptions (가정 사항)
- SDK Version: `twelvelabs` 최신 버전(1.2.3)을 기준으로 작성되었습니다.
- Data Availability: 테스트 실행 시 지정된 `INDEX_ID`에는 최소 1개 이상의 비디오 데이터가 업로드되어 검색이 가능한 상태임을 전제로 합니다.


### 3. Setup (설정 방법)
1. Clone repository
- git clone <your-repo-url>
- cd tl-python

2. Install dependencies
- pip install -r requirements.txt

3. Configure environment variables
- .env.example 파일을 기반으로 .env 파일을 생성하고 API Key와 Index ID를 입력합니다.
- TWELVELABS_API_KEY=your_api_key
- TWELVELABS_INDEX_ID=your_index_id


### 4. Project Structure (프로젝트 구조)
```
├── .github/workflows
│   ├── test.yml            # GitHub Actions workflow 설정 파일
├── core/
│   ├── client.py           # SDK 클라이언트 생성 및 제공
│   └── config.py           # 환경변수 로딩 및 관리
├── tests/
│   ├── test_search_basic.py      # 기본 기능 검증
│   ├── test_search_edge_cases.py # 엣지 케이스 테스트
│   ├── test_search_negative.py   # 예외 및 잘못된 입력 테스트
│   ├── test_search_positive.py   # 정상 시나리오 테스트
│   └── test_search_schema.py     # 응답 데이터 구조 검증
├── utils/
│   └── search_helper.py    # 공통 search wrapper (safe_search)
├── .env.example            # 환경변수 설정 가이드
├── requirements.txt        # 의존성 라이브러리 목록
└── README.md               # 프로젝트 설명서
```

### 5. Key Design (핵심 설계)
1. Environment Variable Management
- API Key 및 Index ID는 .env로 관리하여 코드 내 하드코딩을 제거하고 보안성을 높였습니다.

2. Safe Search Wrapper
- External API의 비결정적 특성을 고려하여 safe_search 유틸을 사용합니다.
- 서버 에러(500) 발생 시 테스트를 즉시 중단하지 않고 상태값으로 관리하여 안정성을 확보합니다.

3. Handling External API Errors
- TwelveLabs API에서 간헐적으로 발생하는 internal_server_error에 대응하기 위해, 이를 클라이언트 측 결함이 아닌 "알려진 이슈(Known Issue)"로 분류하여 테스트 결과의 신뢰도를 유지합니다.

4. 시각화 및 이력 관리: Allure Report를 도입하여 테스트 통계 및 에러 로그를 시각화하고, GitHub Actions를 통해 테스트 이력을 관리합니다.


### 6. Run Tests (테스트 실행 방법)
중요: 반드시 프로젝트 루트 디렉토리(tl-python)에서 실행해야 합니다.

1. 전체 테스트 실행
- pytest -s -v

2. 특정 파일/함수 실행
- pytest -s -v tests/test_search_basic.py
- pytest -s -v tests/test_search_basic.py::test_search_with_valid_query


### 7. Test Reports (Allure)
본 프로젝트는 테스트 결과 시각화를 위해 Allure Report를 사용합니다.

1. GitHub Actions에서 확인 (자동)
본 프로젝트는 GitHub Actions를 통해 테스트 완료 후 리포트를 자동으로 배포합니다. 
저장소의 **Settings > Pages** 설정이 완료되면 아래와 같은 형식의 URL에서 리포트를 확인할 수 있습니다.

- Report 예시: https://wklee0723.github.io/tl-python/
- URL 구조: `https://<your-github-id>.github.io/<repository-name>/`

2. 로컬에서 확인
- 결과 수집
pytest --alluredir=allure-results

- 리포트 생성 및 실행
allure serve allure-results


### 8. What is Covered (검증 범위)
- Functional Tests: 정상 검색 결과 반환 및 다양한 Query 조합 검증
- Negative Tests: 잘못된 Index ID, 빈 Query, 유효하지 않은 옵션 처리
- Edge Cases: 결과 없음(No Results), 반복 호출 안정성, 페이징 제한 검증
- Schema Validation: 응답 필드 존재 여부 및 데이터 타입 일치 검증

### 9. CI/CD (GitHub Actions)
- Trigger: main 브랜치 Push 및 Pull Request 시 자동 실행
- Workflow: 의존성 설치 → Pytest 실행 → Allure 리포트 생성 → GitHub Pages 배포
- Security: GitHub Secrets를 통해 API Key 등 민감 정보 관리


### 10. Notes (주의사항)
- TwelveLabs API는 간헐적인 500 에러가 발생할 수 있습니다.
- 해당 경우 테스트 실패가 아닌 Known Issue로 처리하도록 설계되었습니다.
- 테스트 결과는 네트워크 상태 및 서버 응답 지연에 영향을 받을 수 있습니다.


### 11. Conclusion (결론)
본 테스트는 단순한 기능 검증을 넘어, 실제 운영 환경에서 발생할 수 있는 예외 상황과 외부 API의 불안정성까지 고려하여 설계되었습니다. 이를 통해 TwelveLabs SDK를 활용한 서비스의 안정성과 신뢰성을 보장합니다.





---

## Technical Documentation (기술 문서)

### 1. Chosen Approach (접근 방식)
- Pytest Framework: Python 생태계에서 가장 널리 쓰이고 확장성이 좋은 pytest를 선택했습니다. 특히 fixture를 활용해 SDK 클라이언트를 효율적으로 재사용하도록 설계했습니다.

- Modular Architecture: 코드의 유지보수성을 위해 환경 변수 관리(core/config), 클라이언트 생성(core/client), 유틸리티(utils/search_helper)를 분리하여 구현했습니다.

- Stability First: 외부 API의 불안정성(500 에러 등)을 고려하여, 에러 발생 시 테스트가 무조건 중단되는 대신 상태를 체크하여 보고하는 방식을 채택했습니다.

### 2. Testing Scope Decisions (테스트 범위 결정 근거)
- Search.query() 집중: 과제 가이드에 따라 search.query() 메서드에 집중했습니다.

- 파라미터 선정: 실무에서 가장 빈번하게 사용되는 query_text를 중심으로, 필수 값 누락(index_id), 유효하지 않은 옵션(search_options) 등 사용자가 실수하기 쉬운 시나리오를 우선순위로 두었습니다.

- 응답 데이터 검증: 단순히 에러가 발생하지 않는 것을 넘어, 반환된 데이터의 타입과 구조(Schema)가 명세와 일치하는지 검증하는 테스트를 포함했습니다.

### 3. SDK Version Used
- twelvelabs: 1.2.3 (제출 시점 최신 버전 기준)
- Python: 3.13.x

### 4. Assumptions (가정 사항)
- 사용자의 TwelveLabs 계정에 검색 대상이 되는 비디오가 포함된 인덱스가 최소 하나 이상 존재한다고 가정합니다.
- 환경 변수로 설정된 TWELVELABS_INDEX_ID는 유효한 인덱스 번호여야 합니다.
- 네트워크 환경은 TwelveLabs API 서버와 통신이 가능한 상태여야 합니다.

