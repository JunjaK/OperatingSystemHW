# Documentation And Results

## 사용한 자료구조
#### 프로그램의 구조에 관해서는 소스코드에서 주석으로 설명했습니다.
#### 사용한 주요 변수 설명 
- 설명에 없는 변수는 단순 계산을 위해 선언한 것입니다. 
- 간단한 무한루프 탈출을 위해 Flag로 사용한 Boolean 타입의 설명은 따로 하지 않았습니다.

| name | Description                                                      | Type           |
| --------- | ---------------------------------------------------------------- | -------------- |
| processNum | 사용자에게 입력 받는 Process의 수입니다. | int | 
| resourceNum | 사용자에게 입력 받는 Resource의 수입니다. | int         |
| userSelect | Resource 할당 및 프로그램 종료 플래그를 선택하는 정수입니다. | int |
| requestProcessNum | 사용자가 선택한 추가 Resource를 할당할 Process 번호입니다. | int |
| checkSafeState | 현재 시스템이 Safe State인지 아닌지 체크합니다. safe state일 경우 True | boolean         |
| needCheck | Process에 할당하는 resource가 Need보다 작은지 체크합니다. allocate resource가 need보다 작을 경우 True  | boolean |
| availableCheck |Process에 할당하는 resource가 Available보다 작은지 체크합니다. allocate resource가 Available보다 작을 경우 True | boolean |
| completedProcess | 작업이 완료된 Process의 번호를 저장하는 리스트입니다. | array[int] |
| resource | 사용자에게 입력 받은 가용한 Resource 리스트입니다. | array[int] |
| Allocation | Process에 현재 할당되어 있는 Resource를 나타냅니다. 초기 값은 사용자에게 입력 받습니다. | array[int][int] |
| Max | 각 Process에 최대 가용한 Resource를 나타냅니다. 사용자에게 입력 받습니다.  | array[int][int] |
| Need | Process에 완료되기 위해 필요한 Resource입니다. Max - Allocation으로 나타낼 수 있습니다.  | array[int][int] |
| Available | 현재 시스템에 가용한 Resource를 나타냅니다. 사용자에게 입력 받은 Resource - Allocation으로 나타낼 수 있습니다.  | array[int] |
| allocateR | 사용자에게 추가적으로 Request 받은 Resource입니다.  | array[int][int] |
| finish | Safety Algorithm에 사용되는 finish입니다.  | array[int] |
| Work | Safety Algorithm에 사용되는 Work입니다.  | array[int] |


## 가정사항
#### 1. Process는 최대 10개를 입력 받습니다.
#### 2. Resource는 최대 5개를 입력 받습니다.
#### 3. 사용자는 초기 Allocation 값, Resource Type, Max Resource를 계산이 불가능하게 입력하지 않습니다.
#### 4. 값을 입력시 사용자는 반드시 숫자를 입력해야합니다. (빈 값, 문자열 불가. int 변환이 안됩니다.)

## 사용방법 및 환경
- 개발환경 : python 3.8.2, VSCode 1.45.1, WSL2(window subsystem for linux2)
- 입력의 경우 구분은 공백으로 합니다.
- 코드 실행
```
python deadlock.py
```

## 입출력 예시
```
Memory Size를 입력해주세요. (1000K 이하, 단위 K) : 256

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 1

Request를 진행합니다.
Request ID와 Request Size(단위 K)를 입력해주세요 : 1 64

Best Fit: Allocated at address 0K
192K free, 1 block(s), avserage size = 192K

-- 할당된 Request --
Request 1 : 0K ~ 63K

-- Hole List --
Hole 1 : 64K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 1

Request를 진행합니다.
Request ID와 Request Size(단위 K)를 입력해주세요 : 1 64
이미 할당된 Request입니다. 다시 입력해주세요.
Request ID와 Request Size(단위 K)를 입력해주세요 : 2 64

Best Fit: Allocated at address 64K
128K free, 1 block(s), avserage size = 128K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K

-- Hole List --
Hole 1 : 128K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 1

Request를 진행합니다.
Request ID와 Request Size(단위 K)를 입력해주세요 : 3 32 

Best Fit: Allocated at address 128K
96K free, 1 block(s), avserage size = 96K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K

-- Hole List --
Hole 1 : 160K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 1

Request를 진행합니다.
Request ID와 Request Size(단위 K)를 입력해주세요 : 4 16

Best Fit: Allocated at address 160K
80K free, 1 block(s), avserage size = 80K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 2

Free Request를 진행합니다.
Free Request ID를 입력해주세요. : 1

Best Fit: Freed at address 0K
144K free, 2 block(s), avserage size = 72K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 2

Free Request를 진행합니다.
Free Request ID를 입력해주세요. : 3

Best Fit: Freed at address 128K
176K free, 3 block(s), avserage size = 58K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 128K ~ 159K
Hole 3 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 1

Request를 진행합니다.
Request ID와 Request Size(단위 K)를 입력해주세요 : 5 32

Best Fit: Allocated at address 128K
144K free, 2 block(s), avserage size = 72K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 4 : 160K ~ 175K
Request 5 : 128K ~ 159K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : 2

Free Request를 진행합니다.
Free Request ID를 입력해주세요. : 2

Best Fit: Freed at address 64K
208K free, 2 block(s), avserage size = 104K

-- 할당된 Request --
Request 4 : 160K ~ 175K
Request 5 : 128K ~ 159K

-- Hole List --
Hole 1 : 0K ~ 127K
Hole 2 : 176K ~ 255K
```