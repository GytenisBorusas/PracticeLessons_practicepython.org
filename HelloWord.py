# def main():
#     print("Hello World!")
#
# if  __name__ == "__main__":
#     main()
#
# print(1 *"\n")
# print("Hello and welcome to Guru99")

# Declare a variable and initialize it
f = 101
print(f)

# Global vs. Local variables in functions
def someFunction():
    # global f
    f = 'I am learning Python'
    print(f)

someFunction()
print(f)



