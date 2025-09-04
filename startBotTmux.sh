#!/bin/bash  
SESSION_NAME="botDev_session"
# Проверить, существует ли сеанс уже, если да то убиваем его и запускаем снова
if tmux has-session -t $SESSION_NAME 2>/dev/null; then  
    echo "Session $SESSION_NAME already exists."
    tmux kill-session -t $SESSION_NAME
     # Создать новый сеанс и назвать его
    tmux new-session -d -s $SESSION_NAME
    # Отправить команду по запуску питон файла с ботом в сеанс
    tmux send-keys -t $SESSION_NAME 'echo "python3 bot.py"' C-m
    # Присоединиться к созданному сеансу
#    tmux attach-session -t $SESSION_NAME
else  
    # Создать новый сеанс и назвать его  
    tmux new-session -d -s $SESSION_NAME
    # Отправить команду по запуску питон файла с ботом в сеанс
    tmux send-keys -t $SESSION_NAME 'echo "python3 bot.py"' C-m
    # Присоединиться к созданному сеансу  
#    tmux attach-session -t $SESSION_NAME
fi  
