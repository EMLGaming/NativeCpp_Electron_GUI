#include <nan.h>
#include "Vector.h"

//here we include all the header files


NAN_MODULE_INIT(InitModule) {
  Vector::Init(target);
}

NODE_MODULE(myModule, InitModule);
