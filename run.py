# Search methods

import search

def solve_and_print(problem):
    depth_first = search.depth_first_graph_search(problem)
    breadth_first = search.breadth_first_graph_search(problem)
    branch_and_bound = search.bab(problem)
    subestimation =  search.subBAB(problem)
    print("==================== %s ====================" % (problem.problem_title()))
    print('Busqueda en profundidad: \n', depth_first["solution"].path())
    print('- Nodos visitados: %d\n- Nodos generados %d' % (depth_first["visited_nodes"], depth_first["generated_nodes"]))
    print('Busqueda en anchura: \n', breadth_first["solution"].path())
    print('- Nodos visitados: %d\n- Nodos generados %d' % (breadth_first["visited_nodes"], breadth_first["generated_nodes"]))
    print('Branch & Bound: \n', branch_and_bound["solution"].path())
    print('- Nodos visitados: %d\n- Nodos generados %d' % (branch_and_bound["visited_nodes"], branch_and_bound["generated_nodes"]))
    print('Branch & Bound (subestimation): \n', subestimation["solution"].path())
    print('- Nodos visitados: %d\n- Nodos generados %d' % (subestimation["visited_nodes"], subestimation["generated_nodes"]))
    

solve_and_print(search.GPSProblem('A', 'B', search.romania))
solve_and_print(search.GPSProblem('L', 'Z', search.romania))
solve_and_print(search.GPSProblem('M', 'C', search.romania))
solve_and_print(search.GPSProblem('N', 'R', search.romania))






# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
