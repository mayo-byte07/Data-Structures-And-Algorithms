from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        completed_count = 0
        while queue:
            current = queue.popleft()
            completed_count += 1
            for next_course in graph[current]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        return completed_count == numCourses