-- Write your PostgreSQL query statement below

with DailyTotals as (
    select visited_on, sum(amount) as daily_amount
    from Customer group by visited_on
),
MovingStats as(
    select visited_on, sum(daily_amount) over w as amount,
    round(avg(daily_amount) over w, 2) as average_amount,
    count(visited_on) over w as days_count from DailyTotals window w as (order by visited_on rows between 6 PRECEDING and current row)
)

select visited_on, amount, average_amount from MovingStats where days_count = 7 order by visited_on
