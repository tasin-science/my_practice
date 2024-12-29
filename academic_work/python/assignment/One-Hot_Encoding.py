from sklearn.preprocessing import OneHotEncoder

data = [["cat"], ["dog"], ["mouse"]]
encoder = OneHotEncoder()
numerical_data = encoder.fit_transform(data).toarray()
print(numerical_data)