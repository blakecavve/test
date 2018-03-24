#!/usr/bin/env python
# encoding: utf-8
"""
scoreRecall.py

Convert firebase json output into free recall scored output

"""

import json
import csv
import sys
from pprint import pprint

def main(argv=None):

    if (len(sys.argv) != 3):
        print "Please specify input and output file names"
        return 0

    inputFileName = sys.argv[1]
    outputFileName = sys.argv[2]

    with open(inputFileName) as json_data:
        data = json.load(json_data)

    # get output file ready
    test_file = open(outputFileName,'wb')
    csvwriter = csv.writer(test_file)

    csvwriter.writerow(["ID","blockNumber","scenario", "aord", "setSide","choice",
        "unified", "sCompar", "mCompar","rt","choice_number","key_press"])

    for subj in data.keys():

        ID = subj

        trialKeys = data[subj].keys()
        trialids = []

        for tt in trialKeys:

            if data[subj][tt]["trial_type"]=="single-stim":

                row = data[subj][tt]

                print(data[subj][tt])

                toWrite = [ID, row["blockNumber"], row["scenario"], row["aord"], row["setSide"]]

                choice = 0 # non-positional choice
                setSide = row["setSide"]
                key_press = row["key_press"]
                if (setSide==False and key_press==37) or (setSide and key_press==39):
                    choice = 1

                toWrite.append(choice)
                toWrite.append(row["unified"])
                toWrite.append(row["sCompar"])
                toWrite.append(row["mCompar"])

                toWrite.append(row["rt"])
                toWrite.append(row["trialNumber"])
                toWrite.append(row["key_press"])

                csvwriter.writerow(toWrite)

    test_file.close()


if __name__ == "__main__":
    sys.exit(main())
