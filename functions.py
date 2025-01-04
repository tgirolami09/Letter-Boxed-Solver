import os

class colors():
    GREEN = "\x1b[32m"
    RED = "\x1b[31m"
    RESET = "\x1b[39m"

def usablePath(path):
    scriptAbsolutePath = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(scriptAbsolutePath, path)

currentWords = []
result = []
def recur(remaining:int,currentlyUsedLetters:set[str],wordListByLetter:dict[str, list],lastLetter:str):
    """
    Recursively checks word combinations
    """
    global result,currentWords
    if remaining==0:
        if len(currentlyUsedLetters)==12:
            result.append(currentWords.copy())
        return None
    
    if len(currentlyUsedLetters)==12:
        return None
    
    for word in wordListByLetter[lastLetter]:
        currentWords.append(word)
        recur(remaining-1,currentlyUsedLetters.union(set(word)),wordListByLetter,word[-1])
        currentWords.pop()

def nWordSolution(amoutOfWords:int,wordList:list,wordListByLetter:dict[str, list]):
    """
    Returns a list of solutions with exactly amoutOfWords words in the solution
    """
    global result
    result.clear()
    if amoutOfWords<=0:
        return result
    
    if amoutOfWords>=4:
        return result
    
    for word in wordList:
        currentWords.append(word)
        recur(amoutOfWords-1,set(word),wordListByLetter,word[-1])
        currentWords.pop()

    return result

def minimalWordSolutions(valid_words,valid_words_by_first_letter):
    color = colors()
    for nbWords in range(2,4):
        solutions = nWordSolution(nbWords,valid_words,valid_words_by_first_letter)
        if len(solutions)!=0:
            print(f"Here are some solutions with {nbWords} words:")
            for solution in solutions:
                print(*solution,sep=color.GREEN+" and "+color.RESET)
            break

        else:
            print(f"Did not find any solutions with {nbWords} words")