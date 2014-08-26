void trainMVA_2lss(TString name) {
    TString Path = "/afs/cern.ch/work/c/cirkovic/TREES_250513_HADD";
    //gROOT->ProcessLine(".L ../../../python/plotter/functions.cc+");

    TFile *fOut = new TFile(name+".root","RECREATE");
    TMVA::Factory *factory = new TMVA::Factory(name, fOut, "!V:!Color");

    TFile *fSig = TFile::Open(Path+"/TTH122/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    TTree *tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    tSig->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTH122.root");
    factory->AddSignalTree(tSig, 1.0);
    fSig = TFile::Open(Path+"/TTH127/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
    tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
    tSig->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTH127.root");
    factory->AddSignalTree(tSig, 1.0);

//    fSig = TFile::Open(Path+"/TTH/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
//    tSig = (TTree *) fSig->Get("ttHLepTreeProducerBase");
//    tSig->AddFriend("sf/t", Path+"/2_finalmva_2lss_v2/evVarFriend_TTH.root");
//    factory->AddSignalTree(tSig, 1.0);

    TCut all = "nLepGood == 2 && LepGood1_charge == LepGood2_charge && nBJetMedium25 >= 1 && nJet25 >= 4 && LepGood2_pt > 20 && LepGood1_pt+LepGood2_pt+met > 100";
    if (name.Contains("ttW")) {
        TFile *fBkg = TFile::Open(Path+"/TTWJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
		tBkg->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTWJets.root");
        factory->AddBackgroundTree(tBkg, 1.0);
    } else if (name.Contains("ttbar")) {        
        TFile *fBkg = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg = (TTree *) fBkg->Get("ttHLepTreeProducerBase");
        tBkg->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTJets.root");
        factory->AddBackgroundTree(tBkg, 1.0);
    } else if (name.Contains("mix")) {
        TFile *fBkg1 = TFile::Open(Path+"/TTJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg1 = (TTree *) fBkg1->Get("ttHLepTreeProducerBase");
        tBkg1->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTJets.root");
        factory->AddBackgroundTree(tBkg1, 1.0);
        TFile *fBkg2 = TFile::Open(Path+"/TTWJets/ttHLepTreeProducerBase/ttHLepTreeProducerBase_tree.root");
        TTree *tBkg2 = (TTree *) fBkg2->Get("ttHLepTreeProducerBase");
        tBkg2->AddFriend("sf/t", "/afs/cern.ch/work/c/cirkovic/Milos_24-08-2014/26-08-2014/1/1/evVarFriend_TTWJets.root");
        factory->AddBackgroundTree(tBkg2, 1.0);
    } else  {
        std::cout << "Training not implemented " << std::endl;
        return;
    }

    if (name.Contains("_mm")) {
        all += "abs(LepGood1_pdgId) == 13 && abs(LepGood2_pdgId) == 13";
    } else if (name.Contains("_em")) {
        all += "abs(LepGood1_pdgId) != abs(LepGood2_pdgId)";
    } else if (name.Contains("_ee")) {
        all += "abs(LepGood1_pdgId) == 11 && abs(LepGood2_pdgId) == 11";
    }

        
    factory->AddVariable("lep2AbsEta := abs(LepGood2_eta)", 'F'), 	//good
    //factory->AddVariable("lep2Pt := LepGood2_pt", 'F'), 		//bad
    //factory->AddVariable("MHT : = mhtJet25", 'F'),			//bad
    factory->AddVariable("mindr_lep2_jet : = mindr_lep2_jet", 'F'),	//good
    //factory->AddVariable("MT_met_lep1 : = MT_met_lep1", 'F'),		//bad
    factory->AddVariable("sum_pt : = htJet25", 'F');			//good
    
    factory->AddVariable("avg_dr_jet : = avg_dr_jet", 'F'),		//good
    factory->AddVariable("mindr_lep1_jet := mindr_lep1_jet", 'F'),	//good
    //factory->AddVariable("MT_met_leplep := MT_met_leplep", 'F'),	//bad
    
    //factory->AddVariable("numJets_float := nJet25", 'F'),		//bad
    
    //factory->AddVariable("b1_jet_pt := Jet1_pt", 'F'),			//bad
    //factory->AddVariable("b2_jet_pt := Jet2_pt", 'F'),			//bad
    //factory->AddVariable("lep1pt := LepGood1_pt", 'F'),			//bad
    factory->AddVariable("htJet25 - (sum_abspz - abs(sum_sgnpz)) := htJet25 - (sum_abspz - abs(sum_sgnpz))", 'F'), //good
    factory->AddVariable("htJet25/sum_abspz := htJet25/sum_abspz", 'F'),	//good
    
    factory->AddVariable("m_tjjb := min(m_tjjb, 330)", 'F'),		//good
    factory->AddVariable("m_tlvb := min(m_tlvb, 330)", 'F'),		//good
    //factory->AddVariable("m_Wjj := min(m_Wjj, 330)", 'F'),		//bad
    //factory->AddVariable("mt_Wlv := min(mt_Wlv, 330)", 'F'),		//bad
   
            
#endif

    factory->SetWeightExpression("1");
    factory->PrepareTrainingAndTestTree( all, all, "SplitMode=Random" );

    factory->BookMethod( TMVA::Types::kLD, "LD", "!H:!V:VarTransform=None:CreateMVAPdfs" );

    TString BDTGopt = "!H:!V:NTrees=200:BoostType=Grad:Shrinkage=0.10:!UseBaggedGrad:nCuts=200:nEventsMin=100:NNodesMax=5";

    BDTGopt += ":CreateMVAPdfs"; // Create Rarity distribution
    factory->BookMethod( TMVA::Types::kBDT, "BDTG", BDTGopt);

    factory->TrainAllMethods();
    factory->TestAllMethods();
    factory->EvaluateAllMethods();

    fOut->Close();
}
