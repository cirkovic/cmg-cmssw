#include <TPie.h>

class TPieEx : public TPie
{
public:
     TPieEx() : TPie::TPie() {};
     //TPieEx(const char *name, const char *title, int nvals, double *vals, int *cols) : TPie::TPie(name, title, nvals, reinterpret_cast<Double_t*>(vals), reinterpret_cast<Int_t*>(cols)) {};
     //TPieEx(const char *name, const char *title, double *vals, int nvals, int *cols) : TPie::TPie(name, title, nvals, reinterpret_cast<Double_t*>(vals), reinterpret_cast<Int_t*>(cols)) {}
     TPieEx(const char *name, const char *title, int nvals, double *vals) : TPie::TPie(name, title, nvals, reinterpret_cast<Double_t*>(vals), 0) {};
     ~TPieEx() {};
     
     ClassDef(TPieEx, 1);
};
