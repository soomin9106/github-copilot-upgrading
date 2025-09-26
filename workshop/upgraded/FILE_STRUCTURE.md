# upgraded 폴더 파일 구조 설명

이 파일은 `/workspaces/github-copilot-upgrading/workshop/upgraded` 폴더 내의 파일 및 디렉터리 구조를 설명합니다.

- `distribute_setup.py`, `distribute-0.6.10.tar.gz`, `MANIFEST.in`, `README.rst`, `setup.py`: 패키지 배포 및 설치 관련 파일
- `docs/`: Sphinx 기반 문서화 디렉터리
  - `Makefile`: 문서 빌드용 Makefile
  - `build/`: 빌드된 문서 결과물
  - `source/`: 문서 소스(rst, conf.py 등)
- `guachi/`: 주요 파이썬 패키지 소스 코드
  - `__init__.py`, `config.py`, `database.py`: guachi 패키지의 핵심 모듈
  - `tests/`: 테스트 코드 디렉터리
    - `test_configmapper.py`, `test_configurations.py`, `test_database.py`, `test_integration.py`: 각종 테스트 스크립트
- `guachi.egg-info/`: 패키지 메타데이터 정보
  - `dependency_links.txt`, `PKG-INFO`, `SOURCES.txt`, `top_level.txt`

이 구조는 레거시(legacy) 폴더와 동일하게 복사되어, 업그레이드 작업 및 실험에 활용할 수 있습니다.
