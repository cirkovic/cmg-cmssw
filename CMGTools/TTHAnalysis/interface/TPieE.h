#include <TPie.h>

class TPieE : public TPie
{
public:
     //TPieE();
     TPieE(const char *name, const char *title, int nvals, double *vals, int *cols);
     //~TPieE();
     
     ClassDef(TPieE, 1)
};
