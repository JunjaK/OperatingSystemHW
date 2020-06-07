
# Assignment #3 Memory management (Documentation And Results)
## 사용한 자료구조
#### 프로그램의 구조에 관해서는 소스코드에서 주석으로 설명했습니다.
#### 사용한 주요 변수 설명 
- 설명에 없는 변수는 단순 계산을 위해 선언한 것입니다. 
- 간단한 무한루프 탈출을 위해 Flag로 사용한 Boolean 타입의 설명은 따로 하지 않았습니다.

| name | Description                                                      | Type           |
| --------- | ---------------------------------------------------------------- | -------------- |
| memorySize | 사용자에게 입력 받는 메모리의 크기입니다. | int | 
| requsetID | 사용자에게 입력받는 request의 id입니다. | int |
| requsetSize | 사용자에게 입력받는 request의 메모리 크기입니다. | int |
| remainMemory | 현재 남아있는 메모리를 표현하는 변수입니다. | int |
| isAvailable | 현재 메모리에 request를 할당할 수 있는지 여부를 판단합니다. 할당할 수 없으면 compaction을 진행하고 compaction을 진행하여도 메모리의 여유 공간이 없을 시 False 값을 가집니다.| boolean |
| isHoleAndSizeSame | hole의 사이즈와 request의 사이즈를 비교 후 같다면  | boolean         |
| requestResult | request 실행 후 결과를 반환합니다. 메모리에 여유가 있어 request가 성공한 경우 True, 그렇지 않은 경우 False 값을 가집니다.  | boolean |
| memory | 메모리에 담겨있는 request를 표현한 list입니다. | array[int] |
| holeTable | hole의 정보를 담아놓은 list입니다. (a, b)형식이며, a는 hole의 시작지점, b는 hole의 종료지점을 의미합니다. | array[tuple] |
| allocatedTable | 할당된 request 정보를 담아놓은 list입니다. (a, b, c)형식이며, a는 request id, b는 request size, c는 메모리에서 request의 시작지점을 의미합니다. | array[tuple] |


## 가정사항
#### 1. memory size는 1K 이상 1000K 이하를 입력받습니다.
#### 2. request size의 단위는 K입니다.
#### 3. 값을 입력시 사용자는 반드시 숫자를 입력해야합니다. (빈 값, 문자열 불가.)

## 사용방법 및 환경
- 개발환경 : python 3.8.2, VSCode 1.45.1, WSL2(window subsystem for linux2)
- 입력의 경우 구분은 공백으로 합니다.
- 코드 실행
```
python memoryManagement.py
```

## 입출력 예시
```
Memory Size를 입력해주세요. (1000K 이하, 단위 K) : 256

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 1 64

Best Fit: Allocated at address 0K
192K free, 1 block(s), avserage size = 192K

-- 할당된 Request --
Request 1 : 0K ~ 63K

-- Hole List --
Hole 1 : 64K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 2 64

Best Fit: Allocated at address 64K
128K free, 1 block(s), avserage size = 128K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K

-- Hole List --
Hole 1 : 128K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 3 32

Best Fit: Allocated at address 128K
96K free, 1 block(s), avserage size = 96K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K

-- Hole List --
Hole 1 : 160K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 4 16

Best Fit: Allocated at address 160K
80K free, 1 block(s), avserage size = 80K

-- 할당된 Request --
Request 1 : 0K ~ 63K
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 1 0

Best Fit: Freed at address 0K
144K free, 2 block(s), avserage size = 72K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 3 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 3 0

Best Fit: Freed at address 128K
176K free, 3 block(s), avserage size = 58K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 128K ~ 159K
Hole 3 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 5 32

Best Fit: Allocated at address 128K
144K free, 2 block(s), avserage size = 72K

-- 할당된 Request --
Request 2 : 64K ~ 127K
Request 5 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 63K
Hole 2 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 1

Request를 진행합니다.
Request ID와 Request Size를 입력해주세요(Size가 0일 경우 free request) : 2 0

Best Fit: Freed at address 64K
208K free, 2 block(s), avserage size = 104K

-- 할당된 Request --
Request 5 : 128K ~ 159K
Request 4 : 160K ~ 175K

-- Hole List --
Hole 1 : 0K ~ 127K
Hole 2 : 176K ~ 255K

실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request) : 0
프로그램을 종료합니다. 
```