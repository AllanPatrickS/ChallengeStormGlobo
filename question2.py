# Esta questão está assumindo que as produções são apenas recursivas

op_bracket = ["{", "[", "("]
close_bracket = ["}", "]", ")"]

def question2(word):
    if len(word) % 2 != 0:
        return "Nao"
    for pos in range(int(len(word)/2)):
        if op_bracket.index(word[pos]) != close_bracket.index(word[len(word) - 1 - pos]):
            return "Nao"
    return "Sim"

if __name__ == '__main__':
    print("Palavra: %s resultado %s" % ("{[()]}", question2("{[()]}")))
    print("Palavra: %s resultado %s" % ("{[(])}", question2("{[(])}")))
    print("Palavra: %s resultado %s" % ("{{[[(())]]}}", question2("{{[[(())]]}}")))
