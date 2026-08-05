class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        step 1: build a graph that maps each course to its prerequisites
        step 2: use DFS to check every course
        step 3: mark a course as visiting while checking its prerequisites
        step 4: if we visit a course that is already visiting, there is a cycle, so return False
        step 5: after all prerequisites are checked, mark the course as completed
        step 6: if no cycle is found, return True
        '''
        course_map = {}
        for course in range(numCourses):
            course_map[course] = []

        for course, prerequisite in prerequisites:
            course_map[course].append(prerequisite)

        # 0 = unvisited
        # 1 = visited
        # 2 = completed
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False

            if state[course] == 2:
                return True

            state[course] = 1

            for prerequisite in course_map[course]:
                if not dfs(prerequisite):
                    return False

            state[course] = 2

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True