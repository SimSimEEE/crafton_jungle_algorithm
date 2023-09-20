import re
def solution(myString):
    return re.sub("[a-l]",'l',myString)