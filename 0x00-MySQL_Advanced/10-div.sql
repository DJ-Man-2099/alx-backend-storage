-- 11th Task
DROP FUNCTION IF EXISTS `SafeDiv`;

DELIMITER // 

CREATE FUNCTION `SafeDiv`
(a INT,
b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
IF b = 0 THEN 
RETURN 0;
ELSE
RETURN CAST(a AS DOUBLE)/b;
END IF;
END //

DELIMITER ;
