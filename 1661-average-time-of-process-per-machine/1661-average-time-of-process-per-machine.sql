# Write your MySQL query statement below
select a.machine_id, round(avg(b.timestamp - a.timestamp), 3) as processing_time from Activity a join Activity b on a.machine_id = b.machine_id
and a.process_id = b.process_id where a.activity_type = 'start' and b.activity_type = 'end' group by a.machine_id;









-- | machine_id | activity_type | machine_id | activity_type |
-- | ---------- | ------------- | ---------- | ------------- |
-- | 0          | start         | 0          | end           |
-- | 0          | start         | 0          | end           |
-- | 1          | start         | 1          | end           |
-- | 1          | start         | 1          | end           |
-- | 2          | start         | 2          | end           |
-- | 2          | start         | 2          | end           |