# TwelveLabs SDK Search Test Suite

## Overview (개요)
This project provides an automated test suite for the TwelveLabs SDK `search.query()` functionality.

본 프로젝트는 TwelveLabs SDK의 `search.query()` 기능을 검증하기 위한 자동화 테스트 코드입니다.

The goal is to validate:
- Correct behavior under normal conditions  
- Stability under repeated usage  
- Robustness against invalid inputs and edge cases  
- Proper handling of API errors  
- Integrity of response schema  

다음 항목들을 검증하는 것을 목표로 합니다:
- 정상적인 요청에 대한 올바른 동작
- 반복 호출 시 안정성
- 잘못된 입력 및 엣지 케이스 처리
- API 에러 처리 검증
- 응답 데이터 구조(schema) 검증

---

## Setup (설정 방법)

### 1. Clone repository
bash
git clone <your-repo-url>
cd twelvelabs-test

### 2. Install dependencies
pip install -r requirements.txt


### 3. Configure environment variables
Create a .env file based on .env.example and provide your TwelveLabs API key and index ID.

.env.example 파일을 기반으로 .env 파일을 생성하고 API Key와 Index ID를 입력합니다.

TWELVELABS_API_KEY=your_api_key
TWELVELABS_INDEX_ID=your_index_id


## Test Structure (테스트 구성)
tests/
├── test_search_basic.py        # 기본 기능 검증
├── test_search_positive.py     # 정상 시나리오 테스트
├── test_search_negative.py     # 예외 및 잘못된 입력 테스트
├── test_search_edge_cases.py   # 엣지 케이스 테스트
├── test_search_schema.py       # 응답 데이터 구조 검증
utils/
└── search_helper.py            # 공통 search wrapper (safe_search)
core/
└── config.py                   # 환경변수 관리
└── client.py                   # SDK client 생성

core/config.py 역할
    .env 파일에서 API Key 및 Index ID 로딩
    테스트 코드에서 공통 설정값 제공
    하드코딩 제거 및 재사용성 향상

## Key Design (핵심 설계)

### 1. Environment Variable Management
    API Key 및 Index ID는 .env로 관리
    코드 내 하드코딩 제거

### 2. Safe Search Wrapper
External API의 불안정성을 고려하여 safe_search 유틸을 사용합니다.

safe_search(client, ...)
→ {
    "items": [...],
    "error": None | "SERVER_500"
}


### 3. Handling External API Errors (외부 API 에러 처리)
During testing, intermittent 500 Internal Server Error responses were observed from the TwelveLabs API.
테스트 수행 중 TwelveLabs API에서 간헐적으로 500 Internal Server Error가 발생하는 것을 확인했습니다.

Example:
{
  "code": "internal_server_error",
  "message": "An unexpected error has occurred on our server. Please try again later."
}

This indicates a server-side issue, not a client-side error.
이는 클라이언트 요청 문제가 아닌 서버 내부 오류를 의미합니다.



## 대응전략
500 에러 발생 시 테스트 실패로 처리하지 않음
"SERVER_500" 상태로 명시적으로 구분
테스트 로직에서 별도 처리

if error == "SERVER_500":
    print("Server error occurred (treated as known issue)")
    return



## 설계의도
외부 API의 비결정성(non-deterministic behavior) 대응
테스트의 안정성과 신뢰성 확보
실제 운영 환경과 유사한 테스트 구조 반영



## Run Tests (테스트 실행방법)
### 중요
You must run tests from the project root directory.
반드시 프로젝트 루트 디렉토리에서 실행해야 합니다.


---

### 1. Move to project root

cd tl-python

전체 테스트 실행
    pytest -s -v

특정 파일 샐행
    pytest -s -v tests/test_search_basic.py

특정 테스트 함수 실행
    pytest -s -v tests/test_search_basic.py::test_search_with_valid_query

## What is Covered (검증 범위)
Functional Tests
    정상 검색 결과 반환
    다양한 query 검증

Negative Tests
    잘못된 index_id
    빈 query
    잘못된 search option

Edge Cases
    결과 없음 (no results)
    반복 호출 안정성
    page_limit 검증

Schema Validation
    필드 존재 여부 검증
    데이터 타입 검증



## Notes (주의사항)
TwelveLabs API는 외부 서비스이므로 간헐적인 500 에러가 발생할 수 있음
해당 경우 테스트 실패가 아닌 Known Issue로 처리
테스트 결과는 네트워크 및 서버 상태에 영향을 받을 수 있음



## Conclusion (결론)

This test suite is designed to validate not only functional correctness,
but also robustness, stability, and real-world reliability of the TwelveLabs SDK.

본 테스트는 단순 기능 검증을 넘어
안정성, 예외 처리, 실제 환경 대응 능력까지 검증하도록 설계되었습니다.