winter_list = ["December", "January", "February", 12, 1, 2]
spring_list = ["March", "April", "May", 3, 4, 5]
summer_list = ["June", "July", "August", 6, 7, 8]
fall_list = ["September", "October", "November", 9, 10, 11]
i = input("What is the season? ")

def my_season():
    if i in winter_list:
        print "It is Winter"
    elif i in spring_list:
        print "It is Spring"
    elif i in summer_list:
        print "It is Summer"
    elif i in fall_list:
        print "It is Fall"
    else:
        print "It is not a season"

print my_season()

