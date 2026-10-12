-- Write your PostgreSQL query statement below

select Department, Employee, salary from (
    select d.name as Department, e.name as Employee, e.salary, dense_rank() over (partition by d.name order by salary desc)
    from Employee e join department d on d.id = e.departmentId
) where dense_rank <= 3