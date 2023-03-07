room 1:

The commands used:
find . -name "*.txt" -type f -exec rm -rf {} \;

second command ll -SS -la

the password is "WHATSUPMAN" => in lower case: whatsupman

room 2:

cat /etc/passwd | grep "white_rabbit" | awk -F: '{print $1,$3}'
 white_rabbit =>521

cat users_list | grep -oE "521+\.[0-9]+\.[0-9]+\.[0-9]+"

521.155.111.106
 cat users_list | grep "521.155.111.106" | cut -d "," -f 2-3
 jackie,Ekkel

 find ./Logs/ -type f | while read f; do cat $f | grep 'jackie' | sort; done

 password 472

room 3:

cat song | grep -w  "do" |wc -l
result 12
cat ./song | awk '!/home/ {print $0}' | wc -l
cat song | grep -v  "home" | wc -l
result 39

cat song  | sed '/^\s*$/d' | wc -l
result =32

/ No No! I am hungry, I Dont see any \
\ 'food' files around! give me food! /
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
bash creature.sh food
sudo groupadd vegan
sudo chgrp  vegan food
bash creature.sh food

/ OOOM NOM NOM...                       \
|                                       |
\ The pass to open the chest is 1195723 /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

room 4

sed 's/bla/i/g' && sed 's/blu/h/g' && s/zing/h/g'
hey there this is some crazy line to make some dummy content!
This is just a line like above
The real text is just on the next line!
Sorry another dummy line
Now we are getting serious:
The password for the key is linuxisstillfun
yeeey
password crazyroom

Room 5
sudo apt install default-jre
java -jar PhoenixFire.jar 
i dont understand!
java -jar PhoenixFire.jar fire
Creating Fire!!!
Check new files!

password fireofthephoenix
cat fire.txt 
The password to the next room is: fireofthephoenixescape@0d0951835d1a:~/escapeRoom/room_5$ 

room 6

sudo touch check.txt
sudo chmod 777 check.txt
 script: for i in {1..100} 
do
    if [[ $(($i%7)) -eq 0 ]]
        then
            echo "7" >>check.txt
    else
        echo "$i" >>check.txt
    fi
done
java -jar game7boom.jar 
Check compleete! The password is : 'jumanji'
jumanji => vi key => linuxpro
:

room 7

cat table.csv | cut -d',' -f4 | grep '\.png$' | sort | sed 's/junk[0-9]*//g; s/[0-9]*\.png//g' | tr ' ' '\n' > magic
java -jar magic.jar magic
The pass to next room is: linuxmagic
room 8
touch boogiewoogie
#!/bin/bash
for (( i=1; i<=$1; i++ ))
do
  echo "I like to boogiewoogie every day!"
done
sudo chmod 777 boogiewoogie

cp boogiewoogie /bin

java -jar BlackBox.jar 
Hey! Lets have some fun! Lets create a new command called 'boogiewoogie'!
The command will take only 1 argument - a number N, and print "I like to boogiewoogie every day!" N times, each on separate line!
I will try it now...!
Running the command: "boogiewoogie 3"...
Command output:
Exit value: 0
I like to boogiewoogie every day!
I like to boogiewoogie every day!
I like to boogiewoogie every day!
Good job!
The pass to open the chest is 'shutupanddance'

room 9:

very Good!
Question 2: parameter in 'cd' command which takes you to the previous working directory you have been? (1 char)
Your abswer:
.
wrong answer, try again...
Question: parameter in 'cd' command which takes you to the previous working directory you have been? (1 char)
~
wrong answer, try again...
Question: parameter in 'cd' command which takes you to the previous working directory you have been? (1 char)
/
wrong answer, try again...
Question: parameter in 'cd' command which takes you to the previous working directory you have been? (1 char)
-
very Good!
Question 3:  which  symbol tell the shell to append to file? (2 chars)
Your abswer:
>>
very Good!
Question 4: One of the shell commands you use to show actual command behind the alias (4 chars)
Your abswer:
file
wrong answer, try again...
Question: One of the shell commands you use to show actual command behind the alias (4 chars)
type
very Good!
Question 5:  'cd' to home directory symbol (1 char)
Your abswer:
~
very Good!
Question 6:  alias of 'ls -alF'? (2 chars)
Your abswer:
ll
very Good!
Question 7: command to keep listing the currently running processes, sorted by cpu usage (3 chars)
Your abswer:
top
very Good!
Question 8:  on command line,while executing multiple commands, symbol which make sure that the next command will only run when the previous command was successful (2 chars)
Your abswer:
$?
wrong answer, try again...
Question:  on command line,while executing multiple commands, symbol which make sure that the next command will only run when the previous command was successful (2 chars)
&&
very Good!
Question 9:  commonly used command to print only first N lines of a file (4 chars)
Your abswer:
head
very Good!
Question 10:  on cmd, Reuse the previous command in present command shortcut(2 chars)
Your abswer:
!!
very Good!
Question 11:  convert '546' numeric permission convention to letters(r-xw...) (9 chars)
Your abswer:
r-xr--rw-
very Good!
Question 12: Displays the file system disk space usage (2 chars)
Your abswer:
df
very Good!
Question 13: name of file which is used to keep track of every registered user that has access to the system (6 chars)
Your abswer:
/etc/passwd
wrong answer, try again...
Question: name of file which is used to keep track of every registered user that has access to the system (6 chars)
passwd
very Good!
Question 14: operating system command to read files, which doesn?t need to load the full file while opening and allow to scroll up and down on the content.(4 chars)
Your abswer:
less
very Good!
Question 15: command to edit the sudoers file (6 chars)
Your abswer:
visudo
very Good!
Question 16:  partition reserved for the installation of add-on application software packages (3 chars)
Your abswer:
opt
very Good!
Congrats! you finished the trivia challenge! 
The key to the treasure chest is 'geniuslinuxuser'!

room 10:

inuxTrivia.jar  README  treasureChest
escape@0d0951835d1a:~/escapeRoom/room_9$  vi treasureChest 


_   __             __ _       _     _              _   _   _
\ \ / /__  _   _   / _(_)_ __ (_)___| |__   ___  __| | | |_| |__   ___
 \ V / _ \| | | | | |_| | '_ \| / __| '_ \ / _ \/ _` | | __| '_ \ / _ \
  | | (_) | |_| | |  _| | | | | \__ \ | | |  __/ (_| | | |_| | | |  __/
  |_|\___/ \__,_| |_| |_|_| |_|_|___/_| |_|\___|\__,_|  \__|_| |_|\___|

                                                            _
  ___  ___  ___ __ _ _ __   ___   _ __ ___   ___  _ __ ___ | |
 / _ \/ __|/ __/ _` | '_ \ / _ \ | '__/ _ \ / _ \| '_ ` _ \| |
|  __/\__ \ (_| (_| | |_) |  __/ | | | (_) | (_) | | | | | |_|
 \___||___/\___\__,_| .__/ \___| |_|  \___/ \___/|_| |_| |_(_)
                    |_|
  ____                             _         _       _   _                 _
 / ___| ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |
| |  _ / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
| |_| | (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
 \____|\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                   |___/


