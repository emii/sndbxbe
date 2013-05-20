source /home/$USER/sndbxbe/bin/activate
cd /home/$USER/sndbxbe/sndbxbe/slidesMD
#rm -rf /home/$USER/sndbxbe/sndbxbe/output
python /home/$USER/sndbxbe/sndbxbe/slidesMD/m2d /home/$USER/sndbxbe/sndbxbe/slidesMD/presentationMD.md /home/$USER/sndbxbe/sndbxbe/slidesMD/deck.html > /home/$USER/sndbxbe/sndbxbe/contents/slides/presentation.md
cd /home/$USER/sndbxbe/sndbxbe/
pelican -s "conf.py"
cd /home/$USER/sndbxbe/sndbxbe/output/ 
mv theme/ static/
python -m SimpleHTTPServer
