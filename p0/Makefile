
SRC=hw
EXE=$(SRC)


do: console

all: console postscript troff clean

console: awk bc c c++ factor forth haskell java javascript lisp lua perl python ruby scheme sh \
	 clean

python: $(SRC).py
	@echo "Hola Mundo en $@..."
	python $<

clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class
