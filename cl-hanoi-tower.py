def towerOfHanoi(n, fromRod, toRod, auxRod):
  
  if n ==0:
    
    return
  
  towerOfHanoi(n-1, fromRod, auxRod, toRod)
  
  print("Move disk",n,"From rod",fromRod,"to rod",toRod)
  
  towerOfHanoi(n-1, auxRod, fromRod, toRod)
  
  n = 6

  towerOfHanoi(n, "A", "C", "B")

