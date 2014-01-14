#include "shared.h"
#include <cstdio>

// Can be overwritten to provide on-the-fly functionality.
extern "C" Shared * create() {
  return new Shared;
}

// Can be overwritten to provide on-the-fly functionality.
extern "C" void destroy(Shared * object) {
  delete object;
}

Shared::Shared() {
  Shared::message="This is a library-specific message.\n";
}

void Shared::method() {
  std::printf("%s",Shared::message);
}
