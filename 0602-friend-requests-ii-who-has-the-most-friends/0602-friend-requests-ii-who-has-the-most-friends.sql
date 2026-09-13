# Write your MySQL query statement below
WITH FriendCounts AS (
    SELECT 
        id, 
        COUNT(*) AS num
    FROM (
        SELECT requester_id AS id FROM RequestAccepted
        UNION ALL
        SELECT accepter_id AS id FROM RequestAccepted
    ) AS AllFriends
    GROUP BY 
        id
)
SELECT 
    id, 
    num
FROM 
    FriendCounts
WHERE 
    num = (SELECT MAX(num) FROM FriendCounts);