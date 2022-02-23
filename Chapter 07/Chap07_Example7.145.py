from random import choice
from time import time

my_names = ['Suman','Mohan','Divya','Sugandh']
my_subjects = ['Chemistry','Biology','Maths']

def my_list(num_students):
      mylist = []
      for loop in range(num_students):
            mystudents = {
                  'myid':loop,
                  'myname': choice(my_names),
                  'mysubject':choice(my_subjects)
                  }
            mylist.append(mystudents)
      return mylist

def my_generator(num_students):
      for loop in range(num_students):
            mystudents = {
                  'myid':loop,
                  'myname': choice(my_names),
                  'mysubject':choice(my_subjects) 
                  }
            yield mystudents
            
myt1 = time()
people = my_list(1000000)
myt2 = time()
print('Time taken by list', myt2 - myt1)

myt1 = time()
people = my_generator(1000000)
myt2 = time()
print('Time taken by generator function', myt2 - myt1)