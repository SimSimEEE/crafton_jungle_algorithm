def solution(todo_list, finished):
    return [todo_list[i] for i, todo in enumerate(finished) if not todo]