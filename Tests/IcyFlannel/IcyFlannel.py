# encoding: utf8
from graphviz import Digraph, Graph

graph = Digraph(comment='Test')
graph.format = 'png'

graph1 = Digraph('S1')
graph1.node('A')
graph1.node('Test1')
graph1.node('Test2')

graph2 = Digraph('S2')
graph2.node('B')
graph2.node('C')

graph.subgraph(graph1)
graph.subgraph(graph2)

graph.edge(head_name='S1', tail_name='S2')

graph.render('test')
