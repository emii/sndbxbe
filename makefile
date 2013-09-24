ifeq ($(OS),Windows_NT)

	RM = del /s /q
	FixPath = $(subst /,\,$1)
	SEP = &
else

	RM = rm -rf
	FixPath = $1
	SEP = ;
endif

CONTDIR= contents/articles
_CONT= *.md slides/*.md
CONTENTS = $(patsubst %,$(CONTDIR)/%,$(_CONT))

ODIR= output
_OBJ= *.html static/css/style.css

OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
SETTINGS = conf.py

.PHONY: serve deploy render clean #not objects

serve: deploy
	cd $(ODIR) $(SEP) python -m SimpleHTTPServer 

deploy: render
	git add -A
	git commit -m 'update'
	git push

render: clean
	pelican -s $(SETTINGS)

clean: $(CONTENTS)
	$(RM) $(call FixPath, $(OBJ))

$(CONTENTS):
	@echo checking $@