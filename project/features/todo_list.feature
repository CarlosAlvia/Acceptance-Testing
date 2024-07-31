#language: en

Feature:  Manage a todo list

    Scenario:  Add a task to the to-do list
        Given the to-do list is empty
        When the user adds a task 'Do homework'
        Then the to-do list should contain 'Do homework'

    Scenario:  List all tasks in the to-do list
        Given the to-do list contains tasks:
        | Task |
        | Finish the workshop |
        | Do homework |
        When the user list all tasks
        Then the output should contain:
        | Finish the workshop |
        | Do homework |

    Scenario: Mark a task as completed
        Given the to-do list contains tasks:
        | Task | Status |
        | Do homework | Pending |
        When the user marks task 'Do homework' as completed
        Then the to-do list should show task 'Do homework' as completed

    Scenario: Clear the entire to-do list
        Given the to-do list contains tasks:
        | Task |
        | Finish the workshop |
        | Do homework |
        When the user clears the to-do list
        Then the to-do list should be empty

    Scenario: The list is serialized after adding a task
        Given the to-do list has no tasks:
        When the user adds a task 'test code'
        Then the to-do list gets serialized


