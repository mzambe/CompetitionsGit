all : probl1 probl2 probl3 probl4 probl7 probl8 probl9 probl10 probl11 probl12 probl14 probl16 probl31

probl1 : probl1.ml
	ocamlopt probl1.ml -o probl1

probl2 : probl2.ml
	ocamlopt probl2.ml -o probl2

probl3 : probl3.py
	chmod +x probl3.py

probl4 : probl4.py
	chmod +x probl4.py

probl7 : probl7.py
	chmod +x probl7.py

probl8 : probl8.ml
	ocamlc probl8.ml -o probl8

probl9 : probl9.py
	chmod +x probl9.py

probl10 : probl10.py
	chmod +x probl10.py

probl11 : probl11.ml
	ocamlc probl11.ml -o probl11

probl12 : probl12.ml
	ocamlc probl12.ml -o probl12

probl14 : probl14.ml
	ocamlopt probl14.ml -o probl14

probl16 : probl16.ml
	ocamlopt probl16.ml -o probl16

probl31 : probl31.c
	gcc -Wall -O3 probl31.c -o probl31

clean :
	rm probl1 probl2 probl8 probl11
