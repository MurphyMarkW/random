#include <stdlib.h>
#include "errorcodes.h"

typedef struct LLIterator {
  LinkedList * ll;
  LinkedList__Tuple * t;
} LLIterator;

// Factory methods
extern struct LLIterator * LLIterator__create(LinkedList * ll);
extern void LLIterator__destroy(LLIterator * itt);

// Navigation methods
extern int LLIterator__first(LLIterator * itt);
extern int LLIterator__last(LLIterator * itt);
extern int LLIterator__next(LLIterator * itt);
extern int LLIterator__prev(LLIterator * itt);

// Accessors and modification methods
extern int LLIterator__assign(LLIterator * itt,void * obj);
extern int LLIterator__append(LLIterator * itt,void * obj);
extern int LLIterator__prepend(LLIterator * itt,void * obj);
extern int LLIterator__at(LLIterator * itt,void ** obj);
extern int LLIterator__remove(LLIterator * itt,void ** obj);


extern int LinkedList__split(LinkedList * ll,uint32_t pos,LinkedList ** ll1,LinkedList ** ll2);
extern struct LinkedList * LinkedList__merge(LinkedList * ll1,LinkedList * ll2);
