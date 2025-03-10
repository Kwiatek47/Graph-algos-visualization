# DFS algorithm on 2D array

flag = False  # Global flag to stop DFS when target is reached

def Valid(x, y, selected_squares):
	# Check if the coordinates are out of bounds or hit an obstacle
	if x < 0 or x > 900:
		return False
	if y > 900 or y < 100:
		return False
	if (x, y) in selected_squares:
		return False
	return True 

def dfs(cur_node, end_node, selected_squares, visited_set, visited_list):
	global flag  # Declare that we are using the global flag
	if flag is True:  # Stop recursion if target is reached
		return

	if cur_node in visited_set:
		return
	
	visited_set.add(cur_node)
	visited_list.append(cur_node)

	if cur_node == end_node:
		flag = True  # Set flag to True once the target is reached
		return

	u_x, u_y = cur_node

	# Check left neighbor
	if Valid(u_x - 50, u_y, selected_squares):
		dfs((u_x - 50, u_y), end_node, selected_squares, visited_set, visited_list)
	
	# Check right neighbor
	if Valid(u_x + 50, u_y, selected_squares):
		dfs((u_x + 50, u_y), end_node, selected_squares, visited_set, visited_list)

	# Check top neighbor
	if Valid(u_x, u_y - 50, selected_squares):
		dfs((u_x, u_y - 50), end_node, selected_squares, visited_set, visited_list)

	# Check bottom neighbor
	if Valid(u_x, u_y + 50, selected_squares):
		dfs((u_x, u_y + 50), end_node, selected_squares, visited_set, visited_list)

def generate_dfs_trace(start_node, end_node, selected_squares):
	global flag
	flag = False  # Reset flag before starting DFS
	visited_set = set()
	visited_list = []
	dfs(start_node, end_node, selected_squares, visited_set, visited_list)
	return visited_list
