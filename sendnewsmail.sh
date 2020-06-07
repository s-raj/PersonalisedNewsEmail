python3 ~/Documents/Myjobs/news/news.py > ~/mnt/gdrive/news.txt
echo "Subject: Sharat's Top News Headlines " > ~/mnt/gdrive/subject.txt
cat ~/mnt/gdrive/subject.txt  ~/mnt/gdrive/news.txt |msmtp --from=default -t youremail@gmail.com
