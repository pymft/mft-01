weight = float(input("weight (kilograms) = "))
height = float(input("height (meters) = "))


# SECTION 2: check validity of params
# if weight < 0 :
#     print("negative value is not valid for weight")
#
# elif height < 0:
#     print("negative value is not valid for height")
#
# elif height > 3:
#     print("c'mon, giraffes do not know how to code!")

if weight < 0 or height < 0 or height > 3:
    print("invalid")
else:
    bmi = weight / (height ** 2)
    print(bmi)

    # SECTION 3:
    if bmi < 18.5:
        print("underweight")
    elif bmi < 24:
        print("normal")
    elif bmi < 29.9:
        print("over-weight")
    else:
        print("obese")


