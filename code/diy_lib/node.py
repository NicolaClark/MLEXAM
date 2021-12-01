import itertools
import numpy as np
class Node:
    """hi"""
    next_id = 0         
    def __init__(self,parent, level, data = None ,feature=None,threshold=None,gini_val=None):
        self.parent = parent
        self.level = level
        self.gini_val = gini_val #none as defualt
        self.threshold = threshold #none as defualt
        self.left_child = None #none as defualt
        self.right_child = None #none as defualt
        self.feature=feature
        self.id = Node.next_id
        self.data = data
        Node.next_id += 1
    
    def get_id(self):
        """
        Returns the id/name of the node
        """
        return self.id

    def create_children(self,lchild,rchild):
        """
        Attaches the children to the node
        """
        self.left_child = lchild
        self.right_child = rchild
        
    def get_parent(self):
        """
        Returns the parent of the node
        """
        return self.parent
    
    def get_children(self):
        """
        Returns the children of the node
        """
        return self.left_child, self.right_child
    
    def get_gini_val(self):
        """
        Returns the gini value
        """
        return self.gini_val
    
    def get_feature(self):
        """
        Returns the feature of the node, 
        which it uses to split
        """
        return self.feature
    
    def get_threshold(self):
        """
        Returns the threshold, 
        which is a sort of "decision boundary"
        """
        return self.threshold
    
    def get_level(self):
        """
        Returns the level of the nodes
        in the tree
        """
        return self.level
        
    def get_position(self):
        """
        Returns the position in the tree,
        and whether or not it is a root or leaf
        """
        if self.parent==None:
            return("root")
        elif self.left_child == None:
            return('leaf')
        else:
            return f"node at depth {self.get_level()}"


def main():
    pass
if __name__=="__main__":
    main()