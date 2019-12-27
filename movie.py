#this will get a movie rateing
# importing the reqsts library 
import requests 

movie_name = input ("give us a movie: ")
print("coming soon data on" + movie_name)
URL ="http://www.omdbapi.com"
PARAMS = {'apikey':"952be5f0","t":movie_name}
r = requests.get(url = URL, params = PARAMS)
data = r.json() 
#print(data) 
year = data ["Year"]
print ("this movie came out on "+year)