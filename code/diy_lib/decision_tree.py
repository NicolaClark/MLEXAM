class Decision_tree:
    
    def __init__(self,depth,min_samples_split=2,entropy=False):
        self.entropy_choice=entropy
        self.depth = depth
        self.min_samples_split=min_samples_split
        self.tree = {}
    
    def _splitable(self,current_n,data):#end conditions where we dont split and instead we make leaves 
        if current_n.level >= self.depth:
            return False
        elif len(data)<self.min_samples_split:
            return False
        else:
            return True
   
    def _create_tree(self, current_n,tree, data):
        #should we split?
        """This function is creating nodes though recursion"""
        if self._splitable(current_n,data)==False:
            pass
        #we are splitting
        elif self.entropy == True:
            split = self.find_split(data, self.entropy) #(gini_min, threshold, best_feature)
            current_n.gini_val = split[0]
            current_n.threshold = split[1]
            current_n.feature = split[2]

            mask = data[split[2]]>split[1]
            rightsplit = data[mask]
            leftsplit = data[-mask] #check right split on feature contains higher values 
            l_child = Node(parent = current_n, data = leftsplit, gini_val = self._gini_oneside(leftsplit["type"]) ,level = current_n.level+1,most_common_class=max(Counter(leftsplit["type"]), key = Counter(leftsplit["type"]).get)) # < threshold
            self.tree[l_child.id] = l_child
            r_child = Node(parent = current_n, data = rightsplit, gini_val = self._gini_oneside(rightsplit["type"]) ,level = current_n.level+1,most_common_class=max(Counter(rightsplit["type"]), key = Counter(rightsplit["type"]).get)) # > threshold
            self.tree[r_child.id] = r_child
            current_n.create_children(l_child,r_child)
            self._create_tree(l_child,self.tree,data = leftsplit)
            self._create_tree(r_child,self.tree,data = rightsplit)
            
        else: #creates 2 children when not a leaf
            split = self.find_split(data) #(gini_min, threshold, best_feature)
            current_n.gini_val = split[0]
            current_n.threshold = split[1]
            current_n.feature = split[2]
            mask = data[split[2]]>split[1]
            rightsplit = data[mask]
            leftsplit = data[-mask] #check right split on feature contains higher values 
            l_child = Node(parent = current_n, data = leftsplit, gini_val = self._gini_oneside(leftsplit["type"]) ,level = current_n.level+1,most_common_class=max(Counter(leftsplit["type"]), key = Counter(leftsplit["type"]).get)) # < threshold
            self.tree[l_child.id] = l_child
            r_child = Node(parent = current_n, data = rightsplit, gini_val = self._gini_oneside(rightsplit["type"]) ,level = current_n.level+1,most_common_class=max(Counter(rightsplit["type"]), key = Counter(rightsplit["type"]).get)) # > threshold
            self.tree[r_child.id] = r_child
            current_n.create_children(l_child,r_child)
            self._create_tree(l_child,self.tree,data = leftsplit)
            self._create_tree(r_child,self.tree,data = rightsplit)
        return self.tree

    def _gini_oneside(self,data):
        """Takes a list of labels for one side of a 
        split and returns gini index for that side"""
        size = len(data)
        types = set(data)
        represented = Counter(data)
        gini = 1
        for key, value in represented.items():
            gini -= (value/size)**2
        return gini

    def _gini_overall(self,datal,datar):
        lsize = len(datal)
        rsize = len(datar)
        size = lsize+rsize
        return self._gini_oneside(datal)*(lsize/size)+self._gini_oneside(datar)*(rsize/size)
    
    def entropy(self, data):
        size = len(data)
        types = set(data)
        represented = Counter(data)
        entropy = 0
        for key, value in represented.items():
            entropy -= (value/size)*math.log((value/size))
        return entropy
   
    def _entropy_overall(self,datal,datar):
        lsize = len(datal)
        rsize = len(datar)
        size = lsize+rsize
        return self.entropy(datal)*(lsize/size)+self.entropy(datar)*(rsize/size)

    def fit(self,data):
        self.data = data
        Node.next_id = 0
        root = Node(parent=None, level = 0,data=self.data,most_common_class=max(Counter(data["type"]), key = Counter(data["type"]).get))
        self.tree[root.id] = root
        self.tree = self._create_tree(root,self.tree,self.data)
    
    def view(self):
        """
        Returns the tree
        """
        return self.tree
    
    def _split(self):
        #Make the split
        #calculate the threshold, for each child
        #calculate the gini value
        return #return two tuples, contaning: (feature, threshold, gini_val)

    def find_split(self,data):
        results=[]
        gini_min = 1000
        threshold = None
        best_feature= None
        if self.entropy_choice == True:
            for feature in data.loc[:, data.columns != "type"]:
                sl = list(set(data.sort_values(feature)[feature]))         #sort data by feature
                list_PS = [(sl[i+1]+sl[i])/2 for i in range(len(sl)-1)]        #find betweeen values for each pair of values in sorted 
                for PS in list_PS:#itterate through between values instead 
                    mask = train[feature]>PS
                    split = list(data[mask]["type"])
                    antisplit = list(data[-mask]["type"]);
                    entropy = self._entropy_overall(split,antisplit)
                    if entropy < gini_min:
                        gini_min = entropy
                        threshold = PS 
                        best_feature = feature          
        else:
            for feature in data.loc[:, data.columns != "type"]:
                sl = list(set(data.sort_values(feature)[feature]))         #sort data by feature
                list_PS = [(sl[i+1]+sl[i])/2 for i in range(len(sl)-1)]        #find betweeen values for each pair of values in sorted 
                for PS in list_PS:#itterate through between values instead 
                    mask = data[feature]>PS #check what data is here CHECK THIS LATER
                    split = list(data[mask]["type"])
                    antisplit = list(data[-mask]["type"]);
                    gini_val = self._gini_overall(split,antisplit)
                    if gini_val < gini_min:
                        gini_min = gini_val
                        threshold = PS 
                        best_feature = feature

                    results.append([PS, self._gini_overall(split,antisplit),feature])
        return (gini_min, threshold, best_feature)

    def predict(self, data):
        self.index_of_features=dict()
        for i,col in enumerate(data.columns):#we need this dict to index the correct value in _traverse
            self.index_of_features[col]=i
        predictions = []
        for point in data.values:
            leaf_node = self._traverse(self.tree[0],point)
            predictions.append(leaf_node.most_common_class)
        return predictions
        pass
    
    def _traverse(self,current_node,point):
        #move along decision tree until leaf is reached
        if current_node.left_child == None :
            return current_node
        else:
            threshold=current_node.threshold
            feature=current_node.feature 
            if point[self.index_of_features[feature]] >= threshold:
                return self._traverse(current_node.right_child,point)

            else:
                return self._traverse(current_node.left_child,point)

        #if leaf then return leaf
        #else find next node
        return None
        pass

def main()
    pass
if __name__ == "__main__":
    main()