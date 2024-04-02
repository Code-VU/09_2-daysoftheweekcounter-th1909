def countDayOfTheWeek():
    file_name = input("Enter a file name: ")
    fhand = open(file_name)

    day_list = []
    dictionary = {}

    for line in fhand:
        if line.startswith('From') and not line.startswith('From:'):
            words = line.split()
            day_list.append(words[2])
    
    for day in day_list:
        dictionary[day] = dictionary.get(day, 0) + 1
        

    print(dictionary)
            



## if you want to test locally run > python payCalculator.py
if __name__ == "__main__":
    countDayOfTheWeek()
