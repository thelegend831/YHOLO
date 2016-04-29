text = """
  **   **    
 **** ****   
***********  
  *******    
   *****     
     *       
"""





text = """
         *******        
      *************     
    ***  *******  ***   
  ****    *****    ***  
 *****    *****    **** 
*******  *******  ******
***  **************  ***
 ***   **********   *** 
  ***      **    ****   
    ****        ***     
      *****  *****      
         ******         
"""

text = """
**     **      **   **        ***        **             ***     
**     **      **   **        ***        **             ***     
 **   **       **   **       ** **       **            ** **    
 **   **       **   **       ** **       **            ** **    
 **   **       *******      **   **      **           **   **   
  ** **        *******      **   **      **           **   **   
   ***         *******      **   **      **           **   **   
   ***         *******      **   **      **           **   **   
   ***         **   **       ** **       **            ** **    
   ***         **   **       ** **       **            ** **    
   ***         **   **        ***        *******        ***     
   ***         **   **        ***        *******        ***     
"""

text = """
   ***    ***   
   ***    ***   
   ***    ***   
   ***    ***   
   **********   
   **********   
   **********   
   **********   
   ***    ***   
   ***    ***   
   ***    ***   
   ***    ***   
"""

text = text.splitlines()

m = []
text.pop(0)
for line in text:
    l = []
    for char in line:
        symbol = 1
        if char == ' ':
            symbol = 0
        l.append( symbol )
    m.append(l)

t = []
for k in range( len( m[0] ) ):
    col = []
    for j in range( len(m) ):
        col.append( m[j][k] )
    t.append( col )

seq = []
for col in t:
    x = [ str(n) for n in col ]
    string_num = ''.join( x )
    string_num = string_num[::-1]
    num = int( string_num, 2 )
    seq.append( num )

print seq