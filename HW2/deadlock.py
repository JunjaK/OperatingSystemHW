# 가정사항
# 사용자가 초기 값을 올바르게 줌 
# (초기 Allocation 값, Resource Type, Max Resource를 계산이 불가능하게 주지 않음)

import copy

# Need와 Available를 업데이트합니다.
def updatingNeedAvailable(alloc, maxP, avail, pNum):
    need = []
    available = avail

    print('\n### Need ###')
    for i in range(0, pNum):
        if(len(maxP[i]) != 0):
            line = [x-y for x, y in zip(maxP[i], alloc[i])]
            need.append(line)
            print('process %d : '%(i), line)
        else:
            need.append([])
            print('process %d : Complete!'%(i) )

    for i in range(0, pNum):
        if(len(alloc[i]) != 0):
            available = [x-y for (x, y) in zip(available, alloc[i])]
    
    print('\nAvailable : ', available)

    return available, need

# Safety Algorithm을 실행합니다.
def safetyAlgorithm(alloc, need, avail, maxP, pNum, rNum, compeleted):
    finish = [False for x in range(0, pNum)]
    Work = avail

    print('\n### Safety Algorithm Running! ###')
    for i in range(0, pNum):
        if(len(need[i]) != 0):
            for j in range(0, rNum):
                if(Work[j] < need[i][j]):
                    break
                if(j == rNum - 1):
                    finish[i] = True
                    Work = [x+y for x, y in zip(Work, alloc[i])]
            # 프로세스가 완료됨을 표시
            if(finish[i]):
                print('Process %d is released'%(i))
                print('Process %d is safe state'%(i))
                print('Work :', Work, '\n')
                alloc[i] = []
                need[i] = []
                maxP[i] = []
                compeleted.append(i)
            else:
                print('Process %d is unsafe state.'%(i), '\n')

        else:
            finish[i] = True

    for i in range(0, pNum):
        if(finish[i] == False):
            return False, alloc, need, maxP, compeleted
    
    print('\nThis System is safe state.')
    return True, alloc, need, maxP, compeleted


def main():
    '''
    초기 세팅
    '''
    # 프로세스 및 리소스 개수 입력
    processNum = int(input('프로세스의 수를 입력해주세요(최대 10개) : '))
    resourceNum = int(input('리소스의 수를 입력해주세요(최대 5개) : '))
    completedProcess = []
    checkSafeState = False
    # 리소스 정보 입력
    resource = list(
        map(int, (input('리소스 정보를 입력해주세요(%d개) : ' % (resourceNum)).split())))

    print('\n### t0 시간의 Process들의 Allocation 정보를 입력해주세요. ###')
    Allocation = []
    for i in range(0, processNum):
        while True:
            line = list(
                map(int, (input('%d번째 Process의 현재 리소스 입력(%d개) : ' % (i, resourceNum)).split())))
            if(len(line) == resourceNum):
                break
            else:
                print('입력한 리소스의 수가 부족하거나 많습니다.\n')
        Allocation.append(line)

    print('\n### 각 프로세스의 최대 리소스를 입력해주세요 ###')
    Max = []
    for i in range(0, processNum):
        while True:
            line = list(
                map(int, (input('%d번째 Process의 최대 리소스 입력(%d개) : ' % (i, resourceNum)).split())))
            if(len(line) == resourceNum):
                break
            else:
                print('입력한 리소스의 수가 부족하거나 많습니다.\n')
        Max.append(line)

    Available = copy.deepcopy(resource)
    
    Available, Need = updatingNeedAvailable(Allocation, Max, Available, processNum)


    '''
    알고리즘 시작
    '''
    print("###### 지금부터 Banker's Algorithm을 시작합니다. ######\n")
    while True:
        print("프로그램 종료: 0 | Resource Request: 1")
        userSelect = int(input('원하는 항목을 입력해주세요 : '))
        requestProcessNum = 0
        allocateR = [[] for x in range(0, processNum)]
        
        if(checkSafeState == True):
            break
        elif(userSelect == 0):
            print('프로그램을 종료합니다. \n')
            break

        elif(userSelect == 1):
            # 리소스 pretend allocation
            while True:
                needCheck = True
                availableCheck = True
                # 새로운 작업 할당
                isHoldedTask = sum([len(x) for x in allocateR])
                if(isHoldedTask == 0):
                    # 프로세스 선택
                    while True:
                        if(len(completedProcess) != 0):
                            print('\n완료된 프로세스 : ', *completedProcess)
                        requestProcessNum = int(
                            input('작업을 할당할 프로세스를 선택해주세요(%d ~ %d) : '% (0, processNum-1)))
                        if(requestProcessNum > processNum or requestProcessNum < 0):
                            print('해당하는 프로세스가 없습니다!\n')
                        else:
                            checkRequest = True
                            for i in completedProcess:
                                if(i == requestProcessNum):
                                    checkRequest = False
                            if(checkRequest):
                                break
                            else:
                                print('완료된 프로세스에 작업을 할당할 수 없습니다.\n')
                    # 작업 할당
                    while True:
                        temp = list(map(int, (input('할당할 리소스 입력(%d개) : '%(resourceNum)).split())))
                        if(len(temp) == resourceNum):
                            allocateR[requestProcessNum] = copy.deepcopy(temp)
                            break
                        else:
                            print('입력한 리소스의 수가 부족하거나 많습니다.\n')
                # 보류된 작업 선택
                else:
                    for i in range(0, resourceNum):
                        if(len(allocateR[i]) > 0):
                            requestProcessNum = i
                            break
                print(1, Need)
                print(2, allocateR[requestProcessNum])
                print(3, allocateR[requestProcessNum][0], Need[requestProcessNum][0])
                # need, available 체크  
                for i in range(0, resourceNum):
                    if(allocateR[requestProcessNum][i] > Need[requestProcessNum][i]):
                        needCheck = False
                        break
                    if(allocateR[requestProcessNum][i] > Available[i]):
                        availableCheck = False

                if(needCheck):
                    if(availableCheck):
                        # 작업 할당
                        Allocation[requestProcessNum] = [x+y for (x, y) in zip(Allocation[requestProcessNum], allocateR[requestProcessNum])]

                        # Updating Need, Available
                        Available = copy.deepcopy(resource)
                        Available, Need = updatingNeedAvailable(Allocation, Max, Available, processNum)

                        # SafetyAlgorithm

                        checkSafeState, Allocation, Need, Max, completedProcess = safetyAlgorithm(Allocation, Need, Available, Max, processNum, resourceNum, completedProcess)
                        if(checkSafeState):
                            print('프로세스가 모두 수행됐으므로, 프로그램을 종료합니다!')
                            break
                        else:
                            print('아직 완료되지 않은 프로세스가 있으므로 프로그램을 다시 시작합니다!')
                            allocateR[requestProcessNum] = []
                            Available = copy.deepcopy(resource)
                            Available, Need = updatingNeedAvailable(Allocation, Max, Available, processNum)
                    else:
                        print('할당할 자원이 Available보다 큽니다. 작업을 보류합니다.\n')
                else:
                    allocateR[requestProcessNum] = []
                    print('%d번째 프로세스의 need보다 큰 자원을 할당할 수 없습니다. 다시 자원을 입력해주세요.\n')
            
            
        else:
            print('잘못된 요청입니다. 다시 입력해주세요.\n')

        print('\n----- Safe Sequence : ', completedProcess,' -----')


if __name__ == '__main__':
    main()
