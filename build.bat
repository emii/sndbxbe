cd "C:\Users\ozomatliopochtli\Workpath\sndbxbe\slidesMD"
python m2d presentationMD_win.md deck.html > C:\Users\ozomatliopochtli\Workpath\sndbxbe\contents\slides\presentation.md
cd "C:\Users\ozomatliopochtli\Workpath\sndbxbe"
pelican -s conf.py
ren C:\Users\ozomatliopochtli\Workpath\sndbxbe\output\theme static
cd "C:\Users\ozomatliopochtli\Workpath\sndbxbe\output"
python -m SimpleHTTPServer

