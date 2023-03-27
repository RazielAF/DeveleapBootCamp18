def main(bigstr,smallstr):
  bigstr=bigstr.replace(' ','')
  smallstr=smallstr.replace(' ',"")

  count={}
  
  for char in bigstr:
    if char in count:
      count[char]+=1
    else:
      count[char]=1
 
  for char in smallstr:
    if char in count and count[char]>0:
      count[char]-=1
    else:
      return False
  
  return True


  