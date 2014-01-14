// Some necessary libraries.
#include "shared.h"
#include <dlfcn.h>
#include <cstdio>

// Main function section.
int main(int argc, char ** argv) {
  // Tell the user to specify the shared library to use.
  if(argc < 2) {
    std::printf("Please specify the pathname of the shared library to use...\n");
    return -1;
  }

  // Identify to the user that the program has initiated.
  printf("This is a main-program-specific message.\n");

  // Get the handle to our shared library.
  void * handle = dlopen(argv[1],RTLD_LAZY);

  // Temporarily define two functions to hold the creation/destruction methods.
  Shared * (*create)();
  void (*destroy)(Shared*);

  // Retrieve the creation/destruction methods and assign them.
  create = (Shared * (*)())dlsym(handle,"create");
  destroy = (void (*)(Shared * ))dlsym(handle,"destroy");

  // Use the creation method to get a pointed to an instance of the shared class.
  Shared * shared = (Shared*) create();

  // Use the instance's method.
  shared->method();

  // Use the destruction method to deallocate the instace of the shared class.
  destroy(shared);

  // Close the handle to our shared library.
  dlclose(handle);

  // We're done. Exit 0.
  return 0;
}
