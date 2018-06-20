# Created by Nick Todd at 11/06/2018
Feature: Requesting a game review from a chat bot
  Provided with the name of the game and the platform the chatbot
  should respond with a rating

  Scenario Outline: Get a Quote

    Given the user enters 'I would like to get a quote'
    When asked for the make of car the user enters <make>
    And when asked for the model the user enters <model>
    And when asked for their date of birth te user enters <dob>
    And when asked for the date of passing their driving test the user enters <passdate>
    And when asked for the size of their cars engine te user enters <engine>
    And when prompted to confirm the user enters 'yes'
    Then the chatbot should respond with 'For driver <age> years of age who has been driving for <yearsdriving> years driving a <enginesize>litre engine, the cost of insurance will be approximately: £'

    Examples:
        | make      | model      | dob             | passdate     | engine | age | yearsdriving | enginesize |
        |  'Ford'   |  'Mondeo'  |  '01/01/1980'   | '01/01/2000' | '1'    | 38  | 18           | 1.0        |
        |  'Toyota' |  'Auris'   |  '1982'         | '01/01/2000' | '1'    | 36  | 18           | 1.0        |
        |  'Renault'|  'Clio'    |  '01/01/1980'   | '2010'       | '1'    | 38  | 8            | 1.0        |
        |  'Audi'   |  'Quattro' |  '1980'         | '2010'       | '3.0'  | 38  | 8            | 3.0        |
        |  'Audi'   |  'Quattro' |  'February 1980'| 'July 2010'  | '3.0'  | 38  | 8            | 3.0        |
    
