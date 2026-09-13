# Write your MySQL query statement below
WITH DailyTotal AS (
    SELECT 
        visited_on, 
        SUM(amount) AS daily_amount
    FROM 
        Customer
    GROUP BY 
        visited_on
),
MovingStats AS (
    SELECT 
        visited_on,
        SUM(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS amount,
        ROUND(AVG(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ), 2) AS average_amount,
        COUNT(daily_amount) OVER (
            ORDER BY visited_on 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) AS days_count
    FROM 
        DailyTotal
)
SELECT 
    visited_on, 
    amount, 
    average_amount
FROM 
    MovingStats
WHERE 
    days_count = 7
ORDER BY 
    visited_on ASC;