##Parser tool to extract events tabulated in interrogation reports downloaded from PDMS as PDF files 
##Requires Python>=3.8
##Requires pandas, pdfminer.six and PyPDF2 installed

#Import standard libraries
import pandas as pd
import numpy as np
import os
import pathlib
import pdfminer
from pdfminer.high_level import extract_text
from PyPDF2 import PdfFileMerger
from datetime import datetime
import pathlib

#Import custom functions
from ParserTools import GetFilePaths, MergeFiles, RunParser

#User-specified inputs (Modify accoding to your study)
patient_id = '' #Defined by your study
start, stop = 'YYYYMMDD_HHMM', 'YYYYMMDD_HHMM' #Date and time of period you will tabulate
INDIR = '/path/to/interrogation/reports/pdf/files/' 
OUTDIR = '/path/to/save/output/file'

#Main code (Do not modify)
fn_merged = f'{patient_id}_{start}-{stop}_merged.pdf'
fn_parsed = f'{patient_id}_{start}-{stop}_parsed.csv'

input_files = GetFilePaths(INDIR, 'pdf')
master_file_path = MergeFiles(OUTDIR, input_files, fn_merged)

tabulated_data = RunParser(master_file_path)
##save new dataframe as csv file
tabulated_data.to_csv(pathlib.Path(OUTDIR, fn_parsed))

## END OF CODE ##

