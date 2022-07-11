#ifndef WORKLOAD_H
#define WORKLOAD_H

#include <memory>
#include "dbadapter.h"

namespace ledgerbench {

struct Task {
  int op;
};

class Workload {
 public:
  virtual std::unique_ptr<Task> NextTask() = 0;
  virtual int ExecuteTxn(Task* t, DB* db, Promise* promise) = 0;
};

}  // namespace ledgerbench

#endif  // WORKLOAD_H