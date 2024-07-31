import todo_list
import behave

@given("the to-do list is empty")
def step_impl(context):
    todo_list.limpiar_tareas(todo_list.tareas)

@when("the user adds a task 'Do homework'")
def step_impl(context):
    todo_list.agregar_tarea(todo_list.tareas,'Do homework')

@then("the to-do list should contain 'Do homework'")
def step_impl(context):
    task ='Do homework'
    assert task in todo_list.tareas, f'Task "{task}" not found in the to-do list' 

@given("the to-do list contains tasks")
def step_impl(context):
    todo_list.agregar_tarea(todo_list.tareas,"Finish the workshop")
    todo_list.agregar_tarea(todo_list.tareas,"Do homework")

@when("the user list all tasks")
def step_impl(context):
    todo_list.listar_tareas(todo_list.tareas)

@then("the output should contain")
def step_impl(context):
    tasks = ["Finish the workshop","Do homework"]
    testSet = set(tasks)
    codeSet = set(todo_list.tareas.keys())
    assert testSet.issubset(codeSet), f'The todo-list doesnt contains the taks' 

@given("the to-do list contains task Do homework")
def step_impl(context):
    todo_list.limpiar_tareas(todo_list.tareas)
    todo_list.agregar_tarea(todo_list.tareas,"Do homework")

@when("the user marks task 'Do homework' as completed")
def step_impl(context):
    todo_list.marcar_completada(todo_list.tareas,"Do homework")

@then("the to-do list should show task 'Do homework' as completed")
def step_impl(context):
    status = todo_list.tareas["Do homework"]
    assert status, f'The task is not marked as completed' 

@given("the to-do list contains task Finish the workshop")
def step_impl(context):
    todo_list.limpiar_tareas(todo_list.tareas)
    todo_list.agregar_tarea(todo_list.tareas,"Finish the workshop")

@when("the user clears the to-do list")
def step_impl(context):
    todo_list.limpiar_tareas(todo_list.tareas)

@then("the to-do list should be empty")
def step_impl(context):
    isEmpty = len(todo_list.tareas) == 0
    assert isEmpty, f'The to-do list is not empty' 

@given("the to-do list has no tasks")
def step_impl(context):
    todo_list.limpiar_tareas(todo_list.tareas)

@when("the user adds a task 'test code'")
def step_impl(context):
    todo_list.agregar_tarea(todo_list.tareas,"test code")
    todo_list.guardar_tareas()

@then("the to-do list gets serialized")
def step_impl(context):
    tasks = cargar_tareas()
    isNotEmpy = len(tasks)>0
    assert isNotEmpy, f'The to-do list is empty' 

