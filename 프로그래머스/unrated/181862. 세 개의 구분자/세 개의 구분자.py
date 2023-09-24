import re
def solution(myStr):
    if not re.sub("[a-c]","", myStr):
        return ["EMPTY"]
    return ' '.join(re.split("[a-c]", myStr)).split()
