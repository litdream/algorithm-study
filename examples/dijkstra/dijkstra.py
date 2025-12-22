"""Sample usage:

$ python3 dijkstra.py directed-graph.json A | jq

"""

import json
import os, sys

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = set(graph.keys())
    predecessors = {}
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        
        if distances[current_node] == float('inf'):
            break
            
        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited:
                new_distance = distances[current_node] + weight
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    
        unvisited.remove(current_node)
        
    return predecessors

if __name__ == '__main__':
    graph = "graph.json"
    start_node = "A"
    
    if len(sys.argv) > 1:
        graph = sys.argv[1]
    if not os.path.exists(graph):
        print(f"Graph file does not exist: {graph}")
        sys.exit(1)

    if len(sys.argv) > 2:
        start_node = sys.argv[2].strip()
        
    with open(graph, 'r') as f:
        data = json.load(f)

    original_graph = data['graph']
    nodes = data['nodes']
    if start_node not in nodes:
        print(f"Your start node does not exist: {start_node}")
        sys.exit(2)
        
    predecessors = dijkstra(original_graph, start_node)
    
    # Initialize the new graph with all nodes
    dijk_graph = {node: {} for node in nodes}
    
    # Reconstruct the graph with only the shortest path edges
    for node, pred in predecessors.items():
        weight = original_graph[pred][node]
        dijk_graph[pred][node] = weight
        
    output_data = {
        "nodes": nodes,
        "graph": dijk_graph
    }

    print(json.dumps(output_data, indent=0))
