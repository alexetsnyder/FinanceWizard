#FinWizHelperFunc

def input_to_list(cleanInput):
	inputList = cleanInput.split()
	arg_list = []
	index = 0
	while index < len(inputList):
		if inputList[index][0] == '\'' or inputList[index][0] == '\"':
			for j in range(index, len(inputList)):
				if inputList[j][-1] == '\'' or inputList[j][-1] == '\"':
					arg_list.append(' '.join(inputList[index:j+1])[1:-1])
					index = j + 1
					break
		else:
			arg_list.append(inputList[index])
			index += 1
	return arg_list
