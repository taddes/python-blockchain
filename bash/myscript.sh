#!/bin/bash
declare -i number1
declare -i number2
declare -i total
echo "What is your favorite number?"
  read number1
echo "What number do you hate?"
  read number2
total=$number1*$number2 
  echo "AHA! They equal " $total
exit 0
