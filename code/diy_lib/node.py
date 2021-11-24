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
        self.left_child = lchild
        self.right_child = rchild
        #make a child
        
    def parent(self):
        return self.parent
    
    def children(self):
        return self.left_child,self.right_child
    
    def gini_val(self):
        return self.gini_val
    
    def feature(self):
        return self.feature
    
    def threshold(self):
        return self.threshold
    
    def get_level(self):
        return self.level
        
    def get_position(self):
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