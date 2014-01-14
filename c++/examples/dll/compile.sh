# Compile the object to be shared as Position Independent Code
g++ -fPIC -shared shared.cpp -o libshared.so
g++ -fPIC -shared othershared.cpp -o libothershared.so

# Compile the main program, identifying the directory and shared object
g++ -L`pwd` -lshared main.cpp -o main
