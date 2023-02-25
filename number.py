class Number:
    def __init__(self, value: int):
        self.value = value


    def get_number(self):
        """
        Returns the number.

        returns: int
        """
        return self.value

    def is_odd(self):
        """
        Returns True if the number is odd, otherwise False.

        returns: bool

        """
        return self.value % 2 == 1

    def is_even(self):
        """
        Returns True if the number is even, otherwise False. 

        returns: bool
        """
        return self.value % 2 == 0

    def is_prime(self):
        """
        Returns True if the number is prime, otherwise False.

        returns: bool
        """
        
        
        
           
    def get_divisors(self):
        """
        Returns a list of all the divisors of the number.

        returns: list
        """
        l = []
        for i in range(1, self.value+1):
            if self.value % i == 0:
                l.append(i)
        
        return l

    def get_length(self):
        """
        Returns the number of digits in the number.

        returns: int
        """
        s=[]
        for i in range(1, self.value):
            s.append(i)
        return len(s)


    def get_sum(self):
        """
        Returns the sum of all the digits in the number.

        returns: int
        """
        s=0
        for i in range(1, self.value):
            s+=i

        return s

    def get_reverse(self):
        """
        Returns the number in reverse.

        returns: int
        """
        s=[]
        for i in range(1, self.value):
            s.append(i)

        return s[::-1]
        

    def is_palindrome(self):
        """
        Returns True if the number is a palindrome, otherwise False.

        returns: bool
        """
       
        o=str(self.value)
        s=o[::-1]
        a=int(s)
        if self.value==a:
            d=True
        else:
            d=False
        return d  
           

    def get_digits(self):
        """
        Returns a list of all the digits in the number.

        returns: list
        """
        s=[]

        s.append()
        return s

    def get_max(self):
        """
        Returns the largest digit in the number.

        returns: int
        """
        s=[]
        for i in range(1, self.value):
            s.append(i)
        return max(s)

    def get_min(self):
        """
        Returns the smallest digit in the number.

        returns: int
        """
        s=[]
        f=self.value%10
        d=self.value/10
        s.append(d)
        s.append(f)
        return min(s)

    def get_average(self):
        """
        Returns the average of all the digits in the number.

        returns: float
        """
        a=0
        s=[]
        for i in range(1, self.value):
            a+=i
            s.append(i)
        d=a//len(s)
        return d
    def get_median(self):
        """
        Returns the median of all the digits in the number.

        returns: float
        """
        pass

    def get_range(self):
        """
         

        returns: list
        """
        pass

    def get_frequency(self):
        """
        Returns a dictionary of the frequency of each digit in the number.

        returns: dict
        """
        pass
    

# Create a new instance of Number
number = Number(5)
# print(number.get_number())
# print(number.is_even())
print(number.get_sum())
