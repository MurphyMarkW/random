#ifndef __SHARED_H__
#define __SHARED_H__

class Shared {
  public:
    Shared();
    virtual void method();
  private:
    const char * message;
};

#endif
