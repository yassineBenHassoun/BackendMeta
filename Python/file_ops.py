import os
from pathlib import Path

def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except:
        print("Unable to locate file") 
    
    raise NotImplementedError()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
   
    listResult = [];
  
        
    try:
        with open(file_name, 'r') as file:
            r = file.read()
            listResult = r.split(" ")
            size = len(listResult)
            print('ok')
            
            if size == 1 : 
                if not listResult[0] == True:
                    return []
                    print(listResult)

    except:
        print("Unable to locate file") 
 

    raise NotImplementedError()



def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
  
    firstResult = ""
        
    if (file_contents): 
        toList = file_contents.split("\n")
        firstResult = toList[0]
    try :
        with open(output_filename,'w') as w: 
          return w.write(firstResult)
    except: 
        return print("we can't write in the file ")


    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    
    listResult = []
    getList = read_file_into_list(file_name)

    for x in range(0, len(getList), 2):
        listResult.append(getList[x])

    return listResult

    raise NotImplementedError()

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE
    
    result = []
    getList = read_file_into_list(file_name)
    l = len(getList)

    for i, e in reversed(list(enumerate(getList))):
        result.append(e)
   
    return result
    raise NotImplementedError()

'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''
def main():
    try:
      
      
         
        current_directory = os.getcwd()
       
        filename = current_directory + "/" + "sampletext.txt"
        print(filename)
        file_contents = read_file(filename)
        print(file_contents)
        print(read_file_into_list(filename))
        
        # write_first_line_to_file(file_contents, "online.txt")
        # print(read_even_numbered_lines(filename))
        # print(read_file_in_reverse(filename))
    except:
        print("")

if __name__ == "__main__":
    main()