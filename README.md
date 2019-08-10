# ExceptionCreation
It contains three python file which deal with the exception handling and write those exceptions into a text file.

result.txt file is a log file where the exceptions are stored whenever they occur.

exception_file.py contains a class named Exceptions which consists of four functions for four different exceptions and writes them into 
result.txt file with the timestamp

random_file1.py contains a class named random which checks for four different exceptions an interactive way and send the corresponding tracebacks
to the functions from exception_file.py file.

reading_from_log.py will read the result.txt file and give output in a proper format.

Note - I am stuck in a problem suppose when the result.txt file is tried to open in the exception_file.py and it is not opened, so I need
to write the exception as log in windows event viewer. I am unable to do that.If anybody finds out the way of doing it pls send feedback.
