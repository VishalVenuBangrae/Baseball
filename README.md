# Baseball Program

This Python program reads data from two data files, `teams.dat` and `games.dat`, stored within a folder whose name will be provided in the command line.

## Data Files

Atlanta Braves:ATL
St. Louis Cardinals:STL
Chicago Cubs:CHC
Arizona Diamondbacks:ARI
Cleveland Indians:CLE

**teams.dat**:

2004-03-20:ARI:CHC:10:11
2004-03-23:ATL:STL:0:1
2004-03-27:STL:CHC:7:9
2004-03-27:CLE:ATL:1:0
2004-03-30:ATL:CHC:10:5

# SAMPLE RUN 

$ python3 Baseball.py data

(s) Standings
(t) Team results
(q) Quit

What do you want to see: s

TEAM                   WINS LOSSES   TIES PERCENT
-------------------- ------ ------ ------ -------
CHC                       6      3      0  0.667
ARI                       5      3      1  0.611
STL                       4      5      0  0.444
ATL                       3      5      1  0.389
CLE                       2      4      2  0.375

(s) Standings
(t) Team results
(q) Quit

What do you want to see: t
Enter team code (e.g. ARI, ATL, CHC, CLE, STL): CSC
Invalid team code

(s) Standings
(t) Team results
(q) Quit

What do you want to see: t
Enter team code (e.g. ARI, ATL, CHC, CLE, STL): CHC

Team: Chicago Cubs

      DATE   OPPONENT   US  THEM  RESULT
2004-03-20     at ARI   11    10     WIN
2004-03-27     at STL    9     7     WIN
2004-03-30     at ATL    5    10    LOSS
2004-04-22        CLE    7     4     WIN
2004-04-24        ARI    7    12    LOSS
2004-05-01        STL   10     0     WIN
2004-05-04        ATL   10     8     WIN
2004-05-15     at CLE    8     6     WIN
2004-05-18     at ARI    5    13    LOSS

Overall Record: 6-3-0

(s) Standings
(t) Team results
(q) Quit

What do you want to see: q


