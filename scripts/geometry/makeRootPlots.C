{
  TNtuple *T = new TNtuple("T","","d:s:sl:l:c:x:y:z");
  T->ReadFile("detector_hits.data");
  T->Draw("x:y:z","sl==0");

  TCanvas *c1 = new TCanvas("c1","FTOF Hits",1400,1400);
  c1->Divide(2,2);
  c1->cd(1);
  T->Draw("x:y:z","d==1&&sl==0&&c%2==0");
  T->Draw("x:y:z","d==1&&sl==0&&c%2!=0","same");
  c1->cd(2);
  T->Draw("x:y:z","d==1&&sl==1&&c%2==0");
  T->Draw("x:y:z","d==1&&sl==1&&c%2!=0","same");
  c1->cd(3);
  T->Draw("x:y>>H1PROJ(400,-450.0,450.0,400,-450.0,450.0)","d==1&&sl==0&&c%2==0","");
  T->Draw("x:y","d==1&&sl==0&&c%2!=0","same");
  c1->cd(4);
  T->Draw("x:y","d==1&&sl==1&&c%2==0","");
  T->Draw("x:y","d==1&&sl==1&&c%2!=0","same");

  c1->Print("ftof_detector_HITS.pdf");

  TCanvas *c2 = new TCanvas("c2","CND Hits",1200,600);
  c2->Divide(2,1);
  c2->cd(1);
  T->Draw("x:y:z","d==8&&l==2");
  T->Draw("x:y:z","d==8&&l==1","same");
  T->Draw("x:y:z","d==8&&l==0","same");
  c2->cd(2);
  T->Draw("x:y:z>>CNDL2","d==8&&l==2");
  T->Draw("x:y:z","d==8&&l==1","same");
  T->Draw("x:y:z","d==8&&l==0","same");
  TH3 *CND2 = (TH3*) gDirectory->Get("CNDL2");
  CND2->SetMarkerColor(2);
  c2->Modified();
  c2->Update();
  c2->Print("cnd_detector_HITS.pdf");


  TCanvas *c3 = new TCanvas("c3","EC Hits",1200,1200);
  c3->Divide(2,2);
  c3->cd(1);
  T->Draw("x:y:z","d==6&&l==0&&c%2==0");
  c3->cd(2);
  T->Draw("x:y:z","d==6&&l==1&&c%2==0");
  c3->cd(3);
  T->Draw("x:y:z","d==7&&l==2");
  c3->Print("ec_detector_HITS.pdf");
  

  TCanvas *c4 = new TCanvas("c4","Detector Hits",1200,1200);
  T->Draw("x:y:z","(d!=6&&d!=7)&&(d==8)||(d==1&&sl==0)");
  T->Draw("x:y:z","(d==1&&sl==1)","same");
  T->Draw("x:y:z","(d==1&&sl==2)","same");
  T->Draw("x:y:z","(d==5&&l==0)","same");

  c4->Print("all_detector_HITS.pdf");
}
