def evaluate_document(document, rules):
    evaluation_results = {}
    for rule in rules:
        # Apply each rule to the document
        if rule.lower() in document.lower():
            evaluation_results[rule] = "pass"
        else:
            evaluation_results[rule] = "fail"
    return evaluation_results
