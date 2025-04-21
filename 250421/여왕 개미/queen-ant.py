# 전역변수
# 총 명령 개수
totalCommnands = 0

# 각 개미집의 철거 여부를 저장하는 배열
# 인덱스 0인 여왕 개미집은 철거하지 않기 때문에, 인덱스 번호 1부터 사용하기 위해
# 초기에 하나의 값을 추가
antHouseDeleted = [False]

# 각 개미집의 x좌표 위치를 저장
# 인덱스 0은 여왕 개미집 (x=0)을 의미, 이후 인덱스 1부터 실제 개미집 저장
antHousePositions = [0]

def initialVillageConstruction(arr):
    # 마을 건설 명령에서는 처음에 N개의 개미집을 건설하는 명령이 주어짐.
    # numInitialAntHouse 변수에 건설할 개미집의 수를 저장
    numInitialAntHouse = arr[0]

    # 여왕 개미집은 x=0에 건설되며, 이미 antHousePositions 0번째 인덱스에 저장되어 있음.
    # 이후 1번 인덱스부터 numInitialAntHouse까지 개미집을 건설
    # 각 개미집의 위치를 입력으로 주어지며, 오름차순 순서로 주어짐이 보장.
    for i in range(1, numInitialAntHouse + 1):
        position = arr[i]
        # antHousePositions 맨 뒤에 개미집의 위치를 추가
        antHousePositions.append(position)
        # antHouseDeleted 맨 뒤에서 False를 추가하여 해당 개미집이 철거되지 않았음을 기록
        antHouseDeleted.append(False)


def addNewAntHouse(arr):
    newAntHousePosition = arr[0]

    antHousePositions.append(newAntHousePosition)

    antHouseDeleted.append(False)


def removeAntHouse(arr):
    antHouseNumber = arr[0]

    antHouseDeleted[antHouseNumber] = True


def scoutProcess(arr):
    numAnts = arr[0]

    lowerTime = 0
    upperTime = 1000000000

    minTime = 0

    while lowerTime <= upperTime:
        midTime = (lowerTime + upperTime) // 2

        # midTime 내에 하나의 개미가 커버할 수 있는 영역르올 필요로 하는 구간의 수 저장
        intervalsNeeded = 0

        # 이전에 커버된 마지막 개미집의 위치 저장
        lastCoveredPosition = -1000000000

        # 인덱스 0은 여왕 개미집이므로, 인덱스 1부터 개미집의 위치에 대해 검토
        for i in range(1, len(antHousePositions)):
            # 만약 현재 개미집이 철거된 상태라면 건너띔
            if antHouseDeleted[i] == True:
                continue

            # 현재 개미집의 위치를 저장
            currentAntHousePosition = antHousePositions[i]

            # 만약 현재 개미집과 이전에 커버된 마지막 개미집 사이의 거리가 midTime보다 크다면,
            # 새로운 구간(즉, 새로운 일 개미가 출발하여 이 개미집부터 커버를 시작)을 추가
            if currentAntHousePosition - lastCoveredPosition > midTime:
                # 새로운 구간의 시작점을 현재 개미집의 위치로 설정
                lastCoveredPosition = currentAntHousePosition
                # 구간의 수를 1 증가
                intervalsNeeded += 1
        
        # 만약 필요한 구간의 수가 numAnts보다 작거나 같다면,
        # 주어진 midTime 내에 가능한 정찰이 가능하다는 의미
        if intervalsNeeded <= numAnts:
            # midTime 값을 가능한 최소 시간으로 갱신
            minTime = midTime
            # 더 작은 시간으로 정잘이 가능한지 확인하기 위해 upperTime를 midTime - 1로 조정
            upperTime = midTime - 1
        else:
            # 만약 필요한 구간의 수가 numAnts보다 많다면,
            # midTime이 너무 작다는 의미이므로 lowerTime을 midTime + 1
            lowerTime = midTime + 1
    print(minTime)

totalCommnands = int(input())

while totalCommnands:
    totalCommnands -=1

    arr = list(map(int, input().split()))
    commandType = arr[0]

    if commandType == 100:
        initialVillageConstruction(arr[1:])
    elif commandType == 200:
        addNewAntHouse(arr[1:])
    elif commandType == 300:
        removeAntHouse(arr[1:])
    elif commandType == 400:
        scoutProcess(arr[1:])