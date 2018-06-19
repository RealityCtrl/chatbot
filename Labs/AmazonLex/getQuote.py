from time import gmtime, strftime
import math


def lambda_handler(event, context):
    slots = event['currentIntent']['slots']

    make = slots['CarMake']
    model = slots['CarModel']
    engine = slots['EngineSize']
    DoB = slots['DateOfBirth']
    passDate = slots['PassDate']

    DoB = DoB.split('-')
    passDate = passDate.split('-')
    currentDate = strftime("%Y-%m-%d", gmtime()).split('-')

    approxAge = int(currentDate[0]) - int(DoB[0])
    approxYearsPassed = int(currentDate[0]) - int(passDate[0])
    engine = float(engine)

    quote = Quote(approxAge, engine, approxYearsPassed)
    speech = 'For driver ' + str(approxAge) + ' years of age who has been driving for ' + str(
        approxYearsPassed) + ' years driving a ' + str(
        engine) + 'litre engine, the cost of insurance will be approximately: £' + str(quote)

    response = {"dialogAction": {
        "type": "Close",
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": speech
        }}}

    return response


def Quote(age, engineSize, yearsPassed):
    return round(50 + engineSize / (yearsPassed + 1) * math.exp(-(age - 94) / 10))