import json 
#for i , module in enumerate(dir( json )):
# if (i % 5):
#    print( module,'\t' ,end='')
#  else:
#    print()
'''  ['JSONDecodeError', 'JSONDecoder', 'JSONEncoder',
'__all__', '__author__', '__builtins__', '__cached__',
'__doc__', '__file__', '__loader__', '__name__', '__package__', 
'__path__', '__spec__', '__version__', '_default_decoder', 
'_default_encoder', 'codecs', 'decoder', 'detect_encoding', 
'dump', 'dumps', 'encoder', 'load', 'loads', 'scanner']
   ^---json.dump()            ^---json.load() 

 '''

"""
json.load(file)     # load from file
json.loads(str)     # load from string
----------------------------------------
json.dump(J,file)   # write to a file
json.dumps(J)       # write as a string
"""
# movies.json :
# https://gist.github.com/saniyusuf/406b843afdfb9c6a86e25753fe2761f4  
json_file = open("./Sample_Files/movies.json" ,'r' ,encoding='utf-8')
movies = json.load(json_file)
json_file.close()

# print( movies )   
""" [{'Title': 'Avatar', 'Year': '2009', 'Rated': 'PG-13', 
'Released': '18 Dec 2009', 'Runtime': '162 min', 
'Genre': 'Action, Adventure, Fantasy', 'Director': 
'James Cameron', 'Writer': 'James Cameron', 
'Actors': 'Sam Worthington, Zoe Saldana, Sigourney Weaver, 
Stephen Lang', 'Plot':  .......  


ARRAY OF MOVIES []---->    key   values
movie = dictionary         str : [ "str","str", ... ]
"""
print( type( movies ))        # < class 'dict' >
print( movies[0]["Genre"])    # Action, Adventure, Fantasy,...

for i,mov in  enumerate( movies):# SHOW  EVERY  MOVIE[]
  if (i % 5):                 # index only used to print separated lines 
    print(  mov["Title"] ,"\t", end='')  # we change defaults   end='\n'
  else:
    print()      # separation when i is multiple of 5 ( colums of 4 )
''' I Am Legend   300          The Avengers      The Wolf of Wall Street
Game of Thrones   Vikings      Gotham  Power     Breaking Bad
Doctor Strange   Rogue One: A Star Wars Story    Assassin's Creed  '''

# PRINT FIELDS : Title Year Rated  Released
print( key_list := movies[0].keys() )
print(type(key_list))  # MUST CHANGE KEYS TO LIST
print( key_list := list(movies[0].keys()) )

# PRINT FIRST EVERY TITLE :
for movie in movies:
  print(  movie[ key_list[0] ]) 


# Print the first key from each movie
for movie in movies:
    print(movie[key_list[0]])

# DELETE IMAGES

for movie in  movies:  # movies[i] = movie ={title:"" , genere:""}
  movie_keys = movie.keys()
  if (  "Images" in movie_keys ): 
    print(movie_keys )
    movie.pop("Images") # ERRASE EVERY IMAGE

first_movie = open("./Sample_Files/first_movie.json" ,'w' ,encoding='utf-8')
json.dump( movies[0] , first_movie , indent=4 )
first_movie.close()

noImg       = open("./Sample_Files/movies_noImg.json" ,'w' ,encoding='utf-8')
json.dump( movies    , noImg       , indent=4 )
noImg.close()
