class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        for task in tasks: 
            counter[task] = counter.get(task,0) + 1
        maxheap = [-cnt for cnt in counter.values()]

        heapq.heapify(maxheap)

        q = deque()
        time = 0 
        while q or maxheap:  
            time += 1
            if not maxheap : 
                time = q[0][1]
            else : 
                cnt = 1 + heapq.heappop(maxheap)
                if cnt : 
                    q.append([cnt, time+n])
                
            if q and q[0][1] == time : 
                value = q.popleft()[0]
                heapq.heappush(maxheap, value)

        return time 
        


        