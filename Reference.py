import sys
import gc

class Node():
    def __init__(self, name):
        self.name = name
        self.link = None

node_a = Node("A")
node_b = Node("B")

node_a.link = node_b
node_b.link = node_a

print("Reference to A: ", sys.getrefcount(node_a))
print("Reference to B: ", sys.getrefcount(node_b))

del node_a
del node_b

print("Running Garbage Collector...")
unreachable_obj = gc.collect()

print("Number of ghost objects destroyed: ", unreachable_obj)