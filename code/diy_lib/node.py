class Node:
    def __init__(self,name,parent,level,feature=None,threshold=None,gini_val=None):
        self.name = name
        self.parent = parent
        self.level = level
        self.gini_val = gini_val #none as defualt
        self.threshold = threshold #none as defualt
        self.left_child = None #none as defualt
        self.right_child = None #none as defualt
        self.feature=feature

    def create_children(self,lchild,rchild):
        """
        Attaches the children to the node
        """
        self.left_child = lchild
        self.right_child = rchild
        
    def parent(self):
        """
        Returns the parent of the node
        """
        return self.parent
    
    def children(self):
        """
        Returns the children of the node
        """
        return self.left_child,self.right_child
    
    def gini_val(self):
        """
        Returns the gini value
        """
        return self.gini_val
    
    def feature(self):
        """
        Returns the feature of the node, 
        which it uses to split
        """
        return self.feature
    
    def threshold(self):
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