# I wrote and debugged this code with all the convoluted "int" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

def Eating(input_var):
    return str(int(input_var)*input_geteilt_drei)

def EAt(input_var, eats):
    print(input_var, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < len(input_var) and eat2 < len(eats):
        if eateat%input_geteilt_drei == input_geteilt_drei_minus_eins//input_geteilt_drei_plus_eins:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += input_var[eat1]
            eat1 += 1
        eateat += 1
    return eAt

def aten(input_var):
    return input_var[::input_geteilt_drei-input_geteilt_drei_plus_eins]

def eaT(input_var):
    return Eating(input_var[:input_geteilt_drei]) + aten(input_var)

def Ate(input_var):
    return "Eat" + str(len(input_var)) + input_var[:input_geteilt_drei]

def main(input_var):
    if len(input_var) == 9:
        if str.isdigit(input_var[:input_geteilt_drei]) and\
            str.isdigit(input_var[len(input_var)-input_geteilt_drei+1:]):
                eateat = EAt(eaT(input_var), Ate(aten(input_var)))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + input_var
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")

print("what's the answer")
input_var = input()
input_geteilt_drei = len(input_var)//3
input_geteilt_drei_plus_eins = input_geteilt_drei+1
input_geteilt_drei_minus_eins = input_geteilt_drei-1
main(input_var)
