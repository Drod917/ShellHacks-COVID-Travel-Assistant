
import json

def getKeywords(request)
    keywords = json.load(jsonify(reques))

    state = keywords[0]
    date = keywords[1]

    return state, date