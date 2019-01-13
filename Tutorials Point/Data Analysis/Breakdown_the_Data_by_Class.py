import pandas
data = ("pima_indians.csv")
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','weight in kg','Diabetes pedigree','Age','Outcome']
dataset = pandas.read_csv(data, names=names)


print(dataset.shape)


print(dataset.groupby('Outcome').size())
