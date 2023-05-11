largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
hashtag = "#"
contador_l = 0
contador_a = 0
while largura <= 0 or altura <= 0:
      print()
      print("Digite uma largura ou altura maior do que 0")
      print()
      largura = int(input("digite a largura: "))
      altura = int(input("digite a altura: "))
while contador_a != altura:
      while contador_l != largura:
            print(hashtag, end = "")
            contador_l +=1
      if contador_a == altura and contador_l == largura:
               print()
      if contador_l == largura and contador_a != altura:
               print()
               contador_l = 0
      contador_a +=1
      
               
            
               
      
      
      
      
      
     

