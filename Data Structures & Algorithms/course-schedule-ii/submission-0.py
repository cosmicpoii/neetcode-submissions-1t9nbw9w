class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        step 1: build a map from each course to its prerequisites
        step 2: use DFS with 3 states to detect cycles
        step 3: recursively finish all prerequisites before the current course
        step 4: after all prerequisites are finished, add the current course to res
        step 5: if we find a cycle, return [] otherwith return res
        '''
        course_map = {}
        for course in range(numCourses):
            course_map[course] = []

        for course, pre in prerequisites:
            course_map[course].append(pre)

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely finished
        state = [0] * numCourses
        res = []

        def dfs(course):
            # we came back to a course currently in our DFS path -> cycle
            if state[course] == 1:
                return False

            # already completely processed
            if state[course] == 2:
                return True

            # mark as currently visiting
            state[course] = 1

            # first finish all prerequisites
            for pre in course_map[course]:
                if not dfs(pre):
                    return False

            # now this course is safe and finished
            state[course] = 2

            # prerequistes have already been added, so now add this course
            res.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []


        return res
            