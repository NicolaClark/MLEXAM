import pandas
from typing import List
from itertools import combinations
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import math

class Node:
    """hi"""
    next_id = 0         
    def __init__(self,parent, level, data = None ,feature=None,threshold=None,gini_val=None,most_common_class=None):
        self.most_common_class=most_common_class
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

    def create_children(self,lchild,rchild):
        """
        Attaches the children to the node
        """
        self.left_child = lchild
        self.right_child = rchild
    
    def get_children(self):
        """
        Returns the children of the node
        """
        return self.left_child, self.right_child
    
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
            return f"node at depth {self.level}"

    def get_info(self):
        if self.parent == None:
            parent_id = None
        else:
            parent_id = self.parent.id
        if self.get_children()[0] == None:
            children_id = [None,None]
        else:
            children_id=[self.get_children()[0].id,self.get_children()[1].id]
        return f"ID: {self.id} \nParent: {parent_id} \nChildren: {children_id}\nMost_common_class: {self.most_common_class} \nFeature: {self.feature} \nThreshold: {self.threshold} \nGini: {self.gini_val} \nDepth: {self.level} \nPosition: {self.get_position()}\nAmount of Datapoints: {len(self.data)}\nClasses of Datapoints: {Counter(self.data['type'])}"
        


def main():
    pass
if __name__=="__main__":
    main()