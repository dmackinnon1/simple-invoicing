import csv, sys

#Reads in CSV <file>.csv with headers:
# date,part,is_daily,hours,rate,charge,description
# if is_daily then export tex table to <file>_daily.tex AND <file>_days.csv
# if not is_daily then export tex table to <file>_others.txt
# The <file>_invoice.tex combines these into an invoice.

fbase = sys.argv[1]
fcsv = fbase + '.csv'
dcsv_file = open('./target/days.csv', 'w')
dcsv_file.write("DATE, STAT" + '\n')

dtex_file = open('./target/days.tex', 'w')
otex_file = open('./target/other.tex', 'w')

dtex_file.write('\\begin{tabular}{ l c c} \n')
dtex_file.write('\\toprule \\textbf{Day} & \\textbf{Hours} & \\textbf{Amount} \\\\ \\midrule \n')

otex_file.write('\\begin{tabular}{ l l c } \n')
otex_file.write('\\toprule \\textbf{Item} & \\textbf{Description} & \\textbf{Amount} \\\\ \\midrule \n')

dtotal = 0;
ototal = 0;

with open(fcsv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            #print(row[0])
            if row[2] == 'TRUE':
                dcsv_file.write(row[0] +"," + row[1]+ '\n')
                dtex_file.write(row[0] + " & " + row[3] + " & \\$" + row[5] + '\\\\ \n')
                dtotal += float(row[5])
            else:
                otex_file.write(row[0] +  " & " +row[6] + " & \\$" + row[5] + '\\\\ \n')
                ototal += float(row[5])
        line_count += 1

dtex_file.write("\\midrule \n \\textbf{Total} & &\\$" + str(dtotal) + "\\\\ \n")        
dtex_file.write("\\bottomrule \n \\end{tabular}")
dtex_file.close()

otex_file.write("\\midrule \n \\textbf{Total} & \\$" + str(ototal) + "\\\\ \n" )        
otex_file.write("\\bottomrule \n \\end{tabular}")
otex_file.close()
dcsv_file.close()

total_file = open('./target/' + 'total.tex', 'w')
total_file.write("\\bigskip \n\\\\ \n\\bigskip \n\\Large{\\textbf{Total: \\theCurrency \\$}" + str(dtotal + ototal) + "} \n")
total_file.write("\n %\\includegraphics[scale=1]{receipts.pdf} %%uncomment and modify for receipts")

total_file.close()

with open('./target/main.tex','w') as outfile:
        with open('top.tex') as infile:
            outfile.write(infile.read())
        outfile.write("\n\\InvoiceMonth{" + fbase + "} \n")
        with open('bottom.tex') as infile:
            outfile.write(infile.read())    