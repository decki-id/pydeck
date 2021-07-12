# import re
import sys
# from Question import Question

# MULTIPLE CHOICE QUIZ
# question_prompts = [
#     "\nWhat color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
#     "\nWhat color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
#     "\nWhat color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
# ]
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")
# run_test(questions)


# CLASS ORIGIN
# class Jets:
#     def __init__(self, name, country):
#         self.name = name
#         self.origin = country
# first_item = Jets("F16", "USA")
# a=first_item.name
# b=first_item.origin
# print(a,b)


# JOIN
# lst=["Hawaii", "Phuket", "Aruba", "Keys"]
# joined=", ".join(lst)
# print(joined)


# NESTED DATA
# nested_lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
# ans_1=nested_lst[2]["violet"]
# print(ans_1)


# NAZI LOGO WITH LOOP
# value = [1, 2, 3, 4, 5]
# totalLength = (len(value) * 2) - 1
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for x in value:
#     if x == 1:
#         for a in number:
#             if a <= len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a < totalLength:
#                 sys.stdout.write(" ")
#             elif a == totalLength:
#                 sys.stdout.write("#")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a < totalLength:
#                 sys.stdout.write(" ")
#             elif a == totalLength:
#                 sys.stdout.write("#")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a < totalLength:
#                 sys.stdout.write(" ")
#             elif a == totalLength:
#                 sys.stdout.write("#")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a < totalLength:
#                 sys.stdout.write(" ")
#             elif a == totalLength:
#                 sys.stdout.write("#")
# sys.stdout.write("\n")
# for x in number:
#     sys.stdout.write("#")
#     sys.stdout.flush()
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a == 1:
#                 sys.stdout.write("#")
#             elif a > 1 and a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a <= totalLength:
#                 sys.stdout.write(" ")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a == 1:
#                 sys.stdout.write("#")
#             elif a > 1 and a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a <= totalLength:
#                 sys.stdout.write(" ")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a == 1:
#                 sys.stdout.write("#")
#             elif a > 1 and a < len(value):
#                 sys.stdout.write(" ")
#             elif a == len(value):
#                 sys.stdout.write("#")
#             elif a > len(value) and a <= totalLength:
#                 sys.stdout.write(" ")
# sys.stdout.write("\n")
# for x in value:
#     if x == 1:
#         for a in number:
#             if a == 1:
#                 sys.stdout.write("#")
#             elif a < len(value):
#                 sys.stdout.write(" ")
#             elif a >= len(value) and a <= totalLength:
#                 sys.stdout.write("#")
#                 sys.stdout.flush()


# BASIC CALCULATOR
# num1 = input("Enter a number: ")
# factor = input("Enter the factor: ")
# num2 = input("Enter another number: ")
# if factor == "+":
#     result = float(num1) + float(num2)
#     print(result)
# elif factor == "-":
#     result = float(num1) - float(num2)
#     print(result)
# elif factor == "*":
#     result = float(num1) * float(num2)
#     print(result)
# elif factor == "/":
#     result = float(num1) / float(num2)
#     print(result)
# else:
#     print("The factor is undefined.")


# BASIC FIBONACCI FROM GOOGLE
# nterms = int(input("Insert terms long: "))
# n1, n2 = 0, 1
# num = 1
# if (nterms == 1):
#     print(n1)
# else:
#     while (num <= nterms):
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         num += 1


# BASIC FIBONACCI BY MYSELF
# n1 = int(input("Insert first parameter: "))
# n2 = int(input("Insert last parameter: "))
# n3 = 1
# while (n1 <= n2):
#     print(n1)
#     nth = n1 + n3
#     n1 = n3
#     n3 = nth