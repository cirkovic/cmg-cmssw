#include <CMGTools/TTHAnalysis/interface/TPieE.h>

/*
TPieE::TPieE() : TPie::TPie()
{
}
*/
TPieE::TPieE(const char *name, const char *title, int nvals, double *vals, int *cols) : TPie::TPie(name, title, nvals, reinterpret_cast<Double_t*>(vals), reinterpret_cast<Int_t*>(cols))
{
}
/*
TPieE::~TPieE() : TPie::TPie()
{
}
*/
