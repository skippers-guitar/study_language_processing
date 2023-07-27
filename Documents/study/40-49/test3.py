import graphviz

dot = graphviz.Digraph()
dot.attr('graph', layout='dot')
dot.node('A', 'Node A')
dot.node('B', 'Node B')
test =[['A','B'],['C','D'],['A','C']] 
j = 0
for i in test:
    j +=1
    dot.edge(i[0],i[1],'Edge ' + str(j))

dot.render('test', view=True)