UPDATE stock
SET is_weekend = CASE
    WHEN EXTRACT(DOW FROM date) IN (0, 6) THEN 'Yes'
    ELSE 'No'
END;
