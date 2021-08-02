#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:18:34 2021

@author: saka
"""
print("This is a arithmetic_arranger Project created by SURAJ SAKA")
def arithmetic_arranger(problems, solve = False):
  
  firstnumber=""
  operator=""
  secondnumber=""
  firstline=""
  secondline=""
  thirdline=""
  fourthline=""



  if len(problems)>5:
    return("Error: Too many problems.")

  for problem in problems:
    problem.strip()
    firstnumber=problem.split(" ")[0]
    operator=problem.split(" ")[1]
    secondnumber=problem.split(" ")[2]
    

    if len(firstnumber)>4 or len(secondnumber)>4:
      return("Error: Numbers cannot be more than four digits.")
    
    try:
      if operator=="+":
        sum=int(firstnumber)+int(secondnumber)
      elif operator=="-":
        sum=int(firstnumber)-int(secondnumber)
      else:
        return("Error: Operator must be '+' or '-'.")
    except:
      return("Error: Numbers must only contain digits.")

    length=max(len(firstnumber),len(secondnumber))
    top=""
    middle=""
    below=""
    sumline=""
    top=firstnumber.rjust(length+2)
    middle=operator+secondnumber.rjust(length+1)
    lines=""
    for x in range(length+2):
      lines+="-"
    
    below=lines
    sumline=str(sum).rjust(length+2)

    if problem !=problems[-1]:
      firstline+=top+"    "
      secondline+=middle+"    "
      thirdline+=below+"    "
      fourthline+=sumline+"    "
    else:
      firstline+=top
      secondline+=middle
      thirdline+=below
      fourthline+=sumline



  if solve:
    return (firstline+"\n"+secondline+"\n"+thirdline+"\n"+fourthline)
  else:
    return (firstline+"\n"+secondline+"\n"+thirdline)

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))