capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

# nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
# print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D", "E"], ["F", "G", "H"]]
#print "D"
print(nested_list[2][1])
#print "F"
print(nested_list[3][0])

travel_log2 = {
    "France": {
        "num_times": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "num_times": 2,
    }
}

#print "Stuttgart"
print(travel_log2["Germany"]["cities_visited"][0])