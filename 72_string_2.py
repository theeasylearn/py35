#create list that has 10 cities names in India
indian_cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad", "Pune", "Jaipur", "Lucknow"]

print("Indian cities:", indian_cities)

#join them into a single string separated by space
indian_cities_string = " ".join(indian_cities)
print("Indian cities as a string:", indian_cities_string)   

netflix_shows = "Stranger Things, Wednesday, Squid Game, Money Heist, Dark, The Witcher, Bridgerton, The Crown, Ozark, You, Narcos, Black Mirror, Lucifer, Sex Education, Elite, Emily in Paris, All of Us Are Dead, Sweet Tooth, The Umbrella Academy, Cobra Kai"
print("Netflix shows:", netflix_shows)
#convert into a list of shows
netflix_shows_list = netflix_shows.split(", ")
print("Netflix shows as a list:", netflix_shows_list)

text = "India is a country where India's diversity, India's culture, India's history, and India's unity are celebrated."
#replace India with Bharat
text_replaced = text.replace("India", "Bharat")
print("Text with India replaced by Bharat:", text_replaced) 