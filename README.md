# entity_resolution_spark
Collection of some algorithms for entity resolution.

Character and Edit distance algorithms
1. Levenshtein algorithm
2. Damerau-Levenshtein algorithm
3. Needleman-Wunch distance 

Affine gap
11. Smith-Waterman algorithm

Heuristic based
21. Jaro
22. Jaro-Winkler algorithm


Token Based approach
31. Jaccard similarity
32. Cosine similarity
33. Q-gram cosine similarity

Hybrid approach
41. Soft Tf-idf - combination of cosine similarity and jaro-winkler method.
42. Mogne-Elkan - edit distance and affine gap 


Edit distance (s,t): The number of minimum edit operation (Insertion,Deletion,Substitution) to tranform s to t. Each operation are wieghted.

Affine gap: A+(B⋅L). A is the cost of opening the gap. B is the gap extension penality and L is the length of the gap.
|Algorithm| Applicability|
|---------|---------------|
|Jaro-winkler|works best for small words (First name or last name)|
|cosine similarity| words in the document has relations|
|Soft Tf-idf | handles tokens with smaller correctios|



Reference
1. Cohen, W., Ravikumar, P., & Fienberg, S. (2003, August). A comparison of string metrics for matching names and records. In Kdd workshop on data cleaning and object consolidation (Vol. 3, pp. 73-78).
2. Naumann, F., & Herschel, M. (2010). An introduction to duplicate detection. Synthesis Lectures on Data Management, 2(1), 1-87.
3. A. K. Elmagarmid, P. G. Ipeirotis, and V. S. Verykios, “Duplicate record detection: A survey,”
Knowledge and Data Engineering, IEEE Transactions on, vol. 19, no. 1, pp. 1–16, 2007.

