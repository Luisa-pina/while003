
def get_data():
    my_file = open('nationsPop.txt', 'r')
    lines = my_file.readlines()
    country_data = []
    for country_line in lines:
        country_line = country_line.strip()
        nation_pop_list = country_line.split(',')
        pop_dictionary = {'Name': nation_pop_list[0],
                          'pop': int(nation_pop_list[1]),
                          'change': float(nation_pop_list[2])
                          }
        country_data.append(pop_dictionary)
    return country_data

def print_menu():
    print("========Please select from the following=========")
    print("[1] Find the largest country")
    print("[2] Find the smallest country")
    print("[3] Add a new country")
    print("[4] Quit")
    print("=================================================")

def main():
    country_list = get_data()
    while True:
        print_menu()
        user_choice = input("Please enter the number of your selection:")

main()