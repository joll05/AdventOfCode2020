import re

f=open("input.txt")
Input=f.read().split("\n")
f.close()

accumulator = 0
position = 0
nextInstructionOffset = 1

def acc(arg):
    global accumulator
    accumulator += arg

def jmp(arg):
    global nextInstructionOffset
    nextInstructionOffset = arg

def nop(arg):
    pass

instructions = {"acc": acc, "jmp": jmp, "nop": nop}

instructionRegex = r"^(.{3}) ((\+|-)\d+)$"
def ParseInstruction(instruction):
    match = re.match(instructionRegex, instruction)
    return (match.group(1), int(match.group(2)))

code = [ParseInstruction(i) for i in Input]

visitedInstructions = []

while 0 <= position < len(code):
    visitedInstructions += [position]
    currentInstruction = code[position]
    instructions[currentInstruction[0]](currentInstruction[1])
    position += nextInstructionOffset
    nextInstructionOffset = 1
    if(position in visitedInstructions): break

print(accumulator)
