DO $$
DECLARE
    v_bill_id INTEGER := 1;   -- change to test different bills
    v_product_id INTEGER;
    v_quantity INTEGER;
BEGIN
    -- 1. Verify the bill exists
    IF NOT EXISTS (SELECT 1 FROM Bills WHERE ID = v_bill_id) THEN
        RAISE EXCEPTION 'Bill % does not exist', v_bill_id;
    END IF;

    -- Optional: prevent returning a bill that's already returned
    IF EXISTS (SELECT 1 FROM Bills WHERE ID = v_bill_id AND Status = 'Retornada') THEN
        RAISE EXCEPTION 'Bill % has already been returned', v_bill_id;
    END IF;

    -- 2. Increase stock for each product on this bill
    FOR v_product_id, v_quantity IN
        SELECT ProductID, Quantity FROM Bill_Products WHERE BillID = v_bill_id
    LOOP
        UPDATE Products
        SET Stock = Stock + v_quantity
        WHERE ID = v_product_id;
    END LOOP;

    -- 3. Mark the bill as returned
    UPDATE Bills
    SET Status = 'Retornada'
    WHERE ID = v_bill_id;

    RAISE NOTICE 'Bill % successfully returned. Stock restored.', v_bill_id;
END $$;

