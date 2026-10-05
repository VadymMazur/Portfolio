-- name: customers_by_country
SELECT CustomerId, Name, Country FROM Customer
WHERE Country IN ('USA', 'Canada') ORDER BY Name, CustomerId;

-- name: longest_matching_tracks
SELECT TrackId, Name, Milliseconds FROM Track
WHERE Name LIKE '%Love%' ORDER BY Milliseconds DESC, TrackId LIMIT 5;

-- name: invoice_range
SELECT InvoiceId, TotalCents FROM Invoice
WHERE TotalCents BETWEEN 200 AND 300 ORDER BY TotalCents DESC, InvoiceId;

-- name: revenue_by_country
SELECT c.Country, COUNT(*) AS InvoiceCount, SUM(i.TotalCents) AS RevenueCents
FROM Invoice i JOIN Customer c ON c.CustomerId = i.CustomerId
GROUP BY c.Country HAVING SUM(i.TotalCents) >= 250
ORDER BY RevenueCents DESC, c.Country;

-- name: album_track_counts
SELECT a.AlbumId, a.Title, COUNT(t.TrackId) AS TrackCount
FROM Album a LEFT JOIN Track t ON t.AlbumId = a.AlbumId
GROUP BY a.AlbumId, a.Title ORDER BY TrackCount DESC, a.AlbumId;

-- name: customer_support
SELECT c.CustomerId, c.Name, e.Name AS SupportRep
FROM Customer c LEFT JOIN Employee e ON e.EmployeeId = c.SupportRepId
ORDER BY c.CustomerId;

-- name: invoice_details
SELECT il.InvoiceId, t.Name, il.UnitPriceCents, il.Quantity
FROM InvoiceLine il JOIN Track t ON t.TrackId = il.TrackId
ORDER BY il.InvoiceId, il.InvoiceLineId;

-- name: orphan_invoices
SELECT i.InvoiceId, i.CustomerId FROM Invoice i
LEFT JOIN Customer c ON c.CustomerId = i.CustomerId
WHERE c.CustomerId IS NULL ORDER BY i.InvoiceId;

-- name: mismatched_totals
SELECT i.InvoiceId, i.TotalCents,
       COALESCE(SUM(il.UnitPriceCents * il.Quantity), 0) AS CalculatedCents
FROM Invoice i LEFT JOIN InvoiceLine il ON il.InvoiceId = i.InvoiceId
GROUP BY i.InvoiceId, i.TotalCents
HAVING i.TotalCents <> COALESCE(SUM(il.UnitPriceCents * il.Quantity), 0)
ORDER BY i.InvoiceId;

-- name: customers_without_invoices
SELECT c.CustomerId FROM Customer c
WHERE NOT EXISTS (SELECT 1 FROM Invoice i WHERE i.CustomerId = c.CustomerId)
ORDER BY c.CustomerId;
