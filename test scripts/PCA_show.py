#Remove imports, if redundant.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def show_me_pca(vector, labels, is_pairs=False):
    '''Plot PCA for the two classes. Input is one long vector/list, it creates pairs itself.
    If you already created pairs, use is_pairs=True
    Example: if vector is distance between pairs, do not set is_pairs to True. 
    (as it is one vector describing both documents.)
    
    labels is simply a vector with the labels, which will be used to colour the scatter plot.'''
    
    #Convert labels to np.array (might be a list.)
    labels = np.array(labels)
    
    #Join pairs into one, long vector if necessary. 
    if not is_pairs:
        vector = [np.hstack([vector[x],vector[x+1]]) for x in range(0,len(vector),2)]  
    
    #GEt that PCA
    pca = PCA(n_components=2)
    pcs = pca.fit_transform(vector)
    
    #Printing pcs shape - remember they might be halved, due to pairing. 
    print(pcs.shape)
    
    #Group PC's into two, according to label indices. 
    group1 = pcs[labels==0]
    group2 = pcs[labels==1]
    
    #Plot that shit!
    plt.scatter(group1[:,0], group1[:,1], s=5)
    plt.scatter(group2[:,0], group2[:,1], s=5)

#Example input:
#show_me_pca(tfidf_arr[:400], labels[:200])
#half the amount of labels! - data is not concatenated in pairs.

#show_me_pca(cosine_sim[:200], labels[:200], is_pairs=True)
#Equal number of labels and vectors - data is a single vector per pair.
