\ENCODING=ISO-8859-1
\Problem name: tsp

Minimize
 obj: x2 + 2 x3 + 3 x4 + x5 + 3 x7 + 4 x8 + 2 x9 + 3 x10 + 5 x12 + 3 x13
      + 4 x14 + 5 x15
Subject To
 c1:  x1 + x2 + x3 + x4  = 1
 c2:  x5 + x6 + x7 + x8  = 1
 c3:  x9 + x10 + x11 + x12  = 1
 c4:  x13 + x14 + x15 + x16  = 1
 c5:  x1 + x5 + x9 + x13  = 1
 c6:  x2 + x6 + x10 + x14  = 1
 c7:  x3 + x7 + x11 + x15  = 1
 c8:  x4 + x8 + x12 + x16  = 1
 c9:  x2 + x3 + x4 >= 1
 c10: x3 + x4 + x7 + x8 >= 1
 c11: x2 + x4 + x10 + x12 >= 1
 c12: x4 + x8 + x12 >= 1
 c13: x2 + x3 + x14 + x15 >= 1
 c14: x3 + x7 + x15 >= 1
 c15: x2 + x10 + x14 >= 1
Bounds
 0 <= x1 <= 1
 0 <= x2 <= 1
 0 <= x3 <= 1
 0 <= x4 <= 1
 0 <= x5 <= 1
 0 <= x6 <= 1
 0 <= x7 <= 1
 0 <= x8 <= 1
 0 <= x9 <= 1
 0 <= x10 <= 1
 0 <= x11 <= 1
 0 <= x12 <= 1
 0 <= x13 <= 1
 0 <= x14 <= 1
 0 <= x15 <= 1
 0 <= x16 <= 1
Binaries
 x1  x2  x3  x4  x5  x6  x7  x8  x9  x10  x11  x12  x13  x14  x15  x16 
End
