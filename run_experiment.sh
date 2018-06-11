#!/bin/zsh
#Usage: ./run_experiment.sh go.sh
#where go.sh is the script that runs your experiment 

#ask why you're running this experiment
prompt1='EXPERIMENT NAME: '
echo $prompt1
read response1

prompt2='WHY ARE YOU RUNNING THIS EXPERIMENT?'
echo $prompt2
read response2

prompt3='NEXT STEPS?'
echo $prompt3
read response3

#make log file 
START=`date '+%m-%d-%H:%M'`
log="${response1}_${START}.log"
email="${response1}_${START}.email"
touch $log $email 
echo "log_file=${log}"
echo "log_file=${log}" >> $log 

#add reponses 
echo $prompt1 >> $log
echo $response1 >> $log
echo "" >> $log 
echo $prompt2 >> $log
echo $response2 >> $log
echo "" >> $log 
echo $prompt3 >> $log
echo $response3 >> $log
echo "" >> $log 

echo "start=${START}" >> $log  

#input is the shell script that will be the long-running experiment you want to run 
script="$1"
echo "script=${script}" >> $log 

#add TMUX session to log file
TMUX=`tmux display-message -p '#S'`
echo "tmux=${TMUX}" >> $log
echo "" >> $log 

cp $log $email 

#then run the actual script 
#-maybe something about adding the path from the current directory
./${script} &>> $log 

#end time
echo "" >> $log  
END=`date '+%m-%d-%H:%M'`
echo "end=${END}" >> $log
echo "end=${END}" >> $email 
echo ''
echo 'RESULTS?:'

#send an email to yourself when the experiment is done running
mail -s "EXPERIMENT COMPLETE: ${response1}" kkeith@cs.umass.edu < $email 
rm $email 
#mail -s "EXPERIMENT COMPLETE: ${response1}" kkeith@cs.umass.edu < /home/kkeith/expr_utils/email_blank.txt