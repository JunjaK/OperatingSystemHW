import time
def main():
  '''
  초기 세팅
  '''
  # 초기 값 입력
  hashQueueSize = int(input('Hash Queue Header Size N을 입력해주세요(3<=N<=9) : '))
  hashQueue = [[] for i in range (0, hashQueueSize)]
  sleepList = [[] for i in range (0, hashQueueSize)]

  # HashQueue 초기화
  for i in range(0, hashQueueSize):
    tempblock = list(map(int, (input('%d번째, 각 Queue별로 할당되어있는 block의 개수 n과 n개의 블록 번호를 입력해주세요((3<=n<=9) : '%(i+1)).split()))) 
    hashQueue[i] = [str(tempblock[j]) for j in range(1, tempblock[0]+1)]
    sleepList[i] = [0 for j in range(0, tempblock[0])]
  
  # free list 초기화
  tempblock= list(map(int, (input('Free list에 있는 block의 개수와 m과 m개의 블록 번호를 입력 해주세요((3<=m<=9) : ').split()))) 
  freeList = [tempblock[i] for i in range(1, tempblock[0]+1)]

  while True:
    print('\n### HashQueue ###')
    for i in range (0, hashQueueSize):
      print('blk no %d mod %d '%(i, hashQueueSize), hashQueue[i])
    print('Free List ', freeList)
    
    print('\n### Select Operation ###')
    print('1. Change block status to delayed write')
    print('2. getblk')
    print('3. exit')

    op = list(map(int, (input('\nEnter Operation : ').split())))
    print()
    block = 0

    if(op[0] != 3):
      block = op[1]

    if(op[0] == 1):
      for i in range(0, len(hashQueue[block % hashQueueSize])):
        if(int(hashQueue[block % hashQueueSize][i]) == block):
          hashQueue[block % hashQueueSize][i] = hashQueue[block % hashQueueSize][i] + '_delayed_write'

    elif(op[0] == 2):
      while True:
        checkBlockInHash = False # 블록이 해쉬대기행열에 있는지 여부 체크
        hashBufferIndex = -1 # 
        for i in range(0, len(hashQueue[block % hashQueueSize])):
          if(hashQueue[block % hashQueueSize][i].find('_') == -1):
            if(int(hashQueue[block % hashQueueSize][i]) == block):
              checkBlockInHash = True
              hashBufferIndex = i
                    
        # 블록이 해쉬대기행열에 있음
        if(checkBlockInHash):
          checkBlockFree = False
          freeBufferIndex = -1
          for i in range(0, len(freeList)):
            if(block == freeList[i]):
              checkBlockFree = True
              freeBufferIndex = i
          # 경우 1 버퍼가 사용 중이지 않음
          if(checkBlockFree):
            print('--- return block %d ---'%(freeList[freeBufferIndex]))
            del freeList[freeBufferIndex]
            break
          # 경우 5 버퍼가 사용 중
          else:
            if(sleepList[block % hashQueueSize][hashBufferIndex] == 3):
              sleepList[block % hashQueueSize][hashBufferIndex] = 0
              freeList.append(int(hashQueue[block % hashQueueSize][hashBufferIndex]))
            else:
              print ("## block %d not in freelist, Sleep 1 second ##"%(block))
              time.sleep(1)
              sleepList[block % hashQueueSize][hashBufferIndex] += 1

        # 블록이 해쉬대기행열에 없음
        else:
          # 경우 4 자유리스트 상에 버퍼가 없음 - 
          if(len(freeList) == 0):
            if(sleepList[block % hashQueueSize][0] == 3):
              sleepList[block % hashQueueSize][0] = 0
              tempIndex = hashQueue[block % hashQueueSize][0].find('_')
              if(tempIndex == -1):
                freeList.append(int(hashQueue[block % hashQueueSize][0]))
              else:
                freeList.append(int(hashQueue[block % hashQueueSize][0][0:tempIndex]))
            else:
              print ("## Sleep 1 second for free block %s ##"%(hashQueue[block % hashQueueSize][0]))
              time.sleep(1)
              sleepList[block % hashQueueSize][0] += 1
          else:
            checkCase2 = False
            checkCase3 = False
             # 경우 3 버퍼에 delayed write 
            for i in range (0, len(freeList)):
              for j in range(0, len(hashQueue[freeList[i] % hashQueueSize])):
                tempIndex = hashQueue[freeList[i] % hashQueueSize][j].find('_')
                if(tempIndex != -1):
                  if(int(hashQueue[freeList[i] % hashQueueSize][j][0:tempIndex]) == freeList[i]):
                    print('--- return delayed write block %d ---'%(freeList[i]))
                    hashQueue[freeList[i] % hashQueueSize][j] = hashQueue[freeList[i] % hashQueueSize][j][0:tempIndex]
                    del freeList[i]
                    checkCase3 = True
                    break
              if(checkCase3):
                break

            # 경우 2 빈 버퍼의 검출
            if(checkCase3 == False):
              for i in range(0, len(hashQueue[freeList[0] % hashQueueSize])):
                if(int(hashQueue[freeList[0] % hashQueueSize][i]) == freeList[0]):
                  del hashQueue[freeList[0] % hashQueueSize][i]
                  del freeList[0]
                  hashQueue[block % hashQueueSize].append(str(block))
                  checkCase2 = True
                  print('--- return block %d ---'%(block))
                  break
              if(checkCase2):
                break

    elif(op[0] == 3):
      print('Exit Program')
      break
    

if __name__ == '__main__':
    main()