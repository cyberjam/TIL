# 최대한 자료구조를 활용해서 풀려고 했다.
# 하드코딩인가..


def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_walk = [] # 건너는 트럭 
    truck_pass = [] # 지나간 트럭
    truck_weights = [(elem,0) for elem in truck_weights] # 각 트럭마다 지나간 길이를 표시하기 위해 튜플로 
    time=0

    while(len(truck_weights)>0)|(len(truck_walk)>0): # 대기중인 트럭이나 건너고 있는 트럭이 존재할 경우 반복
        time += 1

        if len(truck_walk)>0: # 지나가는 트럭이 존재한다면
            # 지나가고 있는 트럭의 지나간 길이를 이번 회차에 +1 해준다
            truck_walk = [(elem[0],elem[1]+1) for elem in truck_walk] 
            if truck_walk[0][1] >= bridge_length: # 지나가는 트럭 중 1번째 트럭이 다리 길이 만큼 갔다면
                walk_pop = truck_walk.pop(0) # 지나 가는 트럭 list에서 pop해주고 지나간 list에 추가한다.
                truck_pass.append(walk_pop)
                
        walk_sum = sum([elem[0] for elem in truck_walk]) # 지나가는 트럭들의 총 무게를 계산
        
        # 대기 트럭이 남아있다면
        if len(truck_weights)>0: 
            # (이번에 대기 트럭 중 1번째 트럭 무게 + 지나가는 트럭들의 총 무게) 가 다리가 지탱할수 있는 무게(weight) 이하라면
            if walk_sum + truck_weights[0][0] <= weight: 
                wait_pop = truck_weights.pop(0) # 대기 트럭 1번째 트럭이 지나가는 트럭에 합류할 수 있도록 허가
                truck_walk.append(wait_pop)
                
    answer=time
    return answer
    
    
    # 다른 사람 풀이
    # class.. collection 쓰셨네.. 

    import collections

    DUMMY_TRUCK = 0


    class Bridge(object):

        def __init__(self, length, weight):
            self._max_length = length
            self._max_weight = weight
            self._queue = collections.deque()
            self._current_weight = 0

        def push(self, truck):
            next_weight = self._current_weight + truck
            if next_weight <= self._max_weight and len(self._queue) < self._max_length:
                self._queue.append(truck)
                self._current_weight = next_weight
                return True
            else:
                return False

        def pop(self):
            item = self._queue.popleft()
            self._current_weight -= item
            return item

        def __len__(self):
            return len(self._queue)

        def __repr__(self):
            return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


    def solution(bridge_length, weight, truck_weights):
        bridge = Bridge(bridge_length, weight)
        trucks = collections.deque(w for w in truck_weights)

        for _ in range(bridge_length):
            bridge.push(DUMMY_TRUCK)

        count = 0
        while trucks:
            bridge.pop()

            if bridge.push(trucks[0]):
                trucks.popleft()
            else:
                bridge.push(DUMMY_TRUCK)

            count += 1

        while bridge:
            bridge.pop()
            count += 1

        return count


    def main():
        print(solution(2, 10, [7, 4, 5, 6]), 8)
        print(solution(100, 100, [10]), 101)
        print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


    if __name__ == '__main__':
        main()
