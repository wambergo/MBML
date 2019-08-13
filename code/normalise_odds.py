def normalise_odds(PSCH, PSCD, PSCA):
    """
    Normalise odds to probabilities by odds margin.
    margin weights in proportion to the size of the odds

    """
    probs = [1. / odds for odds in (PSCH, PSCD, PSCA)]
    margin = sum(probs)-1.
    trueo = [1./(3.* odds/(3.-margin*odds)) for odds in (PSCH, PSCD, PSCA)]
    
    return trueo

odds_columns = ['PSCH', 'PSCD', 'PSCA']

probabilities = df[odds_columns].apply(lambda row: normalise_odds(**row), axis=1)
cols = list(['home_win_prob','draw','away_win_prob'])
probabilities = pd.DataFrame(probabilities.values.tolist(), columns=cols)

df = df.merge(
    probabilities,
    left_index=True,
    right_index=True,
    suffixes=['', '_prob']
)
