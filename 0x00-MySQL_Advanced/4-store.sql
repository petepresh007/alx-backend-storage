-- Create the trigger to decrease item quantity after a new order is added
DELIMITER //

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- NEW refers to the new row being inserted into the orders table
    UPDATE items
    SET quantity = quantity - NEW.number -- Decrease the quantity by the number in the new order
    WHERE name = NEW.item_name; -- Match the item by name
END //

DELIMITER ;
