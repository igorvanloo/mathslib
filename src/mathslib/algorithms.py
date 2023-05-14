# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>


'''
Various known algorithms. They are graph theory and optimization related

Author: Igor van Loo
'''

from .simple import is_clockwise

def prims_algorithm(matrix):
    '''
    Implementation of `Prim's algorithm <https://en.wikipedia.org/wiki/Prim%27s_algorithm>`_
    It finds a Minimum Spanning Tree (MST) for a weighted undirected graph.
        
    :param matrix: Takes a `Adjacency matrix <https://en.wikipedia.org/wiki/Adjacency_matrix>`_ as input
    
    :returns Weight: The sum of the minimum spanning tree
    :returns mask: The corresponding Adjacency matrix of the MST
    
    Example from Project `Euler Problem 107 <https://projecteuler.net/problem=107>`_
    
    .. code:: python
        
        matrix = [[0, 16, 12, 21, 0, 0, 0], 
                  [16, 0, 0, 17, 20, 0, 0], 
                  [12, 0, 0, 28, 0, 31, 0], 
                  [21, 17, 28, 0, 18, 19, 23], 
                  [0, 20, 0, 18, 0, 0, 11], 
                  [0, 0, 31, 19, 0, 0, 27], 
                  [0, 0, 0, 23, 11, 27, 0]]
        
        print(prims_algorithm(matrix)) #(93, 
                                      #[[0, 16, 12, 0, 0, 0, 0],
                                      #[16, 0, 0, 17, 0, 0, 0],
                                      #[12, 0, 0, 0, 0, 0, 0],
                                      #[0, 17, 0, 0, 18, 19, 0],
                                      #[0, 0, 0, 18, 0, 0, 11],
                                      #[0, 0, 0, 19, 0, 0, 0],
                                      #[0, 0, 0, 0, 11, 0, 0]])
    
    '''
    dimension = len(matrix)
    mask = [[0 for x in range(len(matrix[0]))] for x in range(dimension)]
    Tree = set([0])
    Weight = 0    
    for x in range(dimension - 1):
        Minimum_edge, a, b = min([(matrix[x][y], x, y) for x in Tree for y in range(dimension) if y not in Tree and matrix[x][y] != 0])
        Tree.add(b)
        mask[a][b] = matrix[a][b]
        mask[b][a] = matrix[a][b]
        Weight += Minimum_edge
        if len(Tree) == dimension:
            break
    return Weight, mask

def dijkstras_algorithm(graph, start_node = 0, INFINITY = 10**10):
    '''
    Implementation of `Dijkstra's algorithm <https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm>`_ 
    It finds the the shortest paths between nodes in a graph

    :param graph: Takes an adjacency list as input
    :param start_node: Optional tuple, default is node 0.
    :param INFINITY: Optional integer, default is 10^10. It is used to set the "Infinty" value

    :returns: Shortest path between start_node and all other nodes
        
    Example from the wikipedia page
    
    .. code:: python
    
        g = [[[1, 7], [2, 9], [5, 14]],
             [[0, 7], [2, 10], [3, 15]],
             [[0, 9], [1, 10], [3, 11], [5, 2]],
             [[1, 15], [2, 11], [4, 6]],
             [[3, 6], [5, 9]],
             [[0, 14], [2, 2], [4, 9]]
            ]
        
        print(dijkstras_algorithm(g)) #[0, 7, 9, 20, 20, 11]
    
    .. note::
        
        A quick comment on this adjacency list. The way it works is for example g[i] contains all the nodes
        node i is connected to. For example, using the above graph g[0] = [[1, 7], [2, 9], [5, 14]] means node 0 is connected to nodes
        1, 2, and 5 and the weight between the edges are 7, 9, and 14 respectively
        
    '''
    n = len(graph)
    D = [INFINITY]*n
    D[start_node] = 0
    cloud = [False for i in range(n)]
    for i in range(n):
        _, v = min((D[i], i) for i in range(n) if cloud[i] == False)
        cloud[v] = True        
        for b, w in graph[v]:
            if cloud[b] == False:
                t = D[v] + w
                if t < D[b]:
                    D[b] = t
        flag = True
        for i in range(n):
            if cloud[i] == False:
                if D[i] != INFINITY:
                    flag = False
                    break
        if flag:
            break
    return D

def floyd_warshall_algorithm(graph, INFINITY = 10**10):
    '''
    Implementation of the `Floyd-Warshall algorithm <https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm>`_ 
    It finds the the shortest paths between every node in the graph to every node in the graph

    :param graph: Takes an adjacency list as input
    :param INFINITY: Optional integer, default is 10^10. It is used to set the "Infinty" value

    :returns: Shortest path between every node to every node
        
    Example from the wikipedia page
    
    .. code:: python
    
        g = [[[1, 7], [2, 9], [5, 14]],
             [[0, 7], [2, 10], [3, 15]],
             [[0, 9], [1, 10], [3, 11], [5, 2]],
             [[1, 15], [2, 11], [4, 6]],
             [[3, 6], [5, 9]],
             [[0, 14], [2, 2], [4, 9]]
            ]
        
        print(floyd_warshall_algorithm(g)) #[[0, 7, 9, 20, 20, 11],
                                          # [7, 0, 10, 15, 21, 12],
                                          # [9, 10, 0, 11, 11, 2],
                                          # [20, 15, 11, 0, 6, 13],
                                          # [20, 21, 11, 6, 0, 9],
                                          # [11, 12, 2, 13, 9, 0]]
    .. note::
        
        This process is like applying Dijkstras Algorithm on every node
        
    '''
    n = len(graph)
    D = [[[ INFINITY for i in range(n) ] for j in range(n) ] for k in range(n+1) ]
    for v in range(n):
        D[0][v][v] = 0
        for e, w in graph[v]:
            D[0][v][e] = w            
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[k+1][i][j] = min(D[k][i][j], D[k][i][k] + D[k][k][j])
    return D[n][:][:]

def knap_sack(values, weights, n, W, no_values = True):
    '''
    Implementation of dynamic programming solution to the 0-1 `Knapsack Problem <https://en.wikipedia.org/wiki/Knapsack_problem>`_
    
    :param values: A list of values
    :param weights: A list with weight of corresponding values
    :param n: Number of items
    :param W: Desired weight
    :param no_values: Optional boolean value
        
    :returns:
        * If no_values == True - It returns the optimal sum of weights
        * If no_values == False - it returns the entire array used to build up the solution
        
    .. code-block:: python
        
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        print(knap_sack(values, weights, n, W)) #220
    '''
    array = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                array[i][j] = 0
                
            elif weights[i - 1] > j:
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = max(array[i - 1][j], array[i - 1][j - weights[i - 1]] + values[i - 1])
    
    if no_values:
        return array[n][W]
    
    if no_values == False:
        return array
    
def knap_sack_values(values, weights, n, W):
    '''
    Extension to KnapSack function
    It finds the actual values used to obtain the optimal sum

    :param values: A list of values
    :param weights: A list with weight of corresponding values
    :param n: Number of items
    :param W: Desired weight

    :returns: A set with the optimal values which form the solution to the knapsack problem
    
    .. code-block:: python
        
        values = [60, 100, 120]
        weights = [10, 20, 30]
        W = 50
        n = len(values)
        
        print(knap_sack_values(values, weights, n, W)) #{20, 30}
    
    '''
    array = knap_sack(values, weights, n, W, no_values = False)
    if n == 0:
        return {}
    if array[n][W] > array[n - 1][W]:
        return {weights[n - 1]}.union(knap_sack_values(values, weights, n - 1, W - weights[n - 1]))
    else:
        return knap_sack_values(values, weights, n - 1, W - weights[n - 1])

def BFS(g, start_node = 0, end_node = False):
    '''
    Implementation of `Breadth First Search <https://en.wikipedia.org/wiki/Breadth-first_search>`_

    :param g: An `Adjacency List <https://en.wikipedia.org/wiki/Adjacency_list>`_
    :param start_node: Optional, pick your start node. Default is 1st node
    :param end_node: Optional, pick your end node. Default is last node

    :returns: A list of nodes which create a path from your start_node to end_node if it exists
    
    .. code-block:: python
        
        G = [[4, 1], [0, 5], [6, 3], [2, 7],
             [0, 8], [1, 6], [2, 5, 10], [3, 11],
             [4, 9], [8, 13], [6], [7, 15],
             [13], [9, 12, 14], [13, 15], [11, 14] ]
        
        print(BFS(G)) #[0, 4, 8, 9, 13, 14, 15]
    
    .. note::
        
        A quick comment on adjacency lists. The way it works is for example G[i] contains all the nodes
        node i is connected to. For example using the above graph G[0] = [4, 1] means node 0 is connected to nodes 1, and 4.
        
    '''
    if end_node == False:
        end_node = len(g) - 1
        
    vertices = [0 for _ in range(len(g))] 
    path = [start_node] 
    queue = [(start_node, path)] 
    while queue != []:
        curr_v, path = queue.pop(0)
        
        if vertices[curr_v] != 1: 
            vertices[curr_v] = 1
            if curr_v == end_node:
                return path
            
            for v in g[curr_v]:
                if vertices[v] != 1:
                    new_path = path + [v]
                    queue.append((v, new_path))
    return []

def DFS(g, start_node = 0, end_node = False):
    '''
    Implementation of `Depth First Search <https://en.wikipedia.org/wiki/Depth-first_search>`_

    :param g: An `Adjacency List <https://en.wikipedia.org/wiki/Adjacency_list>`_
    :param start_node: Optional, pick your start node. Default is 1st node
    :param end_node: Optional, pick your end node. Default is last node

    :returns: A list of nodes which create a path from your start_node to end_node if it exists
    
    .. code-block:: python
        
        G = [[4, 1], [0, 5], [6, 3], [2, 7],
             [0, 8], [1, 6], [2, 5, 10], [3, 11],
             [4, 9], [8, 13], [6], [7, 15],
             [13], [9, 12, 14], [13, 15], [11, 14] ]
        
        print(DFS(G)) #[0, 1, 5, 6, 2, 3, 7, 11, 15]
    
    '''
    if end_node == False:
        end_node = len(g) - 1
        
    vertices = [0 for _ in range(len(g))]
    path = [start_node]
    stack = [(start_node, path)]
    while stack != None:
        curr_v, path = stack.pop(-1)
        
        if vertices[curr_v] != 1:
            vertices[curr_v] = 1
            if curr_v == end_node:
                return path
            
            for v in g[curr_v]:
                if vertices[v] != 1:
                    new_path = path + [v]
                    stack.append((v, new_path))
    return []

def convex_hull_gift_wrapping(pts):
    '''
    Implementation of the Convex Hull `Gift Wrapping Algorithm <https://en.wikipedia.org/wiki/Gift_wrapping_algorithm>`_
    
    :param pts: A list containing 2D points
        
    :returns: A list of points consisting of the convex hull starting from leftmost point going around
        
    '''
    lp = min(pts) 
    convex_hull = [lp]
    hull_not_finished = True
    while hull_not_finished:
        p = convex_hull[-1] 
        for q in pts:
            if q != p:
                flag = True 
                for r in pts:
                    if (r != p) and (r != q):
                        if is_clockwise(p, q, r) == False:
                            flag = False
                            break    
                if flag:
                    if q == lp:
                        hull_not_finished = False
                    else:
                        convex_hull.append(q)
    return convex_hull

def convex_hull_DC(pts):
    '''
    Implementation of the Convex Hull Divide and conquer Algorithm
    
    :param pts: A list containing 2D points
        
    :returns: A list of points consisting of the convex hull starting from leftmost point going around
        
    '''
    x_sort = sorted(pts)
    
    def divideCH(alist):
        l = len(alist) #Length of alist
        if l <= 5:
            return convex_hull_gift_wrapping(alist)
        mid = l//2
        left = divideCH(alist[:mid])
        right = divideCH(alist[mid:])
        return mergeCH(left, right)

    def mergeCH(left, right):
        top_r = max(left) 
        top_l = min(right) 
        bot_r = top_r
        bot_l = top_l
            
        curr_right_index = right.index(top_l)
        curr_left_index = left.index(top_r)
        
        hull_copy = left[:curr_left_index + 1] + right[curr_right_index:] + right[curr_right_index:curr_right_index + 1] + left[curr_left_index:]
        len_h = len(hull_copy)
        
        top_r_index = curr_left_index
        top_l_index = top_r_index + 1
        bot_l_index = top_l_index + len(right)
        bot_r_index = bot_l_index + 1
        
        prev_r = None
        prev_l = None
        while True:
            prev_r = top_r
            prev_l = top_l
            while is_clockwise(top_r, top_l, hull_copy[top_l_index + 1]) == False:
                top_l_index += 1
                top_l = hull_copy[top_l_index]

            while is_clockwise(top_l, top_r, hull_copy[top_r_index - 1]):
                top_r_index -= 1            
                top_r = hull_copy[top_r_index]
            
            if top_r == prev_r and top_l == prev_l:
                break
        
        prev_r = None
        prev_l = None
        while True:
            prev_r = bot_r
            prev_l = bot_l
            
            while is_clockwise(bot_r, bot_l, hull_copy[bot_l_index - 1]):
                bot_l_index -= 1
                bot_l = hull_copy[bot_l_index]
                
            while True:
                if bot_r_index + 1 < len_h:
                    if is_clockwise(bot_l, bot_r, hull_copy[bot_r_index + 1]) == False:
                        bot_r_index += 1
                        bot_r = hull_copy[bot_r_index]
                    else:
                        break
                else:
                    bot_r_index = -1     
            if bot_r == prev_r and bot_l == prev_l:
                break
        
        if bot_r_index == 0:
            convex_hull = hull_copy[0:top_r_index + 1] + hull_copy[top_l_index:bot_l_index + 1]
        else:
            convex_hull = hull_copy[0:top_r_index + 1] + hull_copy[top_l_index:bot_l_index + 1] + hull_copy[bot_r_index:]
        return convex_hull 
    
    return divideCH(x_sort)

  
    