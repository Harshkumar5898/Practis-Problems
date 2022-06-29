def MatchScore(Sentence1, Sentence2):
    words1 = Sentence1.split(" ")
    words2 = Sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1 == word2:
                score += 1

    return score


if __name__ == '__main__':
    Sentences = ["python is cool", "python is good",
                 "python is not python snake"]
    Search = input("  -  Search  -  \n      ").lower()
    Score = []
    for item in Sentences:
        Score.append(MatchScore(Search, item))

    SentenceScore = sorted(zip(Score, Sentences), reverse=True)
    sr = 1
    print(f"About {len(SentenceScore)} results found")
    for score, item in SentenceScore:
        print(f" - {sr}. {item}")
        sr += 1
