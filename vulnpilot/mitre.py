    ### WRITE YOUR CODE BELOW THIS LINE ###
    # Start from an empty list so "no findings" naturally returns [].
    result = []

    # Load the lookup table once, not once per finding.
    with open(MAP_PATH) as f:
        table = json.load(f)

    for finding in findings:
        # .get() gives None for unknown types instead of crashing,
        # so we can skip those findings.
        entry = table.get(finding.finding_type)
        if entry is None:
            continue

        result.append({
            "finding_title": finding.title,
            "id": entry["id"],
            "name": entry["name"],
            "tactic": entry["tactic"],
        })
    ### WRITE YOUR CODE ABOVE THIS LINE ###
