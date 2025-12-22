'''
Now logger is for the purpose that any execution that probably happens, we should be able to, uh,

log all those information, the execution, everything in some files so that we'll be able to track

if there is some errors, even the custom exception error, we will try to, um, you know, any exception

that basically comes will try to log that into the text file.
'''

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''
So my file name fail file name that will be created will be whatever date time is basically coming.

And further this will basically have month day year hours.'''

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
'''So whatever logs will get created it will be with respect to the current working directory.

So here only logs folder will get created and every file will start with logs.

Along with this whatever file name is basically coming okay.'''
os.makedirs(logs_path,exist_ok=True)
'''
So this basically says that even though there is a file even though there is a folder, keep on appending

the files inside that whenever we want to create the file.'''
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
'''
This is with respect to the logging setup okay.

That basically means now wherever I use logging.info import logging and logging.info.

And uh probably I write out any print message.

Then it is going to use this kind of basic config and it is going to create this file path.

It is basically going to keep this particular format with respect to the message and all that we are

going to get.'''


'''
Now, what I will do is that whenever we get an exception, I will take that exception.

Logging it with a logger file and use logging logging.info to put it inside the file.

Right.

So such way we will be able to get that particular folder also perfect.'''

