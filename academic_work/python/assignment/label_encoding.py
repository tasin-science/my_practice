from sklearn.preprocessing import LabelEncoder

data = ["cat", "dog", "mouse"]
encoder = LabelEncoder()
numerical_data = encoder.fit_transform(data)
print(numerical_data)