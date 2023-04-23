# IFIParse
---
A Python script to help individuals parse .csv reports from the CFD trading platform Capital.com.

The output from this script is tailored to the requirements set forth by the Slovene tax agency for reporting income from CFD trades __(DOH-IFI)__.

As a result, all trades are converted from USD to EUR based on the exchange rate posted by the Slovene National Bank on the day of the trade.

## How to use

```bash
python ifiparse.py [target_file]

# for example

python ifiparse.py trades_report.csv
```

<br>

## Output

```
-----------------------------------------------|
2021-12-21
Exchange rate on day: 1.1295
-----------------------------------------------|
CLOSE      NASDAQ 100 -0.10 14149.45 +2.10
OPEN       NASDAQ 100 +0.10 14128.46   |
CLOSE      NASDAQ 100 +0.10 14129.97 -1.50
OPEN SHORT NASDAQ 100 -0.10 14115.01   |
CLOSE      NASDAQ 100 +0.10 14145.20 +1.19
OPEN SHORT NASDAQ 100 -0.10 14157.06   |
CLOSE      NASDAQ 100 -0.08 14145.82 +0.80
CLOSE      NASDAQ 100 -0.02 14145.82 +0.20
OPEN       NASDAQ 100 +0.10 14135.81   |
CLOSE      NASDAQ 100 -0.10 14126.96 +0.60
OPEN       NASDAQ 100 +0.10 14120.94   |
CLOSE      NASDAQ 100 +0.13 14112.00 -15.97
OPEN SHORT NASDAQ 100 -0.13 13989.46   |
CLOSE      NASDAQ 100 -0.13 13983.00 +1.00
OPEN       NASDAQ 100 +0.13 13975.30   |
CLOSE      NASDAQ 100 -0.03 13964.76 +0.32
CLOSE      NASDAQ 100 -0.10 13964.76 +1.07
OPEN       NASDAQ 100 +0.13 13954.14   |
CLOSE      NASDAQ 100 -0.13 13981.14 +3.34
OPEN       NASDAQ 100 +0.13 13955.47   |
CLOSE      NASDAQ 100 -0.13 13998.58 +1.28
OPEN       NASDAQ 100 +0.13 13988.76   |
CLOSE      NASDAQ 100 +0.13 13983.36 +1.27
OPEN SHORT NASDAQ 100 -0.13 13993.09   |
CLOSE      NASDAQ 100 -0.10 13999.03 +1.07
CLOSE      NASDAQ 100 -0.01 13998.94 +0.11
CLOSE      NASDAQ 100 -0.01 13998.94 +0.11
OPEN       NASDAQ 100 +0.12 13988.31   |
-----------------------------------------------|
16 Trades   | 14 winners      |  2 losers      |
14.46 profit| and -17.47 losses                |
-----------------------------------------------|
Running P&L: -3.01
-----------------------------------------------|

```
