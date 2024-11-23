# unix-strings-recreation
This program takes in a filename, encoding type (default to UTF-8), and threshold (default 4)  
It implements the unix command "strings"  
It prints out every string encoded with the given encoding that is equal to or longer than the given threshold

## Files
strings.py contains the code for this program  
All other files are test files for testing.  
 * .s files are UTF-8 encoding  
 * .le files are little endian encoding  
 * .be files are big endian encoding  
 * Task2.png can be used in any encoding to test the handling of a long file

## Options
-e  Encoding  
 * s = UTF-8  
 * l = UTF-16 little endian  
 * b = UTF-16 big endian

-n  Word length threshold. Must be positive integer.

## Running
> python strings.py -e={encoding} -n={min word length} {file}  
> python strings.py -e=s -n=8 s.s
