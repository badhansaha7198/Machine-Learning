import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# Predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3
predictionCO2 = regr.predict([[2300, 1300]])

print(regr.coef_)
print(predictionCO2)


