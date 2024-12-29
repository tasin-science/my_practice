from sklearn.preprocessing import OrdinalEncoder

data = [["low"], ["medium"], ["high"]]
encoder = OrdinalEncoder()
numerical_data = encoder.fit_transform(data)
print(numerical_data)
