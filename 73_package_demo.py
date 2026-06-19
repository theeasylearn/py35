#import module from package 

# from main-package.sub-package.module import function as aliasname 
from world.asia.country import getCountry as getAsianCountries
from world.europe.country import getCountry as getEuropeanCountries
from world.affrica.country import getCountry as getAfricanCountries

#function to print all asian countries 
print("Asian countries:", getAsianCountries())
print("European countries:", getEuropeanCountries())
print("African countries:", getAfricanCountries())