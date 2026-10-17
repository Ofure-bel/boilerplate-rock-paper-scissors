# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(last_opp_move, opp_history=[]):
    #Store learned behaviour patterns, similar to a training dataset
    if not hasattr(player, "learned_patterns"):
        player.learned_patterns ={}

    #My winning strategy
    winning_strategy = {
        "R": "P",
        "P": "S",
        "S": "R"
    }
    #Store my opponent's move
    if last_opp_move:
        opp_history.append(last_opp_move)

    #Wait until enough history is collected and create a feture from recent moves
    if len(opp_history) < 5:
        return "R"
    pattern = "".join(opp_history[-3:])

    #My program will learn what happens after this pattern
    if len(opp_history) >= 4:
        previous_pattern = "".join(opp_history[-4:-1])
        next_move = opp_history[-1]
        if previous_pattern not in player.learned_patterns:
            player.learned_patterns[previous_pattern] = []

        player.learned_patterns[previous_pattern].append(next_move)

    #Predict my opp's next move
    prediction = None
    if pattern in player.learned_patterns:
        prediction = max(set(player.learned_patterns[pattern]), key = player.learned_patterns[pattern].count)

    #if there's no pattern seen, use a frequency
    if prediction is None:
        prediction = max(set(opp_history), key = opp_history.count)

    #Make final decision
    return winning_strategy[prediction]
