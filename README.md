# Travelling Salesman Problem

Implementación de diferentes algoritmos de resolución del problema del viajero. Se partió de un código base aportado por el profesor, que contenía la implementacion de la búsqueda en anchura y en profundidad.

Se tuvo que implementar los metidos de Ramificación y Acotación (`babg(Queue)`) y Ramificación y Acotación con subestimación (`subBABg(Queue)`). 

Además se modificó el método `graph_search` para contabilizar los nodos generados y visitados a lo largo de la ejecución del camino.

A continuación se puede observar los resultados de distintas ejecuciones para hallar distintos caminos:

```
==================== Problema de Ciudad A a Ciudad B ====================
Busqueda en profundidad: 
 [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]
- Nodos visitados: 10
- Nodos generados 3
Busqueda en anchura: 
 [<Node B>, <Node F>, <Node S>, <Node A>]
- Nodos visitados: 16
- Nodos generados 2
Branch & Bound: 
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
- Nodos visitados: 24
- Nodos generados 2
Branch & Bound (subestimation): 
 [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
- Nodos visitados: 6
- Nodos generados 3
==================== Problema de Ciudad L a Ciudad Z ====================
Busqueda en profundidad: 
 [<Node Z>, <Node O>, <Node S>, <Node F>, <Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>]
- Nodos visitados: 18
- Nodos generados 2
Busqueda en anchura: 
 [<Node Z>, <Node A>, <Node T>, <Node L>]
- Nodos visitados: 8
- Nodos generados 2
Branch & Bound: 
 [<Node Z>, <Node A>, <Node T>, <Node L>]
- Nodos visitados: 10
- Nodos generados 3
Branch & Bound (subestimation): 
 [<Node Z>, <Node A>, <Node T>, <Node L>]
- Nodos visitados: 6
- Nodos generados 3
==================== Problema de Ciudad M a Ciudad C ====================
Busqueda en profundidad: 
 [<Node C>, <Node P>, <Node R>, <Node S>, <Node A>, <Node T>, <Node L>, <Node M>]
- Nodos visitados: 11
- Nodos generados 3
Busqueda en anchura: 
 [<Node C>, <Node D>, <Node M>]
- Nodos visitados: 5
- Nodos generados 2
Branch & Bound: 
 [<Node C>, <Node D>, <Node M>]
- Nodos visitados: 7
- Nodos generados 2
Branch & Bound (subestimation): 
 [<Node C>, <Node D>, <Node M>]
- Nodos visitados: 3
- Nodos generados 2
==================== Problema de Ciudad N a Ciudad R ====================
Busqueda en profundidad: 
 [<Node R>, <Node S>, <Node F>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
- Nodos visitados: 14
- Nodos generados 4
Busqueda en anchura: 
 [<Node R>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
- Nodos visitados: 16
- Nodos generados 1
Branch & Bound: 
 [<Node R>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
- Nodos visitados: 17
- Nodos generados 3
Branch & Bound (subestimation): 
 [<Node R>, <Node P>, <Node B>, <Node U>, <Node V>, <Node I>, <Node N>]
- Nodos visitados: 9
- Nodos generados 3
```
