# entity_resolution_spark
Collection of some algorithms for entity resolution.


Written in python. 


Refer spark_template.py(tbi) for applying the algorithm.

refer howtoguide for the overview of features.

Character and Edit distance algorithms<br/>
1. Levenshtein algorithm <br/>
2. Damerau-Levenshtein algorithm<br/>
3. Needleman-Wunch distance <br/>


Affine gap<br/>
11. Smith-Waterman algorithm-tbi<br/>


Heuristic based<br/>
21. Jaro<br/>
22. Jaro-Winkler algorithm


Token Based approach<br/>
31. Jaccard similarity<br/>
32. Cosine similarity<br/>
33. Q-gram cosine similarity

Hybrid approach<br/>
41. Soft Tf-idf - combination of cosine similarity and jaro-winkler method. <br/>
42. Mogne-Elkan - Jaro-winkler as inner similarity function <br/> 


Edit distance (s,t): The number of minimum edit operation (Insertion,Deletion,Substitution) to tranform s to t. Each operation are wieghted.<br/>

Affine gap: A+(B⋅L). A is the cost of opening the gap. B is the gap extension penality and L is the length of the gap. <br/>



|Algorithm| Applicability|
|---------|---------------|
|Jaro-winkler|works best for small words (First name or last name)|
|cosine similarity| words in the document has relations|
|Soft Tf-idf | handles tokens with smaller corrections|
|Monge-Eklan| consider best matching token for similarity test| 



Reference
1. Cohen, W., Ravikumar, P., & Fienberg, S. (2003, August). A comparison of string metrics for matching names and records. In Kdd workshop on data cleaning and object consolidation (Vol. 3, pp. 73-78).<br/>
2. Naumann, F., & Herschel, M. (2010). An introduction to duplicate detection. Synthesis Lectures on Data Management, 2(1), 1-87.<br/>
3. A. K. Elmagarmid, P. G. Ipeirotis, and V. S. Verykios, “Duplicate record detection: A survey,”
Knowledge and Data Engineering, IEEE Transactions on, vol. 19, no. 1, pp. 1–16, 2007.

