from collections import deque

initial_state = (3, 3, 1)
goal_state = (0, 0, 0)

def is_valid_state(m, c):
    return (m == 0 or m >= c) and (m == 3 or m <= 3 - c)

def get_successors(state):
    successors = []
    m, c, b = state
    moves = [(2, 0), (1, 0), (0, 2), (0, 1), (1, 1)] 
    
    if b == 1:  
        for dm, dc in moves:
            new_state = (m - dm, c - dc, 0)
            if is_valid_state(new_state[0], new_state[1]) and new_state[0] >= 0 and new_state[1] >= 0:
                successors.append(new_state)
    else: 
        for dm, dc in moves:
            new_state = (m + dm, c + dc, 1)
            if is_valid_state(new_state[0], new_state[1]) and new_state[0] <= 3 and new_state[1] <= 3:
                successors.append(new_state)
    
    return successors

def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        (state, path) = queue.popleft()
        
        if state in visited:
            continue
        
        visited.add(state)
        path = path + [state]
        
        if state == goal:
            return path
        
        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path))
    
    return None

if __name__ == "__main__":
    path = bfs(initial_state, goal_state)
    
    if path:
        for step in path:
            print(step)
    else:
        print("No solution found")
        
OUTPUT
>>> %Run lol.py
(3, 3, 1)
(3, 1, 0)
(3, 2, 1)
(3, 0, 0)
(3, 1, 1)
(1, 1, 0)
(2, 1, 1)
(0, 1, 0)
(1, 1, 1)
(0, 0, 0)
>>> 

