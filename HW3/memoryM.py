# 할당된 메모리 주소 순으로 순서 변경하는데 필요한 함수
def allocatedTableSorting(elem):
  return elem[1]
# holeTable 만들기
def makeHoleTable(mem):
  holeStart = -1
  holeEnd = -1
  holeTable = []
  for i in range(0, len(mem)):
    if(holeStart == -1 and mem[i] == 0):
      holeStart = i
    if(holeStart != -1 and mem[i] != 0):
      holeEnd = i-1
      holeTable.append([holeStart,holeEnd])
      holeStart = -1
      holeEnd = -1
  if(holeEnd == -1):
      holeTable.append([holeStart, len(mem)-1])
  return holeTable

# 공간이 부족하다면 compaction 진행
def request(mem, id, size, holeTable, allocatedTable, memSize):
  isAvailable = False # 메모리에 request를 할당할 여유가 있는지 확인하는 Flag
  isHoleAndSizeSame = False 

  # request size와 hole size가 같은 것이 있는지 확인, 같다면 할당
  for i in range(0, len(holeTable)):
    holeSize = holeTable[i][1] - holeTable[i][0] + 1
    if(size == holeSize):
      isHoleAndSizeSame = True
      isAvailable = True
      print('\nBest Fit: Allocated at address %dK'%(holeTable[i][0]))
      for j in range(0, size):
        mem[j+holeTable[i][0]] = id
      allocatedTable.append([id, size, holeTable[i][0]])
      break

  # request size < hole size인지 확인, 해당한다면 할당
  if(isHoleAndSizeSame == False):
    for i in range(0, len(holeTable)):
      holeSize = holeTable[i][1] - holeTable[i][0] + 1
      if(size < holeSize):
        print('\nBest Fit: Allocated at address %dK'%(holeTable[i][0]))
        isAvailable = True
        for j in range(0, size):
          mem[j+holeTable[i][0]] = id
        allocatedTable.append([id, size, holeTable[i][0]])
        break
        
  # request size > hole size일 때, Compaction 진행 후 할당.
  if(isAvailable == False):
    # Compaction 
    mem = [0 for i in range (0, memSize)]
    index = 0
    for i in range (0, len(allocatedTable)):
      for j in range(0, allocatedTable[i][1]):
        mem[index] = allocatedTable[i][0]
        index+=1
    holeTable = makeHoleTable(mem)
    
    # memory 할당
    holeSize = holeTable[0][1] - holeTable[0][0]
    if(size < holeSize):
      print('\nBest Fit: Allocated at address %dK'%(holeTable[i][0]))
      isAvailable = True
      for j in range(0, size):
        mem[j+holeTable[0][0]] = id
      allocatedTable.append([id, size, holeTable[i][0]])

  holeTable = makeHoleTable(mem)
  
  # 남은 메모리 계산
  remianMemory = 0
  for i in range(0, len(holeTable)):
    remianMemory += holeTable[i][1] - holeTable[i][0] + 1

  return isAvailable, mem, holeTable, allocatedTable, remianMemory

# free request    
def freeReuest(mem, id, holeTable, allocatedTable, memSize):
  for i in range(0, len(allocatedTable)):
    if(allocatedTable[i][0] == id):
      for j in range(0, memSize):
        if(mem[j] == id):
          mem[j] = 0
      print('\nBest Fit: Freed at address %dK'%(allocatedTable[i][2]))
      del allocatedTable[i]
      break

  holeTable = makeHoleTable(mem)
  
  # 남은 메모리 계산
  remianMemory = 0
  for i in range(0, len(holeTable)):
    remianMemory += holeTable[i][1] - holeTable[i][0] + 1
  # allocatedTable.sort(key=)
  return mem, holeTable, allocatedTable, remianMemory

# 결과 출력
def printResult(freeMem, holeLen):
  print('%dK free, %d block(s), avserage size = %dK\n'%(freeMem, holeLen, freeMem/holeLen))

def main():
  '''
  초기 세팅
  '''
  # 프로세스 및 리소스 개수 입력
  memorySize = int(input('Memory Size를 입력해주세요. (1000K 이하, 단위 K) : '))
  memory = [0 for i in range(0, memorySize)]
  remainMemory = memorySize
  holeTable = [[0,memorySize-1]]
  allocatedTable = []
  while True:
    operation = int(input('\n실행할 연산을 입력해주세요. (0번 - 프로그램 종료, 1번 - Request, 2번 - Free Request) : '))
    if(operation == 0):
      print('프로그램을 종료합니다. \n')
      break
    elif(operation == 1):
      print('\nRequest를 진행합니다.')
      while True:
        checkDup = False
        requsetID, requsetSize  = map(int, (input('Request ID와 Request Size(단위 K)를 입력해주세요 : ').split()))
        for i in range(0, len(allocatedTable)):
          if(requsetID == allocatedTable[i][0]):
            checkDup = True
        if(checkDup):
          print('이미 할당된 Request입니다. 다시 입력해주세요.\n')
        else:
          break
      
      # request 실행
      requestResult, memory, holeTable, allocatedTable, remainMemory = request(memory, requsetID, requsetSize, holeTable, allocatedTable, memorySize)

      if(requestResult == False):
        print('메모리의 남은 공간보다 Size가 크므로, request 할당에 실패하였습니다.\n')
      else:
        holeLen = len(holeTable)
        print('%dK free, %d block(s), avserage size = %dK\n'%(remainMemory, holeLen, remainMemory/holeLen))
        print('-- 할당된 Request --')
        for i in range(0,len(allocatedTable)):
          print('Request %d : %dK ~ %dK'%(allocatedTable[i][0], allocatedTable[i][2], allocatedTable[i][2] + allocatedTable[i][1]-1))
        print('\n-- Hole List --')
        for i in range(0,len(holeTable)):
          print('Hole %d : %dK ~ %dK'%(i+1, holeTable[i][0], holeTable[i][1]))
    elif(operation == 2):
      print('\nFree Request를 진행합니다.')
      while True:
        checkDup = False
        freeRequsetID  = int(input('Free Request ID를 입력해주세요. : '))
        for i in range(0, len(allocatedTable)):
          if(freeRequsetID == allocatedTable[i][0]):
            checkDup = True
        if(checkDup):
          break
        else:
          print('해당하는 ID가 존재하지 않습니다. 다시 입력해주세요.\n')


      # free request 실행
      memory, holeTable, allocatedTable, remainMemory = freeReuest(memory, freeRequsetID, holeTable, allocatedTable, memorySize)

      holeLen = len(holeTable)
      print('%dK free, %d block(s), avserage size = %dK\n'%(remainMemory, holeLen, remainMemory/holeLen))
      print('-- 할당된 Request --')
      for i in range(0,len(allocatedTable)):
        print('Request %d : %dK ~ %dK'%(allocatedTable[i][0], allocatedTable[i][2], allocatedTable[i][2] + allocatedTable[i][1]-1))
      print('\n-- Hole List --')
      for i in range(0,len(holeTable)):
        print('Hole %d : %dK ~ %dK'%(i+1, holeTable[i][0], holeTable[i][1]))
    else: 
      print('잘못된 입력입니다. 초기화면으로 돌아갑니다.')

if __name__ == '__main__':
    main()