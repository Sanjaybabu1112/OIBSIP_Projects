def get_input():
    while True:
        try:
            height = float(input("Enter your weight in kg: "))
            weight = float(input("Enter your heigth in mtrs: "))
            if weight>0 and height>0:
                return height, weight
            else:
                print("Please enter positive values for height and weight! ")
        except ValueError:
            print("Invalid input. Please enter valid numerical values! ")


def cal_bmi(height, weight):
    bmi = weight/(height**2)

    if bmi<=18.5:
        return bmi, "Under Weight"
    
    if 18.5<=bmi<25:
        return bmi, "Normal Weight"
    
    if 25<=bmi<30:
        return bmi, "Over Weight"
    
    else:
        return bmi, "Obese"
    
def main():
    print("Welcome to the BMI Calculator! \n")

    height, weight =get_input()
    bmi, category =cal_bmi(height, weight)

    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__=="__main__":
    main()