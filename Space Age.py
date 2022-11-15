# Space Age

def space_age(person_age_seconds):

    person_age_seconds = float(input("Please enter your age in seconds: "))

    planet_age_dict = {"Mercury":0.2408467,
                       "Venus":0.61519726,
                       "Earth":1.0,
                       "Mars":1.8808158,
                       "Jupiter":11.862615,
                       "Saturn":29.447498,
                       "Uranus":84.016846,
                       "Neptune":164.79132
                       }

    for x,y in planet_age_dict.items():
        print("Your age on " + str(x) + " is " + str((person_age_seconds * y)/float(31557600)) +
              " Earth Years")
