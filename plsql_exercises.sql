
---------------------------------------------------------
-- PL/SQL Exercises Solutions (1–17)
-- Generated for practice
---------------------------------------------------------

-- Exercise 1: Annual Salary
DECLARE
    basic_salary NUMBER := 30000;
    bonus        NUMBER := 5000;
    annual_salary NUMBER;
BEGIN
    annual_salary := (basic_salary * 12) + bonus;
    DBMS_OUTPUT.PUT_LINE('Annual Salary = ' || annual_salary);
END;
/

-- Exercise 2: Average of 3 Subjects
DECLARE
    sub1 NUMBER := 85;
    sub2 NUMBER := 78;
    sub3 NUMBER := 92;
    avg_marks NUMBER;
BEGIN
    avg_marks := (sub1 + sub2 + sub3) / 3;
    DBMS_OUTPUT.PUT_LINE('Average Marks = ' || avg_marks);
END;
/

-- Exercise 3: Bank Balance Check
DECLARE
    balance NUMBER := 3200;
BEGIN
    IF balance < 1000 THEN
        DBMS_OUTPUT.PUT_LINE('Low Balance');
    ELSIF balance BETWEEN 1000 AND 5000 THEN
        DBMS_OUTPUT.PUT_LINE('Sufficient Balance');
    ELSE
        DBMS_OUTPUT.PUT_LINE('High Balance');
    END IF;
END;
/

-- Exercise 4: Grading System
DECLARE
    percentage NUMBER := 82;
    grade VARCHAR2(10);
BEGIN
    grade := CASE 
                WHEN percentage BETWEEN 90 AND 100 THEN 'A Grade'
                WHEN percentage BETWEEN 75 AND 89 THEN 'B Grade'
                WHEN percentage BETWEEN 50 AND 74 THEN 'C Grade'
                ELSE 'Fail'
             END;
    DBMS_OUTPUT.PUT_LINE('Result: ' || grade);
END;
/

-- Exercise 5: Shopping Discount
DECLARE
    bill_amount NUMBER := 4500;
    final_bill  NUMBER;
BEGIN
    IF bill_amount > 5000 THEN
        final_bill := bill_amount - (bill_amount * 0.20);
    ELSIF bill_amount BETWEEN 2000 AND 5000 THEN
        final_bill := bill_amount - (bill_amount * 0.10);
    ELSE
        final_bill := bill_amount;
    END IF;
    DBMS_OUTPUT.PUT_LINE('Final Bill after discount = ' || final_bill);
END;
/

-- Exercise 6: Multiplication Table
DECLARE
    n NUMBER := 7;
BEGIN
    FOR i IN 1..10 LOOP
        DBMS_OUTPUT.PUT_LINE(n || ' x ' || i || ' = ' || (n * i));
    END LOOP;
END;
/

-- Exercise 7: Print Employee IDs (100–120)
BEGIN
    FOR emp_id IN 100..120 LOOP
        DBMS_OUTPUT.PUT_LINE('Employee ID = ' || emp_id);
    END LOOP;
END;
/

-- Exercise 8: Factorial Using WHILE
DECLARE
    n NUMBER := 5;
    fact NUMBER := 1;
    i NUMBER := 1;
BEGIN
    WHILE i <= n LOOP
        fact := fact * i;
        i := i + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Factorial of ' || n || ' = ' || fact);
END;
/

-- Exercise 9: Countdown Timer
BEGIN
    FOR i IN REVERSE 1..10 LOOP
        DBMS_OUTPUT.PUT_LINE(i);
    END LOOP;
END;
/

-- Exercise 10: Print IT Department Employees
DECLARE
    CURSOR c_emp IS
        SELECT emp_name FROM employees WHERE dept_id = 10;
BEGIN
    FOR rec IN c_emp LOOP
        DBMS_OUTPUT.PUT_LINE('Employee: ' || rec.emp_name);
    END LOOP;
END;
/

-- Exercise 11: Salary Increase (if salary < 3000)
DECLARE
    CURSOR c_emp IS
        SELECT emp_id, salary FROM employees WHERE salary < 3000;
BEGIN
    FOR rec IN c_emp LOOP
        UPDATE employees
        SET salary = salary * 1.10
        WHERE emp_id = rec.emp_id;
        DBMS_OUTPUT.PUT_LINE('Updated salary for Employee ID: ' || rec.emp_id);
    END LOOP;
    COMMIT;
END;
/

-- Exercise 12: Employees Above Average Salary
DECLARE
    v_avg NUMBER;
BEGIN
    SELECT AVG(salary) INTO v_avg FROM employees;
    FOR rec IN (SELECT emp_name, salary FROM employees WHERE salary > v_avg) LOOP
        DBMS_OUTPUT.PUT_LINE(rec.emp_name || ' earns ' || rec.salary);
    END LOOP;
END;
/

-- Exercise 13: Categorize Employees by Salary
DECLARE
    CURSOR c_emp IS
        SELECT emp_name, salary FROM employees;
BEGIN
    FOR rec IN c_emp LOOP
        IF rec.salary > 8000 THEN
            DBMS_OUTPUT.PUT_LINE(rec.emp_name || ' → High Earner');
        ELSIF rec.salary BETWEEN 4000 AND 8000 THEN
            DBMS_OUTPUT.PUT_LINE(rec.emp_name || ' → Mid Earner');
        ELSE
            DBMS_OUTPUT.PUT_LINE(rec.emp_name || ' → Low Earner');
        END IF;
    END LOOP;
END;
/

-- Exercise 14: Total Salary per Department
DECLARE
    CURSOR c_dept IS
        SELECT dept_id, SUM(salary) AS total_salary
        FROM employees
        GROUP BY dept_id;
BEGIN
    FOR rec IN c_dept LOOP
        DBMS_OUTPUT.PUT_LINE('Dept ' || rec.dept_id || ' → Total Salary = ' || rec.total_salary);
    END LOOP;
END;
/

-- Exercise 15: Fibonacci Sequence
DECLARE
    n NUMBER := 10;
    a NUMBER := 0;
    b NUMBER := 1;
    c NUMBER;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Fibonacci Sequence up to ' || n || ' terms:');
    DBMS_OUTPUT.PUT_LINE(a);
    DBMS_OUTPUT.PUT_LINE(b);
    FOR i IN 3..n LOOP
        c := a + b;
        DBMS_OUTPUT.PUT_LINE(c);
        a := b;
        b := c;
    END LOOP;
END;
/

-- Exercise 16: Process Bank Transactions
DECLARE
    v_balance NUMBER := 0;
BEGIN
    FOR rec IN (SELECT amount, type FROM transactions) LOOP
        IF rec.type = 'CREDIT' THEN
            v_balance := v_balance + rec.amount;
        ELSIF rec.type = 'DEBIT' THEN
            v_balance := v_balance - rec.amount;
        END IF;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('Final Account Balance = ' || v_balance);
END;
/

-- Exercise 17: Employee Details Procedure
CREATE OR REPLACE PROCEDURE get_employee_details(p_emp_id NUMBER) IS
    v_name employees.emp_name%TYPE;
    v_salary employees.salary%TYPE;
    v_dept_name VARCHAR2(50);
BEGIN
    SELECT e.emp_name, e.salary, d.dept_name
    INTO v_name, v_salary, v_dept_name
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    WHERE e.emp_id = p_emp_id;

    DBMS_OUTPUT.PUT_LINE('Employee Name: ' || v_name);
    DBMS_OUTPUT.PUT_LINE('Department: ' || v_dept_name);
    DBMS_OUTPUT.PUT_LINE('Salary: ' || v_salary);
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No employee found with ID ' || p_emp_id);
END;
/

-- Example call for Exercise 17
BEGIN
    get_employee_details(101);
END;
/
