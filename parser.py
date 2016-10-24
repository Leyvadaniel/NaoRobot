"""String parsing and matching utilities.

Functions:
parse -- parse lines in exercise file and return wrong line or None.
"""


def parse(fileToParse, linesToParse, stringsToParse):
    """parse lines in exercise file, match list and return line differences.

    Keyword arguments
    fileToParse -- the complete path to the filename to parse.
    linesToParse -- a list of line numbers to parse and check.
    stringsToParse -- a list of the values that linesToParse must match.
    """
    fileText = open(fileToParse).readlines()

    for lineToParse, stringToParse in zip(linesToParse, stringsToParse):
        stringToParse = stringToParse.replace(' ', '')
        stringToParse = stringToParse.replace('\n', '')

        stringParsed = fileText[lineToParse-1]
        stringParsed = stringParsed.replace('\n', '')
        stringParsed = stringParsed.replace(' ', '')

        # If a line to check differs, return its line number
        if(stringParsed != stringToParse):
            return lineToParse

    # Reached if all lines match
    return None
