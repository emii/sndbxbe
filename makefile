ifeq ($(OS),Windows_NT) 

	RM = del /s /q
	FixPath = $(subst /,\,$1)
	AND = &
else

	RM = rm -rf
	FixPath = $1
	AND = ;
endif

CONTENTS= contents/articles
#_CONT_ART= *.md slides/*.md
#CONTENTS = $(patsubst %,$(CONTDIR)/%,$(_CONT))

DRAFTS= contents/drafts
#_CONT_DRFT= *.md slides/*.md
#DRAFTS = $(patsubst %,$(CONTDIR)/%,$(_CONT))

ODIR= output
_OBJ= *.html static/css/style.css

OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
SETTINGS = conf.py

contents:
	pelican -s $(SETTINGS) -o $(ODIR) -r

serve:
	cd $(ODIR) $(AND) python -m SimpleHTTPServer 

push:
	git status
	git add -A
	git commit -m 'update'
	git push

deploy:
	cd $(ODIR)
	git status
	git add -A
	git commit -m 'update'
	git push

clean:
	$(RM) $(call FixPath, $(OBJ))

.PHONY: contents draft serve push clean #not objects