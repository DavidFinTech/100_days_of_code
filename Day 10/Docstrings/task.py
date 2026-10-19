#def format_name(f_name, l_name):
    #formated_f_name = f_name.title()
    #formated_l_name = l_name.title()
    #return f"{formated_f_name} {formated_l_name}"


#formatted_name = format_name("AnGeLa", "YU")

#length = len(formatted_name)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            leap_year = True
        else:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
    else:
        leap_year = False

    print(leap_year)


is_leap_year(2024)



