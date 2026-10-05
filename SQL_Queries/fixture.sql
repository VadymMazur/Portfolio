-- Synthetic music-store fixture. Values in minor currency units (cents).
-- Deliberately lacks a Customer foreign key on Invoice to model a bad import.
CREATE TABLE Employee (EmployeeId INTEGER PRIMARY KEY, Name TEXT NOT NULL);
CREATE TABLE Customer (CustomerId INTEGER PRIMARY KEY, Name TEXT NOT NULL,
  Country TEXT NOT NULL, Email TEXT NOT NULL, SupportRepId INTEGER);
CREATE TABLE Album (AlbumId INTEGER PRIMARY KEY, Title TEXT NOT NULL);
CREATE TABLE Track (TrackId INTEGER PRIMARY KEY, AlbumId INTEGER NOT NULL,
  Name TEXT NOT NULL, Milliseconds INTEGER NOT NULL);
CREATE TABLE Invoice (InvoiceId INTEGER PRIMARY KEY, CustomerId INTEGER NOT NULL,
  InvoiceDate TEXT NOT NULL, TotalCents INTEGER NOT NULL);
CREATE TABLE InvoiceLine (InvoiceLineId INTEGER PRIMARY KEY, InvoiceId INTEGER NOT NULL,
  TrackId INTEGER NOT NULL, UnitPriceCents INTEGER NOT NULL, Quantity INTEGER NOT NULL);

INSERT INTO Employee VALUES (1,'Support Alpha'),(2,'Support Beta');
INSERT INTO Customer VALUES
  (1,'Customer Alpha','USA','alpha@example.test',1),
  (2,'Customer Beta','Canada','beta@example.test',2),
  (3,'Customer Gamma','Germany','gamma@example.test',NULL);
INSERT INTO Album VALUES (1,'Synthetic Album A'),(2,'Synthetic Album B'),(3,'Empty Album');
INSERT INTO Track VALUES
  (1,1,'Love Example A',300000),(2,1,'Love Example B',350000),
  (3,2,'Another Example',200000);
INSERT INTO Invoice VALUES
  (101,1,'2026-01-01',300),(102,2,'2026-01-02',250),
  (103,999,'2026-01-03',100);
INSERT INTO InvoiceLine VALUES
  (1,101,1,100,1),(2,101,2,100,2),(3,102,3,100,2),(4,103,1,100,1);
