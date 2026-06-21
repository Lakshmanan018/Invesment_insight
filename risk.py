def get_risk_score(risk):

    scores = {
        "Conservative":3,
        "Moderate":6,
        "Aggressive":9
    }

    return scores[risk]
