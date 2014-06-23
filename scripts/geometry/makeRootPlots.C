{
  TNtuple *T = new TNtuple("T","","d:s:sl:l:c:x:y:z");
  T->ReadFile("detector_hits.data");
  T->Draw("x:y:z","sl==0");

  TCanvas *c1 = new TCanvas("c1","",700,1400);

  c1->Divide(2,4);
  c1->cd(1);

  T->Draw("x:y:z>>H1","d==1&&sl==0&&s==0&&(c==5)");

  //  H1->SetMarkerColor(2);
  c1->cd(2);
  T->Draw("x:y:z>>H2","d==1&&sl==1");
  T->Draw("x:y:z>>H3","d==1&&sl==0","same");
  c1->cd(3);
  T->Draw("x:y","sl==0","contz");
  c1->cd(4);
  T->Draw("x:y","sl==1","contz");

  TCanvas *c2 = new TCanvas("c2","",700,1400);
  T->Draw("x:y:z","d==8&&l==2");
  T->Draw("x:y:z","d==8&&l==1","same");
  T->Draw("x:y:z","d==8&&l==0","same");
  TH3 *CND_1 = (TH3*) gDirectory->Get("CND1");
  CND_1->SetMarkerColor(2);

}
