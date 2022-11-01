my_file = open('nationsPop.txt', 'r')
lines = my_file.readlines()
country_data = []
for country_line in lines:
    country_line = country_line.strip()
    nation_pop_list = country_line.split(',')
    pop_dictionary = {'Name':nation_pop_list[0],
                      'pop':int(nation_pop_list[1]),
                      'change':float(nation_pop_list[2])
                      }
    country_data.append(pop_dictionary)

while True:
    print("========Please select from the following=========")
    print("[1] Find the largest country")
    print("[2] Find the smallest country")
    print("[3] Add a new country")
    print("[4] Quit")
    print("=================================================")
    user_choice = input("Please enter the number of your selection:")
    if user_choice == '1':
        largest_so_far = country_data[0]
        for current_country in country_data:
            if current_country['pop'] > largest_so_far['pop']:
                largest_so_far = current_country
        print("+++++++++++++++++")
        print(f"The largest country is {largest_so_far['Name']} with population {largest_so_far['pop']}")
    elif user_choice == '2':
        smallest_so_far = country_data[0]
        for current_country in country_data:
            if current_country['pop'] < smallest_so_far['pop']:
                smallest_so_far = current_country
        print("--------------")
        print(f"the smallest country is {smallest_so_far['Name']}")
        print("----------------")
    elif user_choice == '3':
        new_name = input("What is the country name:")
        new_pop = int(input(f"What is {new_name}'s population"))
        new_change = float(input(f"What was the pop change for {new_name} for 2021-2022"))
        new_data = {
            'Name':new_name,
            'pop':new_pop,
            'change':new_change
        }
        country_data.append(new_data)
    elif user_choice == '4':
        exit(0)
    else:
        print("Please select 1-4")
