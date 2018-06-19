# Created by Nick Todd at 11/06/2018
Feature: Requesting a game review from a chat bot
  Provided with the name of the game and the platform the chatbot
  should respond with a rating

  Scenario: Get a Rating for Minecraft

    Given the user enters 'I would like to review a game'
    When asked for the game title the user enters 'minecraft'
    And when asked for the game platform the user enters 'pc'
    And when prompted to confirm the user enters 'yes'
    Then the chatbot should respond with 'According to metacritic, minecraft is rated: 93%'


  Scenario: Get a Rating for Fortnite

    Given the user enters 'I would like to review a game'
    When asked for the game title the user enters 'fortnite'
    And when asked for the game platform the user enters 'pc'
    And when prompted to confirm the user enters 'yes'
    Then the chatbot should respond with 'According to metacritic, fortnite is rated: 79%'
