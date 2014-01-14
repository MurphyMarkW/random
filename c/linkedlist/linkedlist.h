#include <stdlib.h>
#include "errorcodes.h"

typedef struct LinkedList {
  unsigned int size;
  struct LinkedList__Tuple * keynode;
} LinkedList;

typedef struct LinkedList__Tuple {
  void * obj;
  struct LinkedList__Tuple * next;
  struct LinkedList__Tuple * prev;
} LinkedList__Tuple;

// Constructor / destructor.
extern struct LinkedList * LinkedList__create();
extern void LinkedList__destroy(LinkedList * ll);

// Basic methods and accessor.
extern unsigned int LinkedList__size(LinkedList * ll);
extern int LinkedList__at(LinkedList * ll,unsigned int pos,void ** obj);
extern int LinkedList__add(LinkedList * ll,unsigned int pos,void * obj);
extern int LinkedList__remove(LinkedList * ll,unsigned int pos,void ** obj);
