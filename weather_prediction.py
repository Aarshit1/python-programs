weather=(1,0,0,1,0,0,1,1,1)       #sunny=1     #rainy=0
sunny=weather.count(1)
rainy=weather.count(0)

if sunny>rainy:
    print("Good Weather")
else:
    print("Bad Weather")