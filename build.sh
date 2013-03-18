cd /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/
rm -rf output
python /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/slidesMD/m2d /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/slidesMD/presentationMD.md /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/slidesMD/deck.html > /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/contents/slides/presentation.md
pelican -s "conf.py"
cd /Users/e.rangel/Documents/workpath/sndbxbe/www-sndbxbe/output/
mv theme/ static/
python -m SimpleHTTPServer

