from decision_tree import Decision_tree
import numpy as np
from sklearn import datasets 


class random_forrest:
    def __init__(self,data,depth=2,n_trees=100):
        self.data=data
        self.depth=depth
        self.n_trees=n_trees
        pass
    def _vote(self):
        #hard soft later?
        pass
    def _bootstrap_sample(self):
        return self.data
        pass
    def fit(self):
        self.trees=[Decision_tree(_bootstrap_sample(),self.depth) for i in range (self.n_trees)]
        #create random forrest of n trees with n bootstrapped datasets 
        pass
    def predict(self,new_data):
        pass





def main():
    iris=datasets.load_iris()
    tree=Decision_tree(iris)
if __name__=="__main__":
    main()