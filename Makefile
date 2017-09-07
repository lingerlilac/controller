objects =  receivea.so

# helloworld: $(objects)
# 	gcc -o receivea $(objects)  -lpthread -L/usr/lib/mysql -lmysqlclient
receivea.so: receivea.c hash_lin.h
	gcc -fPIC -shared receivea.c -o receivea.so -I /usr/include/python2.7/ -lpython2.7 -lpthread -L/usr/lib/mysql -lmysqlclient
clean:
	rm -f *.so receivea