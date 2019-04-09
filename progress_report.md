# 7.2.2019: Progress Report 0




Create git repository
# 25.2.2019: Progress Report 1





Scraped articles from BBC (350), Kommersant (5.290), Radio Svoboda (2.929), Reuters (295), and Tass (3.060). Total is like 12.000-ish articles.<br><br>
[Data overview](https://github.com/Data-Science-for-Linguists-2019/Sentiment-Analysis-of-Russian-Language-News/blob/master/data_overview.ipynb)<br> [Sample File (BBC)](https://github.com/Data-Science-for-Linguists-2019/Sentiment-Analysis-of-Russian-Language-News/blob/master/data_sample/bbc/10_%D1%88%D0%B0%D0%B3%D0%BE%D0%B2_%D0%B4%D0%BE_%D0%BA%D1%80%D0%B0%D1%85%D0%B0_%D0%BA%D0%B0%D0%BA_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D1%8F_%D0%B4%D0%BE%D1%88%D0%BB%D0%B0_%D0%B4%D0%BE_%D0%B4%D0%B5%D1%84%D0%BE%D0%BB%D1%82%D0%B0_1998_%D0%B3%D0%BE%D0%B4%D0%B0_16_%D0%B0%D0%B2%D0%B3%D1%83%D1%81%D1%82%D0%B0_2018.txt)
<br><br>


Sharing plan
-----------
I will probably put all my files on GitHub publicly, so people can just download them if they want. As far as I can tell none of the sites limit sharing of their articles except maybe Reuters, which is sort of vague about its policy (it just says it is in line with Norwegian copyright law). Other than that most of their policies seem to permit sharing if it doesn't earn me profit.


# 19.3.2019: Progress Report 2




Lemmatized all of the dataframes. Made LDA and LSA topic models for each of the data sets as well for all of the sites together. Found and cleaned a set of Russian words with sentiment (happy, angry, sad, etc.), grouped these sets into positive and negative, and pickled. 

### Licensing

I selected MIT license as license type, since it seems to be incredibly broad and to the point. I was considering writing something even broader and simpler myself, like "this data can be used without compensation for any purpose whatsoever with no restrictions", but I felt like it would be better to use an established one. 

### Sharing 
Tass's terms of use 3.1.1: <br>

- Использование текстовых материалов, размещенных на Сайте Агентства, возможно без письменного согласия и на безвозмездной основе исключительно в следующих случаях: (Use of text materials posted on the Agency's site is possible without written permission and for free in the following situations:"

- На персональных страницах физических лиц в сети Интернет, в том числе в личных, информационных, научных, культурных, учебных целях, без извлечения прибыли ("On the personal page of a natural person on the Internet, including for personal, informational, scientific, cultural, or educational goals, without earning a profit.")

So, I can definitely post their data.

BBC's terms of use refer to the English Copyright, Design and Patents Act of 1998 which allows for fair use for research purposes:

- Fair dealing with a... work for the purposes of research for a non-commercial purpose does not infringe any copyright in the work provided that it is accompanied by a sufficient acknowledgement. (section 29.1)

So I can use BBC's content.

Kommersant's terms of use say their content is protected by Russian copyright law. According to Article 1274 of the Civil Code of the Russian Federation:

- Article 1274. Free Use of a Work for Informational, Scientific,
Educational, or Cultural Purposes
	- The following uses are allowed without the consent of the author or other rightholder and without the payment of remuneration but with an obligatory indication of the name of the author whose work is used and of the source of borrowing:
	1. citation in the original and in translation for scientific, polemical/critical, or information purposes of works lawfully made public in an amount justified by the purpose of citation, including the reproduction of excerpts from newspaper and magazine articles in the form of press surveys.

So I can share Kommersant's data.

From Radio Free Europe's terms of service (which I assume are the same as the Russian version):

- Re-Use of Text Content

	- When using RFE/RL text content in full, we require that you credit RFE/RL by including:
		- A permanent link, placed before the text of the article, to the original article on www.rferl.org,
		- The following text somewhere in the article: Copyright (c) 2019. RFE/RL, Inc. Reprinted with the permission of Radio Free Europe/Radio Liberty, 1201 Connecticut Ave NW, Ste 400, Washington DC 20036. 
	- When using excerpts of RFE/RL text content, we require that you note that the material is an excerpt and link to the original content somewhere in your text. You must also refrain from altering or distorting the meaning, name, or integrity of the product.
	
Obviously, adding that "Copyright(c)..." thing into the data set is not feasible but I believe the are assuming the user is a news or personal site, so just putting that acknowledgement anywhere in my project would probably be sufficient. Similarly, I can't put links anywhere in the data set, but I have them in my csv file.

So I can use Radio Svoboda's content.

I still have to figure out how it works with Reuters, so I won't post their articles yet.

In addition to the above, I will post pickled dataframes (or maybe series I forget) with all of the articles' (other than from Reuters) lemmatized text.

Apart from the article data, I also downloaded a wordnet-affect type jawn that was adapted to Russian, I'm not sure if I'll end up using it but I might as well post it. According to their site, I have to cite them as 'Sokolova M., Bobicev V. "Classification of Emotion Words in Russian and Romanian Languages". Proceedings of RANLP-2009 conference, Borovets, Bulgaria, pp. 415-419, 2009. [pdf](http://lilu.fcim.utm.md/SokolovaBobicevRANLP2009.pdf) to use it, but that's it.

# 9.4.2019: Progress Report 3




Continued doing topic modeling. Tried bigram and trigram models, and looked at perplexity and (UMass) coherence scores. I also attempted to use gensim's mallet wrapper which apparently performs better but got an error message. This work can be seen [here](add link).
