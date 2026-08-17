DO $$
DECLARE
    v_user_id INTEGER := 1;                    -- change to test different users
    v_product_ids INTEGER[] := ARRAY[1, 2];     -- products being purchased
    v_quantities INTEGER[] := ARRAY[2, 5];      -- matching quantities
    v_bill_id INTEGER;
    v_current_stock INTEGER;
    i INTEGER;
BEGIN
    -- 1. Confirm the user exists
    IF NOT EXISTS (SELECT 1 FROM Users WHERE ID = v_user_id) THEN
        RAISE EXCEPTION 'User % does not exist', v_user_id;
    END IF;

    -- 2. Check stock is sufficient for EVERY product before doing anything
    FOR i IN 1 .. array_length(v_product_ids, 1) LOOP
        SELECT Stock INTO v_current_stock
        FROM Products
        WHERE ID = v_product_ids[i];

        IF v_current_stock IS NULL THEN
            RAISE EXCEPTION 'Product % does not exist', v_product_ids[i];
        END IF;

        IF v_current_stock < v_quantities[i] THEN
            RAISE EXCEPTION 'Not enough stock for product %. Available: %, Requested: %',
                v_product_ids[i], v_current_stock, v_quantities[i];
        END IF;
    END LOOP;

    -- 3. Insert the bill
    INSERT INTO Bills (UserID, Status)
    VALUES (v_user_id, 'Active')
    RETURNING ID INTO v_bill_id;

    -- 4. Insert each line item and reduce stock
    FOR i IN 1 .. array_length(v_product_ids, 1) LOOP
        INSERT INTO Bill_Products (BillID, ProductID, Quantity)
        VALUES (v_bill_id, v_product_ids[i], v_quantities[i]);

        UPDATE Products
        SET Stock = Stock - v_quantities[i]
        WHERE ID = v_product_ids[i];
    END LOOP;

    RAISE NOTICE 'Purchase completed successfully. Bill ID: %', v_bill_id;
END $$;