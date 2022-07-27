class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self,val):
        new_node = Node(val)
        if not self.root:
            self.root = new_node
            return self
        runner = self.root
        while runner != None:
            if val < runner.value:
                if runner.left == None:
                    runner.left = new_node
                    return self
                else:
                    if runner.right == None:
                        runner = runner.right = new_node
                    else:
                        runner = runner.right

    def contains(self,val):
        if self.root == None:
            return "there's no nodes in this tree!"
        runner = self.root
        while runner != None:
            if runner.value == val:
                return True
            if val < runner.value:
                runner = runner.left
            else:
                runner = runner.right

my_first_BST = BST()
my_first_BST.add(20).add(15).add(11).add(17).add(9).add(25).add(37).add(20).add(10)
print(my_first_BST.root.left.right.value)
my_first_BST.contains(17)