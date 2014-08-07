void script (string option)
{
	gROOT->ProcessLine(".L trainMVA_2lss.cxx");
	trainMVA_2lss(option);
}

