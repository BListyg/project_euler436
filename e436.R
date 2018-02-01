e436=function(a,b,r){f1=function(a,b){
  
  S = as.vector(NA);
  
  S[1] = 0;
  
  S[2] = runif(1,0,1)

while(sum(S)<a){ 
  
  x = runif(1,0,1)
  
  S = c(S,x); if(sum(S)>a) break

}
  
while(sum(S)<b){ 
  
  y = runif(1,0,1)
  
  S = c(S,y); 
  
  if(sum(S)>b) break

}
  
  if(x>y){return("P1")}
 
  else if(y>x){return("P2")}

}

out = t(table(replicate(r,f1(a,b))))/r

return(out)

}

###100

