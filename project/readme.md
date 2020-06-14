
# Term Project #3 Memory management (Documentation And Results)
## 사용한 자료구조
#### 프로그램의 구조에 관해서는 소스코드에서 주석으로 설명했습니다.
#### 사용한 주요 변수 설명 
- 설명에 없는 변수는 단순 계산을 위해 선언한 것입니다. (ex - temp가 붙어있는 변수들)
- 간단한 무한루프 탈출을 위해 Flag로 사용한 Boolean 타입의 설명은 따로 하지 않았습니다.

| name | Description                                                      | Type           |
| --------- | ---------------------------------------------------------------- | -------------- |
| hashQueueSize | 사용자에게 입력 받는 hash queue header의 크기입니다. | int | 
| block | 사용자에게 입력받는 block입니다. delayed_write 지정 및 getblk에 사용됩니다. | int |
| hashBufferIndex | block이 hash queue의 어느 index에 존재하는지 나타냅니다. block이 hash queue에 없다면 -1을 저장합니다. | int |
| freeBufferIndex | block이 free list의 어느 index에 존재하는지 나타냅니다. block이 free list에 없다면 -1을 저장합니다. | int |
| checkBlockInHash | hash queue에 block이 존재하는지 체크하는 변수입니다. hash queue에 block이 존재하면 True, 아닐 시 False를 저장합니다. | boolean |
| checkBlockFree | free list에 block이 존재하는지 체크하는 변수입니다. free list에 block이 존재하면 True, 아닐 시 False를 저장합니다. | boolean |
| checkCase2 | case2(빈 버퍼의 검출)가 실행되면 True, 실행하지 않으면 False를 저장합니다. | boolean |
| checkCase3 | case3(버퍼에 delayed write가 있는 경우)가 실행되면 True, 실행하지 않으면 False를 저장합니다. case3가 False일 시, Case2가 해당하는지 체크합니다, | boolean |
| hashQueue | hash queue를 저장하는 list입니다. 초기 값을 유저에게 입력 받습니다. delayed_write를 처리하기 위해 string list를 list의 원소로 갖습니다. | list[list][string] |
| freeList | free list를 저장하는 list입니다. 초기 값을 유저에게 입력 받습니다. | list[int] |
| sleepList | hash queue에서 block의 sleep을 몇 초 했는지 저장하는 list입니다. 사용중인 block이 3초를 sleep할 시 unlock 되어, 해당 block을 free list에 저장합니다. | list[list][int] |

## 가정사항
#### 1. Hash queue header size의 범위는 3이상 9이하입니다.
#### 2. 각 queue별로 할당되어 있는 block의 개수는 3이상 9이하입니다.
#### 3. free list의 block의 개수는 3이상 9이하입니다.
#### 4. free list가 비어있을 때(경우4), 요청하는 block에 해당하는 hash queue header에서 가장 처음의 block을 unlock 시도를 합니다(sleep). 3번 시도 시, unlock 됩니다.
#### 5. 사용자는 입력을 예시에 맞게 입력합니다. (입력에 관하여 따로 예외처리를 하지 않았습니다.)

## 사용방법 및 환경
- 개발환경 : python 3.8.2, VSCode 1.45.1, WSL2(window subsystem for linux2)
- 입력의 경우 구분은 공백으로 합니다.
- 코드 실행
```
python getblk.py
```

## 입출력 예시
```
Hash Queue Header Size N을 입력해주세요(3<=N<=9) : 4
1번째, 각 Queue별로 할당되어있는 block의 개수 n과 n개의 블록 번호를 입력해주세요((3<=n<=9) : 3 28 4 64
2번째, 각 Queue별로 할당되어있는 block의 개수 n과 n개의 블록 번호를 입력해주세요((3<=n<=9) : 3 17 5 97
3번째, 각 Queue별로 할당되어있는 block의 개수 n과 n개의 블록 번호를 입력해주세요((3<=n<=9) : 3 98 50 10
4번째, 각 Queue별로 할당되어있는 block의 개수 n과 n개의 블록 번호를 입력해주세요((3<=n<=9) : 3 3 35 99
Free list에 있는 block의 개수와 m과 m개의 블록 번호를 입력 해주세요((3<=m<=9) : 6 3 5 4 28 97 10

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10']
blk no 3 mod 4  ['3', '35', '99']
Free List  [3, 5, 4, 28, 97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 4

--- return block 4 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10']
blk no 3 mod 4  ['3', '35', '99']
Free List  [3, 5, 28, 97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 18

--- return block 18 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  [5, 28, 97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 1 5

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5_delayed_write', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  [5, 28, 97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 1 28

### HashQueue ###
blk no 0 mod 4  ['28_delayed_write', '4', '64']
blk no 1 mod 4  ['17', '5_delayed_write', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  [5, 28, 97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 28

--- return delayed write block 5 ---
--- return delayed write block 28 ---
## block 28 not in freelist, Sleep 1 second ##
## block 28 not in freelist, Sleep 1 second ##
## block 28 not in freelist, Sleep 1 second ##
--- return block 28 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  [97, 10]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 10

--- return block 10 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  [97]

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 97

--- return block 97 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['35', '99']
Free List  []

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 2 43

## Sleep 1 second for free block 35 ##
## Sleep 1 second for free block 35 ##
## Sleep 1 second for free block 35 ##
--- return block 43 ---

### HashQueue ###
blk no 0 mod 4  ['28', '4', '64']
blk no 1 mod 4  ['17', '5', '97']
blk no 2 mod 4  ['98', '50', '10', '18']
blk no 3 mod 4  ['99', '43']
Free List  []

### Select Operation ###
1. Change block status to delayed write
2. getblk
3. exit

Enter Operation : 3
Exit Program
```