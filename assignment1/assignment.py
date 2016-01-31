import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
numberOfPassengers = data.shape[0]

print numberOfPassengers, 'passengers'

isMale = data['Sex'] == 'male'

print data[isMale].count()[0], 'males'

isFemale = data['Sex'] == 'female'

print data[isFemale].count()[0], 'females'

survived = data['Survived'] == 1

print data[survived].count()[0], 'passengers survived'

firstClass = data['Pclass'] == 1

print 'Percentage of passengers survived =', data['Survived'].value_counts()[1] / float(numberOfPassengers)

print 'Percentage of first class passengers =', data[firstClass].count()[1] / float(numberOfPassengers)

print 'Mean Age =', data['Age'].mean(axis=0)

print 'Median Age =', data['Age'].median()

sibSp = data['SibSp']
parch = data['Parch']

print 'Correlation between SibSp and Parch =', sibSp.corr(parch)


femalesNames = data[isFemale]['Name']

name = femalesNames.str.split('Miss.')

containsMiss = femalesNames.str.contains('Miss.')
containsMrs = femalesNames.str.contains('Mrs.')
missDF = femalesNames[containsMiss]
mrsDF = femalesNames[containsMrs]
frames = [mrsDF, missDF]

def findNameMiss(arg):
	components = arg.split('.')
	components = components[1].split(' ')
	return components[1]

def findNameMrs(arg):
	components = arg.split('.')
	components = components[1].split(' ')
	if len(components) > 3:
		return components[2]
	else:
		return components[1]

firstNamesMiss = missDF.apply(findNameMiss)
firstNamesMrs = mrsDF.apply(findNameMrs)
# nameFrequency = firstNames.value_counts()
print 'Most popular female name on titanic is'

# print data[isFemale]['Name'].apply(findFirstName).value_counts()

print pandas.concat([firstNamesMiss, firstNamesMrs]).value_counts()
print data[firstClass]['Sex'].value_counts()
