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

#prove that it worked
for nation in country_data:
    print(nation)
