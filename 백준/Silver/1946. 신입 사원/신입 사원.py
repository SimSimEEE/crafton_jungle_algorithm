import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    applicant = sorted(list(tuple(map(int,input().split())) for _ in range(n)))

    hired_people = 0
    hired_applicant = n+1

    for application, interview in applicant:
        if  hired_applicant > interview:
            hired_applicant = interview
            hired_people += 1
    print(hired_people)