# Write your MySQL query statement below
-- select v.customer_id, count(customer_id) as count_no_trans from Visits v
-- where v.visit_id not in (
--     select v.visit_id from Visits join Transactions t on
--     v.visit_id = t.visit_id
-- ) group by customer_id;


select customer_id, count(*) as count_no_trans from Visits v left join Transactions t on
v.visit_id = t.visit_id where transaction_id is null group by customer_id;