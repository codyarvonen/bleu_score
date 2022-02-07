# bleu_score

Below are the deliverables for Assignment 9 along with a description of the `bleu.py` BLEU score calculator I implemented.

1121 sentances translated by Google Translate and DeepL

Running `sacrebleu reference.txt -i translation1.txt -m bleu -b -w 4` gives us a BLEU score of 51.4222

Running `sacrebleu reference.txt -i translation2.txt -m bleu -b -w 4` gives us a BLEU score of 48.0188

Running `python3 bleu.py` and uncommenting the `candidate = open("translation1.txt", "r")` line gives us a BLEU score of 47.2884

Running `python3 bleu.py` and uncommenting the `candidate = open("translation2.txt", "r")` line gives us a BLEU score of 45.2631

As shown in `tilde_bleu.png`, translation1.txt receives a BLEU score of 52.64 and translation2.txt receives a BLEU score of 49.47

The results from the DQF as shown in `dqf.png` confirms that `translation1.txt` (Google translate) scores higer than `translation2.txt` (DeepL)


**Analysis:**

Were the two sets of BLEU scores the same? Why or why not?
- The BLEU scores for two different MT systems were not the same. Across all of the BLEU score calculations, `translation1.txt` out performed `translation2.txt`. The actual scores themselves differ because of the slightly different calculation methods implemented. For example, my implementation of the BLEU score calculation is not likely to exactly match a highly developed sacrebleu. My hypothesis for why the scores from my script are lower in general is because there is nothing in my script to account for punctuation or other special cases. This could cause some matches to be skipped. Otherwise, I believe it was failry successful.

How closely did the BLEU scores correlate with your ranking, or did they not correlate at all?
- All of the BLEU score calculations that were computed correlate with the manual ranking that I gave the 50 sentances. A preference is given to the Google Translate system over DeepL.

Provide your thoughts/hypothesis on why they did or did not correlate.
- I belive that my success in computing consistent BLEU scores and having their scores match the manual ranking is due to the fact that I was easily able to find 1000+ sentances. The larger the dataset is, the more likely the BLEU scores are to be consistent because the effects of outliers are minimized.


**The seven files contained in this repository are listed and described below:**

`bleu.py` contains the code that calculates the BLEU score according to my implementation. Uncomment line 11 or 13 in order to choose between the different translation files (`translation1.txt`, etc.). The script iterates through each line in the reference and candidate files and accumulates the number of n-grams. After that, the BLEU score is calculated and displayed in the terminal.

`source.txt` contains the source text from the dataset given to us in class including the 50 sentances used in the DQF

`reference.txt` contains the reference translation from the dataset given to us in class

`translation1.txt` contains the Google Tranlsate output of `source.txt`

`translation2.txt` contains the DeepL output of `source.txt`

`dqf.png` is the image that shows the results of the manual ranking

`tilde_bleu.png` is the image that shows the results of the BLEU score calculation from Tilde Custom Machine Translation
