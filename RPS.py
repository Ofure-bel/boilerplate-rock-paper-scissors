def player(prev_play, opp_history=[]):
    if not hasattr(player, "models"):
        player.models = {2: {}, 3: {}, 4: {}}
        player.my_history = []

    counter = {"R": "P", "P": "S", "S": "R"}

    #Start fresh when a new game begins
    if prev_play == "":
        opp_history.clear()
        player.models = {2: {}, 3: {}, 4: {}}
        player.my_history = []

    #Keep track of the opponent's moves and learn their patterns
    if prev_play:
        for size in (2, 3, 4):
            if len(opp_history) >= size:
                pattern = "".join(opp_history[-size:])

                if pattern not in player.models[size]:
                    player.models[size][pattern] = {"R": 0, "P": 0, "S": 0}
                player.models[size][pattern][prev_play] += 1

        opp_history.append(prev_play)

    #Use different moves at the beginning
    if len(opp_history) < 5:
        move = ["R", "P", "S"][len(opp_history) % 3]
        player.my_history.append(move)
        return move

    scores = {"R": 0, "P": 0, "S": 0}

    #Use past patterns to guess the opponent's next move
    for size in (4, 3, 2):
        if len(opp_history) >= size:
            pattern = "".join(opp_history[-size:])
            counts = player.models[size].get(pattern, {})
            total = sum(counts.values())

            if total >= 2:
                prediction = max(counts, key=counts.get)
                confidence = counts[prediction] / total

                if confidence >= 0.5:
                    scores[prediction] += size * confidence

    #Check which move the opponent uses most often
    recent = opp_history[-20:]

    for move in ("R", "P", "S"):
        scores[move] += 0.25 * recent.count(move)

    prediction = max(scores, key=scores.get)
    move = counter[prediction]

    player.my_history.append(move)
    return move
