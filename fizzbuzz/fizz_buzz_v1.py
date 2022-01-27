FizzBuzz
# https://leetcode.com/problems/fizz-buzz/

# Runtime 78 ms	Memory: 15.1 MB
class Solution1:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(str(i))
        return fizz_list


# Runtime 47 ms	Memory: 15 MB
class Solution2:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            if i % 15 == 0: #if i % 3 == 0 and i % 5 == 0:
                fizz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_list.append("Fizz")
            elif i % 5 == 0:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(str(i))
        return fizz_list


# Runtime 58 ms	Mempry: 15.1 MB
class Solution3:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            element = ""
            if i % 3 == 0:
                element += "Fizz"
            if i % 5 == 0:
                element += "Buzz"
            if not element:
                element = str(i)
            fizz_list.append(element)
        return fizz_list



# Runtime 60 ms	Memory: 15 MB
class Solution4:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    fizz_list.append("FizzBuzz")
                else:
                    fizz_list.append("Fizz")
            elif  i % 5 == 0:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(str(i))
        return fizz_list

