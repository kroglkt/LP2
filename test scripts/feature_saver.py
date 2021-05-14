import pickle

def save_features(feature_dict):
    '''Save the updated feature dictionary. Takes dictionary as input and saves as binary file
    
    example: 
    >>> my_featues = {'freqdist': [1,6,3,5]}
    >>> save_features(my_features)'''
    
    with open('data/features.dat', 'wb') as file:
        pickle.dump(feature_dict, file)
    print("Features saved! :-)")

def load_features():
    '''Load feature dictionary. Returns the saved feature as a dictionary.
    Will then print all the available features.
    
    example: 
    >>> my_features = load_features()'''
    
    with open('data/features.dat', 'rb') as file:
        feats = pickle.load(file)
    print("Features available:")
    for i in feats.keys():
        print(i)
