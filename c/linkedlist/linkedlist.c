#include "linkedlist.h"

//#define DEBUG

#ifdef DEBUG
#include <stdio.h>
#endif

/**
 * Linked List factory method.
**/
struct LinkedList * LinkedList__create() {
  struct LinkedList * ll = (LinkedList *)malloc(sizeof(LinkedList));
  ll->keynode = (LinkedList__Tuple *)malloc(sizeof(LinkedList__Tuple));
  #ifdef DEBUG
  printf("LinkedList::LinkedList__create\t%u\t%u\n",ll,ll->keynode);
  #endif
  ll->keynode->obj = NULL;
  ll->keynode->next = ll->keynode;
  ll->keynode->prev = ll->keynode;
  return ll;
};

/**
 * Linked List recycler method.
**/
void LinkedList__destroy(LinkedList * ll) {
  // Remove all elements which were added to the Linked List.
  // Does not 
  while(LinkedList__size(ll)) LinkedList__remove(ll,0,NULL);
  free(ll->keynode);
  free(ll);
};

// Class utility functions. Not to be used externally.
// ===================================================

// Returns the tuple located at pos in the Linked List ll.
struct LinkedList__Tuple * getTuple(LinkedList * ll,unsigned int pos) {
  #ifdef DEBUG
  printf("LinkedList::getTuple\t%u\t%u\n",ll,pos);
  #endif
  struct LinkedList__Tuple * t = (LinkedList__Tuple *)ll->keynode->next;
  while(pos) {
    t = t->next;
    pos--;
  }
  #ifdef DEBUG
  printf("LinkedList::getTuple\treturned: %u\n",t);
  #endif
  return t;
};

// Instantiates a LinkedList__Tuple structure and adds the LinkedList__Tuple to the Linked List ll at position pos.
void addTuple(LinkedList * ll,unsigned int pos,void * obj) {
  #ifdef DEBUG
  printf("LinkedList::addTuple\t%u\t%u\t%u\n",ll,pos,obj);
  #endif
  struct LinkedList__Tuple * prev = ll->keynode;
  while(pos) { prev = prev->next; pos--; }
  struct LinkedList__Tuple * t = (LinkedList__Tuple*)malloc(sizeof(LinkedList__Tuple));
  t->obj = obj;

  t->prev = prev;
  t->next = prev->next;
  t->next->prev = t;
  t->prev->next = t;

  ll->size++;

  #ifdef DEBUG
  printf("LinkedList::addTuple\tadded: %u\t%u\n",t,obj);
  #endif
  return;
};

// Removes a LinkedList__Tuple structure, deallocates the memory associated with the LinkedList__Tuple and passes back the object reference.
void removeTuple(LinkedList * ll,unsigned int pos,void ** obj) {
  #ifdef DEBUG
  printf("LinkedList::removeTuple\t%u\t%u\t%u\n",ll,pos,(*obj));
  #endif
  struct LinkedList__Tuple * t = ll->keynode;
  while(pos) { t = t->next; pos--; }
  t = t->next;

  t->prev->next = t->next;
  t->next->prev = t->prev;

  (*obj) = t->obj;
  ll->size--;
  free(t);

  #ifdef DEBUG
  printf("LinkedList::removeTuple\tremoved: %u\tpassed: %u\n",t,(*obj));
  #endif
  return;
};


// Public class methods.
// =====================

/**
 * Linked List size accessor.
 * Returns the size of the Linked List as an unsigned int.
**/
unsigned int LinkedList__size(LinkedList * ll) {
  #ifdef DEBUG
  printf("LinkedList::LinkedList__size\t%u\t%u\n",ll,ll->size);
  #endif
  return ll->size;
};

/**
 * Linked List element accessor.
 * Passes the pos referenced object pointer back through obj.
**/
int LinkedList__at(LinkedList * ll,unsigned int pos,void ** obj) {
  #ifdef DEBUG
  printf("LinkedList::LinkedList__at\t%u\t%u\t%u\n",ll,pos,(*obj));
  #endif
  if(pos >= LinkedList__size(ll)) return ERROR_INDEX;
  (*obj) = getTuple(ll,pos)->obj;
  #ifdef DEBUG
  printf("LinkedList::LinkedList__at\tpassed: %u\n",(*obj));
  #endif
  return 0;
};

/**
 * Linked List add method.
 * Adds the passed object pointer to the Linked List at position pos.
**/
int LinkedList__add(LinkedList * ll,unsigned int pos,void * obj) {
  #ifdef DEBUG
  printf("LinkedList::LinkedList__add\t%u\t%u\t%u\n",ll,pos,obj);
  #endif
  if(pos > LinkedList__size(ll)) return ERROR_INDEX;
  addTuple(ll,pos,obj);
  #ifdef DEBUG
  printf("LinkedList::LinkedList__add\tadded: %u\n",obj);
  #endif
  return 0;
};

/**
 * Linked List remove method.
 * Removes the object from position pos in the Linked List and passes the reference object back through obj.
**/
int LinkedList__remove(LinkedList * ll,unsigned int pos,void ** obj) {
  #ifdef DEBUG
  printf("LinkedList::LinkedList__remove\t%u\t%u\t%u\n",ll,pos,(*obj));
  #endif
  if(pos >= LinkedList__size(ll)) return ERROR_INDEX;
  removeTuple(ll,pos,obj);
  #ifdef DEBUG
  printf("LinkedList::LinkedList__remove\tpassed: %u\n",(*obj));
  #endif
  return 0;
};
