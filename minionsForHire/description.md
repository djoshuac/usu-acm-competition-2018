# Minions Data Entry

The minions are great and providing consistent manual labor, however Gru has found that they are often less than adequate
in filling their data entry duty's. In order for Gru to maintain his full workforce he must keep his data stores clean and
tidy. 

Write a program to help Gru validate that the minions are performing correctly.

The data is stored in a XML format, make sure that the xml is valid (meaning each open tag < tag > has a closing tag </ tag>).
There is also some specific data that Gru wants to validate:
* if a tag is a < phone> tag make sure that the only value inside is a phone number in the format 555-555-5555
* if a tag is an < email> make sure that it is a valid email meaning before the @ it only contains letters, numbers, and _
and after the @ it contains only letters and a period followed by 2-3 letters for domain name.

### Input

The first line will be a number *n* of how many lines exist in the xml data set. The following *n* lines will be the 
xml to check. XML may or may not be formated properly (meaning multiple tags may exist on the same line see sample 2)

### Output

The output will be a single True if all data is correct, or False if data is incorrect