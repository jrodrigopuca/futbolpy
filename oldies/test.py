# bhattacharyya test
import numpy
import math

h1 = [ 1, 2, 3, 4, 5, 6, 7, 8 ];
h2 = [ 1, 2, 3, 4, 5, 6, 7, 8 ];
h3 = [ 8, 7, 6, 5, 4, 3, 2, 1 ];
h4 = [ 1, 2, 3, 4, 4, 3, 2, 1 ];
h5 = [ 8, 8, 8, 8, 8, 8, 8, 8 ];

h = [ h1, h2, h3, h4, h5 ];

def mean( hist ):
    mean = 0.0;
    for i in hist:
        mean += i;
    mean/= len(hist);
    return mean;

def bhatta ( hist1,  hist2):
    # calculate mean of hist1
    h1_ = mean(hist1);

    # calculate mean of hist2
    h2_ = mean(hist2);

    # calculate score
    score = 0;
    for i in range(8):
        score += math.sqrt( hist1[i] * hist2[i] );
    # print h1_,h2_,score;
    score = math.sqrt( 1 - ( 1 / math.sqrt(h1_*h2_*8*8) ) * score );
    return score;

print(bhatta(h1,h2))