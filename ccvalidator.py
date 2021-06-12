class CheckCreditCard:
    def __init__(self, card_number, card_type = "", is_valid = True):
        self.card_number = card_number
        self.card_type = card_type
        self.is_valid = is_valid

    def determine_card_type(self):
        self.card_number = str(self.card_number)

        if self.card_number[0:1] == '4': 
        	self.card_type = 'Visa' 
        elif self.card_number[0:2] in ('51', '52', '53', '54', '55'):
        	self.card_type = 'Master Card' 
        elif self.card_number[0:2] in ('34', '37'):
        	self.card_type = 'AMEX' 
        elif self.card_number[0:4] == '6011':
        	self.card_type = 'Discover' 
        else:
        	self.is_valid = False
        print(self.card_number, self.card_type, self.is_valid)
        return self.card_type

    def check_length(self):
        self.card_number = str(self.card_number)
        if self.determine_card_type() == 'AMEX':
        	length = 15
        else:
        	length = 16

        print("Expected Card Length :", length)

        if len(self.card_number) == length:
            self.is_valid = True
            return self.is_valid
        else:
            self.is_valid = False
            return self.is_valid

    # 1. From the second rightmost digit,
    # double the value of every other digit.
    def validate(self):
        self.card_number = str(self.card_number)
        doubled_values = []
        print(self.card_number)

        for i in range(len(self.card_number)-1, -1, -1):
            int_num = int(self.card_number[i])
            if i % 2 == 0 and self.card_type != "AMEX":
                doubled_values.append(int_num * 2)
            elif i % 2 != 0 and self.card_type == "AMEX":
                doubled_values.append(int_num * 2)
            else:
                doubled_values.append(int_num)
        print(doubled_values)

        sum = ""
        numerical_sum = 0
        for value in doubled_values:
        	value = int(value)
        	sum = sum + str(value)
        for digit in sum:
        	numerical_sum = int(digit) + numerical_sum
        print(numerical_sum)

        if numerical_sum % 10 == 0:
            self.is_valid = True
            return self.is_valid
        else:
            self.is_valid = False
            return self.is_valid

my_card = CheckCreditCard(4485040993287617)

print(my_card.determine_card_type())
print(my_card.check_length())
print(my_card.validate())