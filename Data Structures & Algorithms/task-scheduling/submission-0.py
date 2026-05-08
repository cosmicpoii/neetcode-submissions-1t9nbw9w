class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        1. use hashmap to store each task and its frequency
        2. find the maxFreq(the maximum number of tasks)
            e.g. tasks = ["A","A","A","B","C"], 3A -> maxFreq = 3
        3. find the maxCount(how many tasks meet the maxFreq)
        4. (maxFreq - 1) * (n + 1) + maxCount
            A, _, _, _, A, _, _, _, A
            <-(n + 1)-> 
        5. if there are enough tasks, we don't need idle, 
            so max(num(tasks), (maxFreq - 1) * (n + 1) + maxCount)
        '''
        task_map = {}
        for i in tasks:
            # if not i in task_map:
                # task_map.append(i, 0)
            # else:
                # task_map.append(i, task_map.get(i) + 1)
            task_map[i] = task_map.get(i, 0) + 1

        maxFreq = 0
        maxCount = 0
        for freq in task_map.values():
            if freq > maxFreq:
                maxFreq = freq

        for freq in task_map.values():
            if freq == maxFreq:
                maxCount += 1

        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)