def apply_hashing_trick(feature_dict,vector_size=2000):
    # create an array of zeros of length 'vector_size'
    new_features = [0 for x in range(vector_size)]

    # iterate over every feature in the feature dictionarye
    for key in feature_dict: 

        # get the index into the new feature array
        array_index = hash(key) % vector_size

        # add the value of the feature to the new feature array
        # at the index we got using the hashing trick
        new_features[array_index] += feature_dict[key]

    return new_features



