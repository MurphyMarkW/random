#include <stdio.h>
#include "linkedlist.h"

std::list * l = NULL;

int main(int argc, char ** argv) {
  // Instantiate the LinkedList
  struct LinkedList * ll = LinkedList__create();

  // Populate the LinkedList with the character arrays we get from STDIN
  int i = 0;
  for(i; i < argc; i++) {
    printf("Adding: %s\n",argv[i]);
    LinkedList__add(ll,0,&argv[i]);
  }

  // Run through the elements of the LinkedList
  for(i = 0; i < LinkedList__size(ll); i++) {
    char ** s = NULL;
    LinkedList__at(ll,i,(void **)&s);
    printf("At %u: %s\n",i,s[0]);
  }

  // Remove elements from the front of the LinkedList
  while(LinkedList__size(ll)) {
    char ** s = NULL;
    LinkedList__remove(ll,0,(void **)&s);
    printf("Removed: %s\n",s[0]);
  }
}
