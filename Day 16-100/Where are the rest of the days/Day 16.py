import turtle
import another_module
print(another_module.another_variable)
timy = turtle.Turtle()
timy.color("coral")
print(timy)#OBJECT
timy.forward(100) #method
screen = turtle.Screen() #OBJECT
print(screen.canvheight) #Object Attribute
screen.exitonclick() #Object Method

from prettytable import PrettyTable
#from object import class
table = PrettyTable()
print(table)

table.add_column('Pokemon Name', ['Pikachu', 'squirtle', 'charmander'])
table.add_column('Type', ['Electric', 'water','fire'])
print(table)
table.align = 'l'
print(table)