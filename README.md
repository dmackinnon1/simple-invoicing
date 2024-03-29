# simple-invoicing
Local scripts to produce LaTeX formatted invoices from provided csv files.


Provide a CSV file named YEAR-MONTH.csv in the same folder as invoice.py, where YEAR is four digit and MONTH is two digit. The
CSV file must have headers:

date,stat,is_daily,hours,rate,charge,description

- **date** is YEAR-MONTH-DAY
- **stat** is A,P,F for A=am, P=pm, and F=full, designating what part of the day was worked.
- **hours**, **rate**, and **charge** are floats, no dollar signs or commas.
- **description** is a short description of the invoice charge
- **is_daily** is TRUE for daily rate charge entries, FALSE for additional expenses

Running *python invoice.py YEAR-MONTH* will generate additional files in the *target* directory.
Zipping up the target directory and uploading it to Overleaf as a project will generate the invoice file.
> zip -r target target

The generated .tex files require further editing - information on the contractor should be put in main.tex. Depending on the number of entries, the font size may be adjusted between 10 and 12pt to fit everything on a single page. No other files should require
modification.




