from random import choice

user = input("Enter an anime ").title()

result = {'Supernatural' : ['Blue exorcist', "Jojo's Bizarre Adventure"],
          
'Action':["One Punch Man","Demon Slayer","Vinland Saga","Baki","Baki Hanma","Full Metal alchemist:brotherhood","Yasuke","Dragon Ball Z","Dragon Ball Super"],

'Adventure':["My hero academia "," Black Clover","Naruto","Cowboy Bebop"],

'Sci-fi':["Attack on Titan","Assasination Classroom","Parasyte"],

'Fantasy':["Jujustsu Kaisen","Hunter x Hunter","Devilman Crybaby"],

'Comedy':["Komi Can't Communicate"],

'Drama':["Food Wars","The Disastrous Life of Saiki K"],

'Psychological':["Code Geass","Mob Pyscho","Death Note"],

'Horror':["Castlevania","Record of Ragnarok"]



}
print(choice(result[user]))
 



   


