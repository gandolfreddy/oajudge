from collections import deque

# input
course_dt = {}
for i in range(4):
    courses = input().split()
    course_dt[courses[0]] = courses[1:]
    for course in courses[1:]:
        if not course in course_dt:
            course_dt[course] = []
wish_course = input()

# process
q = deque([wish_course])
order = wish_course
while q:
    cur_c = q.popleft()
    pre_c = course_dt[cur_c]
    if pre_c:
        order = ' '.join(sorted(pre_c)) + ' ' + order
        for c in pre_c:
            q.append(c)

# output
print(order)
