#!/bin/bash
VALUE=$(($RANDOM % 10+1))
echo $VALUE

echo "Guess the number between 1 and 10"

TURN=0
GUESS=0

while (($TURN < 3))
  do
    read GUESS

    if [ $GUESS < $VALUE ]; then
       echo "Too low, try again..."
       ((TURN++))
    fi 


    if [ $GUESS > $VALUE ]; then
       echo "Too high, try again..."
       ((TURN++))
    fi


    if [ $GUESS = $VALUE ]; then
       echo "You win!"
       TURN=3
    fi
  done   

