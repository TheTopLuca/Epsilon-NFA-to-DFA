import argparse
import re



class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


class State :
    def __init__(self,name):
        self.name = name
        self.ec = []
        self. transitions = dict()
        self.isAcceptState = False


class NFA :
    def __init__(self):
        self.states = []
        self.startState = None
        self.acceptState = None
        self.alphabet = None
        #self.Alphabet = alphabet


    def findState(self ,name):
        for state in self.states:
            if(state.name == name):
                return state
        return  None

class DFAState :
    def __init__(self,name):
        self.name = name
        self.transitions = dict()
        self.states = None

def findEC(array):

    for item in array:
        epsilonClosure = item.ec
        for item2 in epsilonClosure:
            if(not array.__contains__(item2)):
                array.append(item2)
    return array

def findTransitions(array,alphabet):
    return 1

def addCommas(currentstring , stringToBeAdded):
    i = 0
    if(len(stringToBeAdded)==0):
        return currentstring

    while(i<len(stringToBeAdded)-1):
        currentstring = currentstring + str(stringToBeAdded[i]) + ","
        i=i+1
    currentstring = currentstring + str(stringToBeAdded[i]) + "\n"
    return  currentstring




def addCommas2(currentstring , stringToBeAdded):
    i = 0

    while(i<len(stringToBeAdded)-1):
        currentstring = currentstring + str(stringToBeAdded[i]) + ","
        i=i+1
    currentstring = currentstring + str(stringToBeAdded[i])
    return  currentstring




if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=True, description='Sample Commandline')

    parser.add_argument('--file', action="store", help="path of file to take as input", nargs="?",
                        metavar="file")

    args = parser.parse_args()

    print(args.file)


    output_file = open("task_2_2_result.txt","w+")

    with open(args.file,"r")as file :
        currentNFA = NFA()
        currentNFA.alphabet = []
        currentNFA.acceptState = []
        lineNumber = 0
        transitions = []
        stack = Stack()
        x = 1
        for line in file:
           field = ""
           for character in line:
               if(lineNumber>=4):
                   break
               if(lineNumber==0):

                   if(character.isalnum()):

                       field = field+character
                   elif (character ==","):
                       currentState = State(field)
                       stateX = currentNFA.findState(field)
                       if(stateX==None):
                          currentNFA.states.append(currentState)
                       field  = ""
                   elif (character == "\n"):
                       currentState = State(field)
                       stateX = currentNFA.findState(field)
                       if(stateX==None):
                          currentNFA.states.append(currentState)

                       field  = ""
                       lineNumber+=1
                       break


               if(lineNumber==1):
                    if(character.isalnum() or character==" "):
                         field = field + character
                    elif(character ==","):
                        currentNFA.alphabet.append(field)
                        field = ""
                    elif(character=="\n"):

                        currentNFA.alphabet.append(field)
                        lineNumber +=1
                        field=""
                        break

               if (lineNumber==2):
                  if(character.isalnum() or character==" "):
                         #print(character)
                         field = field + character
                  elif(character=="\n"):
                        lineNumber +=1
                        for state in currentNFA.states:
                            if state.name == field:
                                currentNFA.startState = state
                                break
                        break

               if(lineNumber==3):
                  if(character.isalnum() or character==" "):
                         #print(character)
                         field = field + character
                  elif(character==","):
                      for state in currentNFA.states:
                            if state.name == field:
                                state.isAcceptState = True
                                currentNFA.acceptState.append(state)
                      field = ""
                  elif(character=="\n"):
                        lineNumber +=1
                        for state in currentNFA.states:
                            if state.name == field:
                                state.isAcceptState = True
                                currentNFA.acceptState.append(state)
                        break
           if(lineNumber>=4):
               length = len(line)
               i = 0
               while (i<length-1):

                    field = ""
                    if(line[i]==")" and line[i+1]=="\n"):
                        lineNumber=0
                        if( not stack.items.__contains__(currentNFA)):
                          stack.push(currentNFA)
                        print(line[i] + " " + line[i+1])
                        currentNFA = NFA()
                        currentNFA.alphabet = []
                        currentNFA.acceptState = []
                        print("A New NFA is encountered")
                        break
                    if(line[i]=="("):
                        j = i+1
                        while not(line[j]==")"):
                           field = field + line[j]
                           
                           j=j+1
                        i=j
                        transitions.append(field)

                    field = ""
                    i+=1
               if( not stack.items.__contains__(currentNFA)):
                     stack.push(currentNFA)


        # Form the Transitions list for each state along with the epsilon closures
        for item in transitions:
            x = item.split(",")
            fromStateName = x[0].replace(" ","")
            character = x[1].replace(" ","")
            toStateName = x[2].replace(" ", "")
            fromState = currentNFA.findState(fromStateName)
            toState = currentNFA.findState(toStateName)
            if(character==""):
                fromState.ec.append(toState)
            else:

                fromState.transitions.update({character: toState})


        DFAStack = Stack()
        startState = currentNFA.startState
        ctr = 0
        array = findEC([currentNFA.startState])


        newState = DFAState(ctr)
        ctr +=1
        newState.states = array
        newState.transitions = dict()
        DFAStack.push(newState)
        DFAArray = []
        DFAArray.append(newState)
        xx = 0

        while(not DFAStack.isEmpty()):#not DFAStack.isEmpty()):
            currentDFAstate = DFAStack.pop()
            #print("The current State is :" )
            #print(currentDFAstate)
            alphabet = currentNFA.alphabet
            index = 0




            for char in alphabet:
                if(not char==" "):
                    transitions2 = []
                    for state in currentDFAstate.states:
                        stateTransitions = state.transitions
                        for index in stateTransitions:
                            if(index == char):
                                transitions2.append(stateTransitions[index])
                    transitions2 = findEC(transitions2)
                    newDFAstate = DFAState(ctr)
                    newDFAstate.states = transitions2 #The New DFA state has the same list of states as the one included in the transition from the old state that was popped
                    # alone with the epsilon closure of them

                    #Make old DFA state point to this new state with the character
                    #currentDFAstate.transitions.update({char:newDFAstate})
                    arr2 = []
                    for k in newDFAstate.states:
                             arr2.append(k.name)


                    flag = False
                    for item in DFAArray:
                         arr1 = []
                         for j in item.states:
                             arr1.append(j.name)
                         if(set(arr1)==set(arr2)):
                             #print("item was already found")
                             index = item
                             flag = True
                             break
                             xx+=1
                    if(flag==False):
                        currentDFAstate.transitions.update({char:newDFAstate})
                        ctr+=1
                        DFAStack.push(newDFAstate)
                        DFAArray.append(newDFAstate)
                        #print("item was pushed")
                    else:
                        currentDFAstate.transitions.update({char:index})
                        #print("item was already found")
 #DFAStack.push(newDFAstate)
#We need to make sure that the newly created DFA state is not included in the list of DFA states
            #if(xx>=6):
             #   break
        outputString = ""
        stateNames = []
        dfaAlphabet = []
        startState = DFAArray[0].name
        acceptStates = []
        allTransitions = []

        #loop for renaming the state to Dead if it's dead

        for item in DFAArray:
            isDead = True
            for item2 in item.transitions:
                if(not item.transitions[item2]==item):
                    isDead=False
            if isDead:
                item.name = "DEAD"


        for item in DFAArray:
            stateNames.append(item.name)
            for xxx in item.transitions:
                if(not dfaAlphabet.__contains__(xxx)):
                    dfaAlphabet.append(xxx)
                #print(xxx + " : " + str(item.transitions[xxx].name))
                allTransitions.append("(" + str(item.name) + "," + xxx + "," + str(item.transitions[xxx].name) + ")")

            for state in item.states:
                if(state.isAcceptState):
                    acceptStates.append(item.name)





            #print("Newline + \n")
        #print(DFAStack.items)
        outputString = addCommas(outputString,stateNames)
        outputString = addCommas(outputString,dfaAlphabet)
        outputString = outputString + str(startState) + "\n"
        if(len(acceptStates)==0):
            outputString = addCommas(outputString,"") + "\n"
        else :
              outputString = addCommas(outputString,acceptStates)
        outputString = addCommas2(outputString,allTransitions)
        output_file.write(outputString)


























