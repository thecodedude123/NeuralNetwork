#This is my first neural network program in python so I wanted to make it from scratch to understand how a neural network works although, it is still mysterios.
#In computer vision, the input would be the grayscale value of the pixels so that you can use those inputs, put them through a layer and get the output.
#The weights give parameters, the program's a target number to calculate a probablistic value to show what should be the output for the given information.
# The bias gives the neuron an ability to be inactive so that if the bias number gets to the output layer, it can keep going with out error.

import random #This code adds in the random package so that the inputs are almost like a real neural network
a_decimal = random.randint(0,9) * 0.1
b_decimal = random.randint(0,9) * 0.1
c_decimal = random.randint(0,9) * 0.1
d_decimal = random.randint(0,9) * 0.1

a = random.randint(0,9) + a_decimal
b = random.randint(0,9) + b_decimal
c = random.randint(0,9) + c_decimal
d = random.randint(0,9) + d_decimal

inputsVector = [a,b,c,d] #input values for one layer of neurons

weightsMatrix = [ [-2.3 , -4.3 ,6.7 , -3.4]
             ,[-4.7 , 5.8 , 7.4 , -6.8]
             ,[-5.1 , 8.4 , -7.2 , 6.4]]

biases = [3.7, 2.6, 5.9]

output_layer = []
for neuronWeights, neuronBiases in zip(weightsMatrix,biases):
    neuronOut = 0
    for neuronInputs, weights in zip(inputsVector, neuronWeights):
        neuronOut += neuronInputs*weights
    neuronOut += neuronBiases
    output_layer.append(neuronOut)
    
#using the array values to get the output

print("Inputs:     ", inputsVector)
print("Outputs:    ", output_layer)
e = 2.71828
sigmoid = round(1/(1+e**(output_layer[0]+ output_layer[1]+ output_layer[2])))
if(sigmoid == 0):
    print("Animal in this picture is a cat")
        
else:
    print("Animal in this picture is a dog")
        
#display reults of the program



   
    
    

    
