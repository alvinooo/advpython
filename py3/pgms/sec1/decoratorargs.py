#!/usr/bin/env python3
# decoratorargs.py - decorator arguments

handlers = {}
def eventHandler(event): 
    def register(func):
        handlers[event] = func
        return func
    return register

@eventHandler("BUTTON")
def buttonHandler(msg):
    print(msg)

# implemented as: 
#    temp = eventHandler("BUTTON")
#    buttonHandler = temp(buttonHandler)

@eventHandler("CHECKBOX")
def checkboxHandler(msg):
    print(msg)

# implemented as: 
#    temp = eventHandler("CHECKBOX")
#    checkboxHandler = temp(checkboxHandler)

buttonHandler("button clicked")
checkboxHandler("checkbox checked")
print(handlers)

#####################################
#
#     $ decoratorargs.py
#     button clicked
#     checkbox checked
#     {'BUTTON': <function buttonHandler at 0x9d3e374>, 
#     'CHECKBOX': <function checkboxHandler at 0x9d3e6f4>}
#      
