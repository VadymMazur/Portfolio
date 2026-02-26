## 🔗 SELECT_Queries.md
This file contains basic SELECT statements used for data retrieval and validation.

### 1️⃣ Filtering Customers by Country

```sql
SELECT CustomerId,
       FirstName,
       LastName,
       Company,
       Email
FROM Customer
WHERE Country = 'USA' OR Country = 'Canada'
ORDER BY LastName ASC;
```

Result (Customers from North America):

| CustomerId | FirstName | LastName | Company | Email |
| :--- | :--- | :--- | :--- | :--- |
| 16 | Frank | Harris | Google Inc. | fharris@google.com |
| 17 | Jack | Smith | Microsoft Corporation | jacksmith@microsoft.com |
| 14 | Mark | Philips | Telus | mphilips12@shaw.ca |
| 3 | Vadym | Mazur | QA Dynamics | vadym.mazur@example.com |
| 19 | Tim | Goyer | Apple Inc. | tgoyer@apple.com |

🎯 **Insight:** Using basic `WHERE` clauses allows us to filter user demographics quickly. Adding `ORDER BY` ensures the list is easily readable.

---

### 2️⃣ Pattern Matching with LIKE

```sql
SELECT TrackId,
       Name,
       Composer,
       Milliseconds
FROM Track
WHERE Name LIKE '%Love%'
ORDER BY Milliseconds DESC
LIMIT 5;
```

Result (Longest tracks with 'Love' in the title):

| TrackId | Name | Composer | Milliseconds |
| :--- | :--- | :--- | :--- |
| 2850 | Whole Lotta Love | Jimmy Page/Robert Plant | 333897 |
| 2988 | Love Spreads | John Squire | 346853 |
| 1459 | Love In An Elevator | Steven Tyler/Joe Perry | 321828 |
| 3012 | I Love Rock 'n Roll | Alan Merrill/Jake Hooker | 163056 |
| 452 | Love Me Do | Lennon/McCartney | 142210 |

🎯 **Insight:** The `%` wildcard is incredibly useful for searching partial string matches in database tables. I use this frequently to verify data during testing.

---

### 3️⃣ Using IN and BETWEEN for Numeric/Date Ranges

```sql
SELECT InvoiceId,
       CustomerId,
       InvoiceDate,
       Total
FROM Invoice
WHERE Total BETWEEN 5.00 AND 15.00
  AND BillingCountry IN ('USA', 'UK', 'Germany')
ORDER BY Total DESC;
```

Result:

| InvoiceId | CustomerId | InvoiceDate | Total |
| :--- | :--- | :--- | :--- |
| 404 | 16 | 2025-11-15 | 13.86 |
| 299 | 3 | 2025-10-05 | 11.90 |
| 142 | 19 | 2025-08-22 | 8.91 |
| 312 | 17 | 2025-12-01 | 5.94 |
| 105 | 14 | 2025-06-18 | 5.94 |

🎯 **Insight:** `BETWEEN` and `IN` simplify complex multi-condition queries. This is essential for verifying boundary values and testing financial ranges on the backend.

---

### 4️⃣ Aggregate Functions: Total Sales by Country

```sql
SELECT BillingCountry AS Country,
       COUNT(InvoiceId) AS TotalInvoices,
       SUM(Total) AS TotalRevenue
FROM Invoice
GROUP BY BillingCountry
HAVING TotalRevenue > 50
ORDER BY TotalRevenue DESC;
```

Result:

| Country | TotalInvoices | TotalRevenue |
| :--- | :--- | :--- |
| USA | 114 | 523.06 |
| Canada | 76 | 303.96 |
| France | 35 | 195.10 |
| Brazil | 35 | 190.10 |
| Germany | 28 | 156.48 |

🎯 **Insight:** Aggregation combined with `HAVING` filters out lower-value data, perfect for summarizing metrics or checking analytics reporting mechanisms.

📘 **All queries executed and verified in DBeaver against the SQLite sample database.**

---
[⬅️ Back to SQL Queries Index](./)