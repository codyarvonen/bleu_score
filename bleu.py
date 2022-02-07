import numpy as np

def find_ngrams(input, n):
    ngram = []
    for i in range(len(input)-n+1):
        ngram.append(tuple(input[i:i+n]))
    return ngram

refer = open("reference.txt", "r")

candidate = open("translation1.txt", "r")

# candidate = open("translation2.txt", "r")

print("Calculating BLEU score for candidate...")

p1 = 0
p2 = 0
p3 = 0
p4 = 0
w1 = 0
w2 = 0
w3 = 0
w4 = 0
count = 0

for cand, ref in zip(candidate, refer):

    r_n1 = ref.split()
    c_n1 = cand.split()

    r_n2 = find_ngrams(r_n1, 2)
    r_n3 = find_ngrams(r_n1, 3)
    r_n4 = find_ngrams(r_n1, 4)

    c_n2 = find_ngrams(c_n1, 2)
    c_n3 = find_ngrams(c_n1, 3)
    c_n4 = find_ngrams(c_n1, 4)

    r_n2 = list(set(r_n2))
    c_n2 = list(set(c_n2))
    r_n3 = list(set(r_n3))
    c_n3 = list(set(c_n3))
    r_n4 = list(set(r_n4))
    c_n4 = list(set(c_n4))

    p1 += np.sum([np.unique(r_n1).tolist().count(ngram) for ngram in c_n1])
    p2 += np.sum([r_n2.count(ngram) for ngram in c_n2])
    p3 += np.sum([r_n3.count(ngram) for ngram in c_n3])
    p4 += np.sum([r_n4.count(ngram) for ngram in c_n4])
    w1 += len(r_n1)
    w2 += len(r_n2)
    w3 += len(r_n3)
    w4 += len(r_n4)

n = 4
P = (p1/w1) * (p2/w2) * (p3/w3) * (p4/w4)

b = np.power(P,(1/n))

if len(r_n1) < len(c_n1):
    bp = 1
else:
    bp = np.exp(1 - (len(r_n1)/len(c_n1)))

bleu = bp * b

print("BLEU score for candidate: {}".format(bleu*100))
