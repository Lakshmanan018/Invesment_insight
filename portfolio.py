def get_portfolio(risk):

    if risk == "Conservative":
        return {
            "Fixed Deposit":40,
            "Government Bonds":30,
            "Debt Funds":20,
            "Gold":10
        }

    if risk == "Moderate":
        return {
            "Large Cap Funds":40,
            "Index Funds":25,
            "Bonds":20,
            "Gold":10,
            "Cash":5
        }

    return {
        "Stocks":60,
        "Mutual Funds":20,
        "ETFs":10,
        "Gold":5,
        "Cash":5
    }
