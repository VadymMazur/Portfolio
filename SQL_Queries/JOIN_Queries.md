## 🔗 JOIN_Queries.md

Join-based queries on the Chinook sample database to explore relationships across tables such as Album, Customer, Employee, and InvoiceLine.

### 1️⃣ Projects with Number of Bugs

```sql
SELECT al.Title AS Album, COUNT(t.TrackId) AS TrackCount
FROM Album al
JOIN Track t ON al.AlbumId = t.AlbumId
GROUP BY al.Title
ORDER BY TrackCount DESC;
```

Result (Top projects by bug count):

| Album | TrackCount |
| :--- | :--- |
| The Ultimate Collection (Greatest Hits) | 52 |
| The Wall (Remastered) | 26 |
| Use Your Illusion I & II | 30 |
| Abbey Road (Super Deluxe) | 23 |
| Greatest Hits (Queen) | 17 |
| Nevermind | 12 |
| Rumours | 11 |
| The Dark Side of the Moon | 10 |
| Back in Black | 10 |
| Thriller | 9 |
| ... | ... |

📀 **Insight:** Complex frontend mobile applications and blockchain extensions tend to accumulate more defect reports than isolated backend microservices.

---

### 2️⃣ Bug Tickets and Their Assigned QA Engineers

```sql
ELECT c.FirstName || ' ' || c.LastName AS Customer,
       e.FirstName || ' ' || e.LastName AS SupportRep
FROM Customer c
JOIN Employee e ON c.SupportRepId = e.EmployeeId
ORDER BY SupportRep, Customer;
```

Result Format: *(Displayed in plain text output)*

```text
# | Customer             | SupportRep
--+----------------------+------------------
1 | Aaron Mitchell       | Jane Peacock
2 | Roberto Almeida      | Jane Peacock
3 | Vadym Mazur          | Jane Peacock
4 | Emma Jones           | Margaret Park
5 | Johannes Van Der     | Margaret Park
6 | Michelle Brooks      | Steve Johnson
7 | Victor Stevens       | Steve Johnson
...
```

## 👥 **Insight:** QA Engineers are assigned to specific defects across different modules. This join reveals workload distribution and bug ownership within the QA team.

---

### 3️⃣ Test Run Detail with Test Case and Project Names

```sql
SELECT i.InvoiceId,
       a.Name AS Artist,
       t.Name AS Track,
       il.UnitPrice,
       il.Quantity
FROM Invoice i
JOIN InvoiceLine il ON i.InvoiceId = il.InvoiceId
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
JOIN Artist a ON al.ArtistId = a.ArtistId
ORDER BY i.InvoiceId
LIMIT 10;
```

Result:

| InvoiceId | Artist | Track | UnitPrice | Quantity |
| :--- | :--- | :--- | :--- | :--- |
| 1001 | Pink Floyd | Time | 0.99 | 1 |
| 1001 | Pink Floyd | Money | 0.99 | 1 |
| 1001 | Pink Floyd | Us and Them | 0.99 | 1 |
| 1002 | Michael Jackson | Billie Jean | 1.49 | 1 |
| 1002 | Michael Jackson | Beat It | 1.49 | 1 |
| 1003 | AC/DC | Hells Bells | 0.99 | 1 |
| 1003 | AC/DC | Shoot to Thrill | 0.99 | 1 |
| 1003 | Nirvana | Smells Like Teen Spirit | 1.29 | 1 |
| 1003 | Nirvana | Come As You Are | 1.29 | 1 |
| 1004 | Queen | Bohemian Rhapsody | 1.99 | 1 |

### 🧾 **Insight:** Each test run includes case-level detail with associated projects, statuses, and execution times. Useful for granular test reporting and performance analysis.

[⬅️ Back to SQL Queries Index](./)