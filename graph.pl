/* Md Ashiqur Rahman : 1007035 */

coloring(1,1,5,b,C) :- true.
coloring(2,2,5,b,C) :- true.
coloring(3,3,5,b,C) :- true.
coloring(4,4,5,b,C) :- true.
coloring(5,5,5,b,C) :- true.
coloring(2,1,5,b,C) :- true.
coloring(3,2,5,b,C) :- true.
coloring(4,3,5,b,C) :- true.
coloring(5,4,5,b,C) :- true.

adjacent(1,2).         adjacent(2,1). 
adjacent(1,3).         adjacent(3,1). 
adjacent(1,4).         adjacent(4,1). 
adjacent(1,5).         adjacent(5,1). 
adjacent(2,3).         adjacent(3,2). 
adjacent(2,4).         adjacent(4,2). 
adjacent(3,4).         adjacent(4,3). 
adjacent(4,5).         adjacent(5,4). 

/*------------------------------------*/

color(1,red,a).    color(1,red,b). 
color(2,blue,a).   color(2,blue,b). 
color(3,green,a).  color(3,green,b). 
color(4,yellow,a). color(4,blue,b). 
color(5,blue,a).   color(5,green,b). 

/*------------------------------------*/

conflict(Coloring,C) :- 
   adjacent(X,Y,C),
   color(X,Color,Coloring), 
   color(Y,Color,Coloring).

/*-------------------------------------*/

conflict(R1,R2,Coloring) :- 
   adjacent(R1,R2), 
   color(R1,Color,Coloring), 
   color(R2,Color,Coloring).

coloring(R1,R2,N,Coloring,C) :- 
   R1>2,
   R1\=R2,
   R1 is R1-1,
   coloring(R1,R2,N,Coloring,C1),
   C is C1+1,
   adjacent(R1,R2), 
   color(R1,Color,Coloring), 
   color(R2,Color,Coloring),
   R2<N,
   R2 is R2+1,
   coloring(R1,R2,N,Coloring,C1).
