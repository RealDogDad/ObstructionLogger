#D:\school-development\saas\ObstructionLogger\read-only.txt

import os
import sys
import logging
import logging.config
from timeit import default_timer as timer

"""
.. module:: a8_obstruction_logger
:platform: Unix, Windows
:synopsis: A small application demonstrating log levels in Python. Reads from a text file to determine metrics on the word 'imperdiet'. Writes a sentence to a file to determine metrics on the word 'imperdiet'.
.. moduleauthor:: Brandan Foster <brandan@getfoster.net>
"""
#--Globals--#
TGT_WORD = 'imperdiet'
TIME_IN_READ = 0
TIME_IN_WRITE = 0
#Log Configuration from an external config
logging.config.fileConfig('logging.conf')
log = logging.getLogger('obstructionLogger') # Client facing Messages

def openThis(path = './', op = 'r'):
    log.info("openThis Method Started")
    if (os.path.exists(path)):
        log.debug("Given Path: " + path)
        if (op == 'r'):
            log.debug("Given Operation: " + op)
            try:
                log.debug("Opening file: " + os.path.basename(path))
                file = open(path, op)
                log.info("Read Mode Timer Start")
                startRead = timer()
                log.debug("Opened file: " + str(file))
            except:
                log.critical("Invalid File Path")
            else:
                log.info("Reading File")
                print(countEmUp(file))
                file.close()
                TIME_IN_READ = timer() - startRead
                log.info("Elapsed Read Time: " + str(TIME_IN_READ) + " seconds")
        else:
            log.debug("Given Operation: " + op)
            try:
                log.debug("Opening file: " + os.path.basename(path))
                file = open(path, op)
                log.info("Write Mode Timer Start")
                startWrite = timer()
                log.debug("Opened file: " + str(file))
            except:
                log.critical("Invalid File Path")
            else:
                log.info("Writing to File")
                file.write(tempText(input("Enter sentence(s): ")))
                os.remove("temp.txt")
                file.close()
                TIME_IN_WRITE = timer() - startWrite
                log.info("Elapsed Write Time : " + str(TIME_IN_WRITE) + " seconds")
    log.info("openThis Method Complete")
    return
def tempText(sentences):
    log.info("tempText Method Started")
    tempFile = open('temp.txt', 'w')
    log.debug("Inserting '" + sentences + "' into file." )
    tempFile.write(sentences)
    tempFile.close()
    tempFile = open('temp.txt', 'r')
    countEmUp(tempFile)
    log.info("tempText Method Completed")
    return sentences

def prettyPrint():
    log.info("prettyPrint Method Started")
    path = os.path.abspath("D:\school-development\saas\ObstructionLogger\consoleapp.log")
    file = open(path, 'r')
    log.debug("Opening File: " + str(file))
    returnString = "---- Start Log ----    \n"
    for line in file:
        returnString += line + " \n"
    log.info("prettyPrint Method Completed")
    returnString += " \n ---- End Log ----"
    return returnString
    
def countEmUp(file):
    log.info("countEmUp Method Started")
    TGT_WORD = 'imperdiet'
    TOTAL_LINE_COUNT = 0
    TOTAL_WORD_COUNT = 0
    LINES_WITH_TGT_WORD = 0
    TGT_WORD_COUNT = 0
    log.debug("Looking for: " + TGT_WORD)
    for line in file:
        if(TGT_WORD in line):
            TOTAL_LINE_COUNT += 1
            LINES_WITH_TGT_WORD += 1
            for word in line.split():
                if(word.strip(".") == TGT_WORD):
                    TOTAL_WORD_COUNT += 1
                    TGT_WORD_COUNT += 1
                    log.debug("found " + str(TGT_WORD_COUNT) + " occurence(s)")
                else:
                    TOTAL_WORD_COUNT += 1
        else:                            
           TOTAL_LINE_COUNT += 1
    returnString = "Found " + str(TGT_WORD_COUNT) + " occurence(s) of the word: '" + str(TGT_WORD) + "' in " + str(LINES_WITH_TGT_WORD) + " out of " + str(TOTAL_LINE_COUNT) + " total lines and " + str(TOTAL_WORD_COUNT) + " total words."
    log.info(returnString)
    log.info("countEmUp Method Complete")
    return returnString

def main():
    log.info("Main Method Started")
    exit = "false"
    while (exit == "false"):
        print("Obstruction Logger")
        PATH = input("Enter path: ")
        OPERATION = input("r/w: ")
        if OPERATION in ['r', 'w']:
            openThis(PATH, OPERATION)
        else:
            log.error("Invalid Operation Parameter")
        metrics = input("Print Metrics? true/false: ")
        if (metrics.lower() == "true"):
            print(prettyPrint())
            exit = input("Exit? true/false: ").lower()
        else:
            exit = input("Exit? true/false: ").lower()
    log.info("Main Method Completed")
if __name__ == "__main__":
    log.info("Obstruction Logger Application Started")
    main()
    log.info("Obstruction Logger Application Completed")