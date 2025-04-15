# Python3 implementation of the Traveling Salesman Problem (TSP) approach V = 4
answer = []

# Function to find the minimum weight Hamiltonian Cycle
def tsp(graph, v, currPos, n, count, cost):
    # If all nodes are visited, check if there's a link to the starting node
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])  # Include the cost to return to the starting node
        return

    # Backtracking step: Loop to traverse the adjacency list of currPos node
    for i in range(n):
        # Proceed only if the node i is not visited and there's a path from currPos to i
        if v[i] == False and graph[currPos][i]:
            # Mark node i as visited
            v[i] = True
            # Recur to the next node
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])
            # Backtrack: Mark node i as unvisited for future explorations
            v[i] = False

# Driver code
if __name__ == '__main__':
    n = 4  # Number of nodes (cities)
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Boolean array to check if a node has been visited or not
    v = [False] * n

    # Start at node 0
    v[0] = True

    # Find the minimum weight Hamiltonian Cycle
    tsp(graph, v, 0, n, 1, 0)

    # The answer contains all possible cycles, now find the minimum cost cycle
    print(min(answer))  # Output the minimum cost
