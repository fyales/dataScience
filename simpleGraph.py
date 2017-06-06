from matplotlib import pyplot as plt

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1074.0,2423.4,3013.5,5014.5,7434.4]

plt.plot(years,gdp,color='green',marker='o',linestyle = 'solid')
plt.title("GDP")
plt.ylabel("billion dollars")
plt.show()

movies = ['Annie Hall','Ben-Hur','Gasablanca','Gandhi','West Side Story']
num_oscars = [5,11,3,8,10]
xs = [i + 0.1 for i,_ in enumerate(movies)]
plt.bar(xs,num_oscars)
plt.ylabel('Oscar num')
plt.title('My Favourite Movie')
plt.show()