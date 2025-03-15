# BFS algorithm on 2D array

# BFS algorithm on 2D array

def Valid(x, y, selected_squares, visited):
	# Check if the coordinates are out of bounds or hit an obstacle
        if x < 0 or x > 900:
                return False
        if y > 900 or y < 100:
                return False
        if (x, y) in selected_squares:
                return False
        if (x, y) in visited:
                return False
        return True

def bfs(start_node, end_node, selected_squares, visited_list):

        from collections import deque
        q = deque()

        visited = set()

        # map selected_squares as visited
        for (x, y) in selected_squares:
                sq = (x, y)
                visited.add(sq)
        
        visited.add(start_node)
        q.append(start_node)

        while q:
                cur_node = q.popleft()
                if cur_node == end_node:
                        return

                visited_list.append(cur_node)

                for (x, y) in [(-50, 0), (50, 0), (0, -50), (0, 50)]:
                        tmp_x = cur_node[0] + x
                        tmp_y = cur_node[1] + y
                        if Valid(tmp_x, tmp_y, selected_squares, visited):
                                q.append((cur_node[0] + x, cur_node[1] + y))
                                visited.add((tmp_x, tmp_y))

def generate_bfs_trace(start_node, end_node, selected_squares):
        visited_list = []
        bfs(start_node, end_node, selected_squares, visited_list)
        return visited_list
