ifeq ($(OS),Windows_NT)

	RM = del /s /q
	FixPath = $(subst /,\,$1)

    CCFLAGS += -D WIN32
    ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
        CCFLAGS += -D AMD64
    endif
    ifeq ($(PROCESSOR_ARCHITECTURE),x86)
        CCFLAGS += -D IA32
    endif
    UNAME = Win
else

	RM = rm -rf
	FixPath = $1

    UNAME_S := $(shell uname -s)
    ifeq ($(UNAME_S),Linux)
        CCFLAGS += -D LINUX
    endif
    ifeq ($(UNAME_S),Darwin)
        CCFLAGS += -D OSX
    endif
    UNAME_P := $(shell uname -p)
    ifeq ($(UNAME_P),x86_64)
        CCFLAGS += -D AMD64
    endif
    ifneq ($(filter %86,$(UNAME_P)),)
        CCFLAGS += -D IA32
    endif
    ifneq ($(filter arm%,$(UNAME_P)),)
        CCFLAGS += -D ARM
    endif
endif

ODIR= output
_OBJ= *.html static/css/style.css

OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))
SETTINGS = conf.py

serve: deploy
	cd $(ODIR)
	python -m SimpleHTTPServer 

render: clean
	pelican -s $(SETTINGS)

deploy: render
	git add -A
	git commit -m 'update'
	git push

clean:
	$(RM) $(call FixPath, $(OBJ))