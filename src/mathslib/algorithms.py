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
Various known algorithms, graph theory and optimization related

Author: Igor van Loo
'''
def PrimsAlgorithm(matrix):
    '''
    Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    See here: https://en.wikipedia.org/wiki/Prim%27s_algorithm
    Implementation is based of Wikipedia
    
    Parameters
    ----------
    graph : Takes a matrix input

    Returns
    -------
    The minimum spanning tree for the weighted undirected Graph

    '''
    dimension = len(matrix)
    Previous_Weight = sum([matrix[x][y] for x in range(dimension) for y in range(x+1, dimension) if matrix[x][y] != 0])
    Tree = set([0])
    New_Weight = 0    
    for x in range(dimension - 1):
        Minimum_edge, Corresponding_vertex = min([(matrix[x][y], y) for x in Tree for y in range(dimension) if y not in Tree and matrix[x][y] != 0])
        Tree.add(Corresponding_vertex)
        New_Weight += Minimum_edge
        if len(Tree) == dimension:
            break
    return Previous_Weight - New_Weight

def DijkstrasAlgorithm(matrix, start_node = (0, 0), end_node = (-1, -1)):
    '''
    Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph
    See here: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    Implementation is based of Wikipedia
    
    Parameters
    ----------
    matrix : Takes a matrix input, representing the graph, assumes all nodes are connected

    Returns
    -------
    Shortest path between desired starting and ending node
    '''
    rows = len(matrix)
    columns = len(matrix[0])
    INF = 10**8    
    unvisisted_nodes = dict()
    for x in range(rows):
        for y in range(columns):
            unvisisted_nodes[(x, y)] = INF
    unvisisted_nodes[(0, 0)] = matrix[0][0]    
    mask = [[INF]*columns for i in range(rows)]
    mask[0][0] = matrix[0][0]    
    def visit_neighbour(og_x, og_y, x, y, unvisisted_nodes):
        if x < 0 or x >= rows or y < 0 or y >= columns:
            return False
        if (x, y) in unvisisted_nodes:
            return min(mask[x][y], mask[og_x][og_y] + matrix[x][y])
    curr = start_node #Starting node
    while True:
        x, y = curr
        for (a, b) in ((x + 1, y), (x, y+ 1), (x - 1, y), (x, y - 1)):
            temp = visit_neighbour(x, y, a, b, unvisisted_nodes)
            if temp:
                mask[a][b] = temp
                unvisisted_nodes[(a, b)] = temp
        unvisisted_nodes.pop(curr)        
        if len(unvisisted_nodes) != 0:
            curr = min(unvisisted_nodes, key=unvisisted_nodes.get)
        else:
            break
    if end_node == (-1, -1):
        return mask[rows - 1][columns - 1] #Ending node
    else:
        a, b = end_node
        return mask[a - 1][b - 1]

def KnapSack(values, weights, n, W, no_values = True):
    '''
    Given a set of items, each with a weight and a value, determine the number of each item to include in a 
    collection so that the total weight is less than or equal to a given limit and the total value is as 
    large as possible
    See here: https://en.wikipedia.org/wiki/Knapsack_problem
    
    Parameters
    ----------
    values : A list of values
    weights : A list with weight of corresponding values
    n : Number of items (len(values))
    W : Desired weight
    no_values : TYPE, optional
                Default is True
        

    Returns
    -------
    If no_values == True - It returns the optimal sum of weights
    If no_values == False - it returns the entire array, which is used in KnapSackValues to find which values were 
    actually used in the optimal sum
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
    if not no_values:
        return array
    
def KnapSackValues(values, weights, n, W):
    '''
    Extension to KnapSack function
    It finds the actual values used to obtain the optimal sum

    Parameters
    ----------
    values : A list of values
    weights : A list with weight of corresponding values
    n : Number of items (len(values))
    W : Desired weight

    Returns
    -------
    A set with the optimal values
    '''
    array = KnapSack(values, weights, n, W, no_values = False)
    if n == 0:
        return {}
    if array[n][W] > array[n - 1][W]:
        return {weights[n - 1]}.union(KnapSackValues(values, weights, n - 1, W - weights[n - 1]))
    
    
    