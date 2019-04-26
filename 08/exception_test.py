# test on "yes" or "no"
def is_yes(s):
    if s == "yes":
        return True
    if s == "no":
        return False
    raise Exception("Value must be either 'yes' or 'no'")


try:
    is_yes("zssss")
except Exception as e:
    print("Incorrect value: " + str(e))




