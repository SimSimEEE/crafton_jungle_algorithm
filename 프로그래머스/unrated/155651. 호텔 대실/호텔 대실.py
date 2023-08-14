import heapq

def solution(book_time):
    answer = 0
    rooms = []
    book_time.sort(key=lambda x:x[0])
    for book in book_time:
        check_in = timeTonum(book[0])
        check_out = timeTonum(book[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in:
            heapq.heappop(rooms)
        heapq.heappush(rooms,check_out)
    print(rooms)
    answer = len(rooms)
    return answer

def timeTonum(book_time):
    return 60*int(book_time[:2]) + int(book_time[3:])