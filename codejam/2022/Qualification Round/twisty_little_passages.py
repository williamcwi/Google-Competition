from math import ceil

def get_room():
    try: 
        room, passage = list(map(int, input().split()))
        return room, passage
    except Exception:
        print('Wrong Answer')
        quit()

def walk():
    print('W', flush=True)

def teleport(location):
    print('T {}'.format(location), flush=True)

def guess(location):
    print('E {}'.format(location), flush=True)

def solve(n, k):

    rooms = [[]] * n

    visited = []

    room_num, num_of_passages = get_room()
    rooms[room_num-1] = [None] * num_of_passages
    visited.append(room_num)
    not_visited = list(set(range(1, n+1)) - set(visited))
    
    for _ in range(k):

        flat_list = [item for sublist in rooms for item in sublist]
        
        if all(x is None for x in rooms[room_num-1]):
            walk()
            mem = room_num
            room_num, num_of_passages = get_room()
            if room_num in visited and mem in rooms[room_num-1]:
                continue
            if room_num not in visited: 
                rooms[room_num-1] = [None] * num_of_passages

            rooms[mem-1].remove(None)
            rooms[mem-1].append(room_num)
            rooms[room_num-1].remove(None)
            rooms[room_num-1].append(mem)

            visited.append(room_num)
            visited = list(dict.fromkeys(visited))
            not_visited = list(set(range(1, n+1)) - set(visited))

        elif len(visited) < n:
            
            teleport(not_visited[0])
            mem = room_num

            room_num, num_of_passages = get_room()
            if room_num in visited:
                continue
            rooms[room_num-1] = [None] * num_of_passages

            visited.append(room_num)
            visited = list(dict.fromkeys(visited))
            not_visited = list(set(range(1, n+1)) - set(visited))

        else:
            result = int(len(flat_list)/2)
            guess(result)
            break
    
    for l in rooms:
        if not l:
            l.append(None)

    flat_list = [item for sublist in rooms for item in sublist]
    result = int(ceil(len(flat_list)/2))
    guess(result)

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        n, k = list(map(int, input().split()))
        solve(n, k)